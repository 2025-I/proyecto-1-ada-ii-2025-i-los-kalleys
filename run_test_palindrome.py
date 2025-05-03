import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('src'))

specific_test_folder = os.path.join('tests', 'palindrome')
suite = unittest.defaultTestLoader.discover(specific_test_folder, pattern='test*.py')

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)