from geo import Application as BaseApplication
from geo import Ip, Place


class Application(BaseApplication):
    def run(self):
        while True:
            value = input('Enter ip: ')
            try:
                ip = Ip(value)
                data = self.get_ip_info(ip)
                if data:
                    print(data)
                    break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    app = Application('./.env')
    app.run()
