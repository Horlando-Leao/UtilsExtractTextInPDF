"""Tentando resolver problema de importação"""

from unittest import TestCase, main
from pipeline_tools.utils_tools import get_platform


class TesteUtilsTools(TestCase):

    def test_get_name_system_for_windows(self):
        valor_esperado = 'Windows'
        self.assertEqual(get_platform(), valor_esperado)

    def test_get_name_system_for_windows2(self):
        valor_esperado = 'Windows'
        self.assertEqual(get_platform(), valor_esperado)



main()
