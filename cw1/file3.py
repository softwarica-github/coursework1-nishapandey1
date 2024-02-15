import unittest
import socket

def ip_host(host, port=80):
    try:
        sock = socket.create_connection((host, port), timeout=1)
        return True
    except OSError:
        return False

class TestIpHost(unittest.TestCase):
    def test_ip_host_valid_host(self):
        self.assertTrue(ip_host("google.com"))

    def test_ip_host_invalid_host(self):
        self.assertFalse(ip_host("this-is-an-invalid-host.com"))

    def test_ip_host_valid_port(self):
        self.assertTrue(ip_host("google.com", 80))

    def test_ip_host_invalid_port(self):
        self.assertFalse(ip_host("google.com", -1))

if __name__ == '__main__':
    unittest.main()