import importlib
import sys
import unittest
from unittest import mock


class ImportTests(unittest.TestCase):
    def test_pyrec_imports_without_recutils(self):
        with mock.patch.dict(sys.modules, {'recutils': mock.MagicMock()}):
            module = importlib.import_module('pyrec')
            self.assertTrue(hasattr(module, 'Recdb'))


if __name__ == '__main__':
    unittest.main()
