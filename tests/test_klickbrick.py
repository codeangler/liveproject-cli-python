from klickbrick_codeangler.__init__ import __version__
import klickbrick_codeangler.main as klickbrick
import unittest

if __name__ == "__main__":
    parser = create_parser()
    args = parser.args()

def test_version():
    assert __version__ == '0.1.0'

class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class TestKlickBrick(unittest.TestCase):
        def test_hello_world(self):
            noArg = klickbrick.greeting();
            self.assertEqual(noArg, 'Hello World.')


