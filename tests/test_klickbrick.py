from klickbrick import __version__
import unittest

def test_version():
    assert __version__ == '0.1.0'

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
