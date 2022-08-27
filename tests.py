import os
import subprocess
import unittest


class TestMemory(unittest.TestCase):
    def test_simple(self):
        process = subprocess.run(
            os.path.abspath("memory") + ' python3 -c "import time; time.sleep(1);"',
            shell=True,
            universal_newlines=True,
            stderr=subprocess.PIPE,
        )
        print(process.stderr)
        self.assertEqual(process.returncode, 0)
        self.assertGreater(len(process.stderr), 50)
