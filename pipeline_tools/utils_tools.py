import os
import subprocess
import uuid
import platform
from typing import Union, List
import pathlib


def get_list_name_files(app_folder: Union[str, pathlib.Path], extesion_files: str) -> List[str]:
    """Não suporte subdiretorios"""

    name_files = []

    for base, dirs, files in os.walk(app_folder):
        print('Searching files in : ', base)
        for Files in files:
            if Files.lower().endswith(f'.{extesion_files}'):
                name_files.append(Files)

    return name_files


def get_number_of_files(app_folder: Union[str, pathlib.Path], extesion_files: str) -> int:
    """Não suporte subdiretorios"""

    total_files = 0

    for base, dirs, files in os.walk(app_folder):
        print('Searching number of files in : ', base)
        for file in files:
            if file.lower().endswith(f'.{extesion_files}'):
                total_files += 1
    print('Total number of files', total_files)

    return int(total_files)


def get_platform() -> str:
    this_platform = platform.system()

    if this_platform == 'Windows':
        return 'Windows'
    elif this_platform == 'Linux' or this_platform == 'Linux2' or this_platform == 'Linux3':
        return 'Linux'
    else:
        return 'Others Plataforms'


def generate_file_bat(list_commands: List[str] = [],
                      path_save: Union[str, pathlib.Path] = "bin/windows/executable.bat"):

    if len(list_commands) > 0:
        with open(path_save, 'w') as file_bat:
            file_bat.write("echo off\n")
            for command in list_commands:
                file_bat.write(f'{command}\n')


def extract_text_on_pdf(PATH_FILES: Union[str, pathlib.Path]):

    if get_platform() == 'Windows':
        try:
            list_files = get_list_name_files(PATH_FILES, 'pdf')
            list_commands = []
            for file in list_files:
                list_commands.append(
                    f'START /WAIT java -jar ./bin/java/pdfbox-app-2.0.19.jar ExtractText {PATH_FILES}/{file}')

            generate_file_bat(list_commands)

            try:
                path_bat = os.path.abspath("bin/windows/executable.bat")
                subprocess.call([r'{0}'.format(path_bat)])
            except FileNotFoundError:
                path_bat = os.path.abspath("GenarateDatabaseProdigyCV/bin/windows/executable.bat")
                subprocess.call([r'{0}'.format(path_bat)])
        except FileNotFoundError:
            raise FileNotFoundError("File executable.bat not found")


def clear_text_file_non_ut8(path: Union[str, pathlib.Path] = '', path_save: Union[str, pathlib.Path] = '',
                            extension: str = 'txt'):

    from pipeline_tools.tools_regex import clean_cv_underlines_with_space
    from pipeline_tools.variables_main import list_str_garbage, dict_str_gargabe_with_str_replace

    list_files = get_list_name_files(path, extension)

    for file in list_files:
        with open(f'{path}\\{file}', 'r', encoding='utf8') as file_txt:

            file_contents = file_txt.read()
            file_contents = file_contents.encode('utf-8', 'ignore').decode("utf-8")
            file_contents = str(file_contents)

            if file_contents != '':

                file_contents = clean_cv_underlines_with_space(file_contents)

                for str_remove in list_str_garbage:
                    file_contents = file_contents.replace(str_remove, ' ')

                for str_find, str_rep in dict_str_gargabe_with_str_replace.items():
                    file_contents = file_contents.replace(str_find, str_rep)

                with open(f'{path_save}/{str(uuid.uuid4())}.{extension}', 'w', encoding='utf8') as new_file_txt:
                    new_file_txt.write(file_contents)


def make_database_for_prodigy(path_list_txt: Union[str, pathlib.Path], path_save_json: Union[str, pathlib.Path],
                              extension_find_path='txt'):
    list_files_name = get_list_name_files(path_list_txt, extension_find_path)

    def format_jsonl_with_db_prodigy(content: str = ''):

        open_str = '{"text":"'
        middle_str = str(content)
        close_str = '"}\n'

        return f'{open_str}{middle_str}{close_str}'

    print(list_files_name)

    for file in list_files_name:
        with open(f'{path_save_json}', 'a', encoding='utf8') as file_jsonl:
            with open(f'{path_list_txt}\\{file}', 'r', encoding='utf8') as file_txt:
                file_contents = file_txt.read()
                file_jsonl.write(format_jsonl_with_db_prodigy(file_contents))


def renames_all_files(path: Union[str, pathlib.Path], extesion: str):

    for file in get_list_name_files(path, extesion):
        old_name_file = f'{path}/{file}'
        new_name_file = f'{path}/{str(uuid.uuid4())}.{extesion}'
        os.rename(old_name_file, new_name_file)


