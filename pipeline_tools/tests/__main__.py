"""Tentando resolver problema de importação"""

from unittest import TestCase, main

from pipeline_tools.tools_regex import clean_cv_underlines_with_space
from pipeline_tools.utils_tools import clear_text_file_non_ut8, generate_file_bat
from pipeline_tools.utils_tools import get_list_name_files, get_number_of_files, get_platform
from pipeline_tools.variables_main import list_str_garbage, dict_str_gargabe_with_str_replace
from pipeline_tools.utils_tools import make_database_for_prodigy, renames_all_files, extract_text_on_pdf


class TestUtilsTools(TestCase):

    def test_get_platform(self):
        """test_get_platform"""

        value_input = get_platform()
        value_expected = 'Windows'
        self.assertEqual(value_input, value_expected)

    def test_get_list_name_files(self):
        """test_get_list_name_files"""

        value_input = get_list_name_files(app_folder='pipeline_tools/tests/folder_tests/files_txt',
                                          extesion_files='txt')
        value_expected = ['file1.txt', 'file2.txt', 'file3.txt']

        self.assertEqual(value_input, value_expected)

    def test_get_number_of_files(self):
        """test_get_number_of_files"""

        value_input = get_number_of_files(app_folder='pipeline_tools/tests/folder_tests/files_txt',
                                          extesion_files='txt')
        value_expected = 3

        self.assertEqual(value_input, value_expected)

    def test_renames_all_files(self):
        """test_renames_all_files"""
        #renames_all_files()

        pass

    def test_clear_text_file_non_ut8(self):
        """test_clear_text_file_non_ut8"""
        import os, shutil

        value_input = None
        value_expected = ' #  #  texto1  #   #   #   #   #   #   #   # '

        path_files_clean = 'pipeline_tools/tests/folder_tests/files_clean'

        # DELETE ALL FILES IN PATH
        for filename in os.listdir(path_files_clean):
            file_path = os.path.join(path_files_clean, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        # DELETE ALL FILES IN PATH

        clear_text_file_non_ut8(path='pipeline_tools/tests/folder_tests/files_garbage',
                                path_save=path_files_clean)

        first_file = os.listdir(path_files_clean)[0]
        print(first_file)
        with open(f'pipeline_tools/tests/folder_tests/files_clean/{first_file}', 'r', encoding='utf8') as file_clean:
            value_input = file_clean.read()

        self.assertEqual(str(value_input), str(value_expected))

    def test_generate_file_bat(self):
        """test_generate_file_bat"""
        value_input = None
        value_expected = 'echo "hello world"\necho "hello marte"\necho "hello venus"\n'

        commands = ['echo "hello world"', 'echo "hello marte"', 'echo "hello venus"']
        path = 'pipeline_tools/tests/folder_tests/bin/windows/executable.bat'
        generate_file_bat(list_commands=commands, path_save=path)

        with open(f'pipeline_tools/tests/folder_tests/bin/windows/executable.bat', 'r', encoding='utf8') as file_bat:
            value_input = file_bat.read()

        self.assertEqual(value_input, value_expected)



    def test_extract_text_on_pdf(self):
        """test_extract_text_on_pdf"""
        #extract_text_on_pdf()
        pass

    def test_make_database_for_prodigy(self):
        """test_make_database_for_prodigy"""

        value_input = None
        value_expected = '{"text":"texto1"}\n{"text":"texto2"}\n{"text":"texto3"}\n'

        with open(f'pipeline_tools/tests/folder_tests/cv_database/database.jsonl', 'r+', encoding='utf8') as file_jsonl:
            file_jsonl.truncate(0)

        make_database_for_prodigy(path_list_txt='pipeline_tools/tests/folder_tests/files_txt',
                                  path_save_json='pipeline_tools/tests/folder_tests/cv_database/database.jsonl')

        with open(f'pipeline_tools/tests/folder_tests/cv_database/database.jsonl', 'r', encoding='utf8') as file_jsonl:
            value_input = file_jsonl.read()

        self.assertEqual(value_input, value_expected)

    def test_clean_cv_underlines_with_space(self):
        """test_clean_cv_underlines_with_space"""

        text = 'carro-passaro, aviao - comercial, vida-boa, logo-logo, boa - viagem'
        value_input = clean_cv_underlines_with_space(text=text)
        value_expected = 'carro – passaro, aviao  –  comercial, vida – boa, logo – logo, boa  –  viagem'

        self.assertEqual(value_input, value_expected)

    def test_dict_str_gargabe_with_str_replace(self):
        """dict_str_gargabe_with_str_replace"""

        value_input = type(dict_str_gargabe_with_str_replace)
        value_expected = dict
        self.assertEqual(value_input, value_expected)

    def test_list_str_garbage(self):
        """list_str_garbage"""

        value_input = type(list_str_garbage)
        value_expected = list
        self.assertEqual(value_input, value_expected)


main()
