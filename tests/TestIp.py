import unittest
from geo import Ip


class TestIp(unittest.TestCase):
    def test_success(self):
        v4 = '127.0.0.1'
        v6 = '2001:db8:85a3::8a2e:370:7334'
        ip_v4 = Ip(v4)
        ip_v6 = Ip(v6)
        self.assertEqual(ip_v4.value, v4)
        self.assertEqual(ip_v6.value, v6)
        self.assertTrue(ip_v4.is_ip_v4)
        self.assertTrue(ip_v6.is_ip_v6)

    def test_failed(self):
        with self.assertRaises(ValueError):
            Ip('')
        with self.assertRaises(ValueError):
            Ip('asasdas')


if __name__ == '__main__':
    unittest.main()
