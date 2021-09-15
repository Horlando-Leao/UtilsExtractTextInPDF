"""Tentando resolver problema de importação"""

from unittest import TestCase, main
from pipeline_tools.utils_tools import get_platform, get_list_name_files, get_number_of_files, renames_all_files, \
    clear_text_file_non_ut8, generate_file_bat, extract_text_on_pdf, make_database_for_prodigy
from pipeline_tools.tools_regex import clean_cv_underlines_with_space
from pipeline_tools.variables_main import list_str_garbage, dict_str_gargabe_with_str_replace


class TestUtilsTools(TestCase):

    def test_get_platform(self):
        """test_get_platform"""

        valor_esperado = 'Windows'
        self.assertEqual(get_platform(), valor_esperado)

    def test_get_list_name_files(self):
        """test_get_list_name_files"""

        pass

    def test_get_number_of_files(self):
        """test_get_number_of_files"""

        pass

    def test_renames_all_files(self):
        """test_renames_all_files"""

        pass

    def test_clear_text_file_non_ut8(self):
        """test_clear_text_file_non_ut8"""

        pass

    def test_generate_file_bat(self):
        """test_generate_file_bat"""

        pass

    def test_extract_text_on_pdf(self):
        """test_extract_text_on_pdf"""

        pass

    def test_make_database_for_prodigy(self):
        """test_make_database_for_prodigy"""

        pass

    def test_clean_cv_underlines_with_space(self):
        """test_clean_cv_underlines_with_space"""

        pass

    def test_dict_str_gargabe_with_str_replace(self):
        """dict_str_gargabe_with_str_replace"""

        pass

    def test_list_str_garbage(self):
        """list_str_garbage"""

        pass

main()
