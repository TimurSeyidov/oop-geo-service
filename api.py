import json
import os.path
import sys
import logging
from typing import Any
from flask import Flask, request, make_response
from geo import Application as BaseApplication
from geo import Ip
from telegram import Telegram
from telegram.classes import Message


class Application(BaseApplication):
    def __init__(self, env_file: str):
        super().__init__(env_file)
        self.app = Flask(__name__)

    def __prepare_init(self):
        logger_format = logging.Formatter(
            '%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s'
        )
        log_folder = os.path.abspath('./logs')
        if not os.path.exists(log_folder) or not os.path.isdir(log_folder):
            os.makedirs(log_folder, 0o755)
        logger_root = logging.getLogger()
        file_handler = logging.FileHandler(f'{log_folder}/app.log')
        file_handler.setFormatter(logger_format)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logger_format)
        logger_root.addHandler(file_handler)
        logger_root.addHandler(console_handler)
        logger_root.setLevel(logging.DEBUG)
        requires = ['telegram_token', 'telegram_url']
        for param in requires:
            p = self.get_param(param)
            if not p:
                logging.error(f'Param "{p} is empty or undefined')
                sys.exit()

    def __response(self, data: Any = None, status: int = 200):
        response = {
            'status': None,
            'message': None,
            'data': None
        }
        if 200 <= status < 300:
            response['status'] = 'success'
            response['data'] = data
        else:
            response['status'] = 'error'
            response['message'] = str(data)
        response = make_response(json.dumps(response), status)
        response.headers['Content-Type'] = 'application/json'
        return response

    def run(self):
        self.__prepare_init()
        try:
            telegram_token = self.get_param('telegram_token')
            telegram_url = self.get_param('telegram_url')
            t = Telegram.connect(telegram_token, f'{telegram_url}/{telegram_token}', self.http)
        except Exception as e:
            logging.error(e)
            sys.exit()

        @self.app.route(f'/{telegram_token}', methods=['GET', 'POST'])
        def telegram():
            if request.method == 'POST':
                message = t.parse(request.json)
                try:
                    logging.info(f'Input message: {message}')
                    ip = Ip(message.text.strip())
                    data = self.get_ip_info(ip)
                    if not data:
                        raise Exception(f'Data for ip {ip.value} not found')
                    resp_message = t.send_message(Message(text=str(data), chat=message.chat))
                    logging.info(f'Response of sended message: {resp_message}')
                    resp_location = t.send_location(message.chat, data.point)
                    logging.info(f'Response of sended location: {resp_location}')
                except Exception as e:
                    logging.error(e)
                    t.send_message(Message(text=str(e), chat=message.chat))
            return make_response({'ok': True})

        @self.app.route('/ip')
        def get_ip():
            p_ip = request.args.get('ip', '')
            try:
                ip = Ip(p_ip)
            except Exception as e:
                return self.__response(e, 400)
            try:
                data = self.get_ip_info(ip)
                if not data:
                    return self.__response(f'Info about {ip.value} not found', 404)
                return self.__response(data.dict)
            except Exception as e:
                logging.error(e)
                return self.__response('Internal errors', status=504)

        self.app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    app = Application('./.env')
    app.run()
