import os
import sys
import unittest

sys.path.insert(0, os.path.abspath("src"))

suite = unittest.defaultTestLoader.discover("tests", pattern="test_*.py")

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
