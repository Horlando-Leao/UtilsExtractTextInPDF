import os
import subprocess
import uuid
import platform



def get_list_name_files(APP_FOLDER: str, EXTESION_FILES: str) -> list:
    """Não suporte subdiretorios"""

    NameFiles = []

    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching files in : ', base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                NameFiles.append(Files)

    return NameFiles


def get_number_of_files(APP_FOLDER: str, EXTESION_FILES: str) -> int:
    """Não suporte subdiretorios"""
    totalFiles = 0

    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching number of files in : ', base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                totalFiles += 1
    print('Total number of files', totalFiles)

    return int(totalFiles)


def get_platform():
    PLTAFORM = platform.system()

    if PLTAFORM == 'Windows':
        return 'Windows'
    elif PLTAFORM == 'Linux' or PLTAFORM == 'Linux2' or PLTAFORM == 'Linux3':
        return 'Linux'
    else:
        return 'Others Plataforms'


def generate_file_bat(list_commands: list = [], path_save: str = "bin/windows/executable.bat"):
    if len(list_commands) > 0:
        with open(path_save, 'w') as file_bat:
            for command in list_commands:
                file_bat.write(f'{command}\n')


def extractPDF_text(PATH_FILES: str):
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


def clear_text_file_non_ut8(path: str = '', path_save: str = '', extension: str = 'txt'):

    from pipeline_tools.main.variables_main import list_str_garbage
    list_files = get_list_name_files(path, extension)

    for file in list_files:
        with open(f'{path}/{file}', 'r', encoding='utf8') as file_txt:

            file_contents = file_txt.read()
            file_contents = file_contents.encode('utf-8', 'ignore').decode("utf-8")
            file_contents = str(file_contents)

            for str_remove in list_str_garbage:
                file_contents = file_contents.replace(str_remove, ' ')

            with open(f'{path_save}/{str(uuid.uuid4())}.{extension}', 'w', encoding='utf8') as new_file_txt:
                new_file_txt.write(file_contents)


def make_database_for_prodigy(path_list_txt: str, path_save_json: str, extension_find_path='txt'):
    list_files_name = get_list_name_files(path_list_txt, extension_find_path)

    def format_jsonl_with_db_prodigy(content: str = ''):
        open_str = '{"text":"'
        middle_str = str(content)
        close_str = '"}\n'
        return f'{open_str}{middle_str}{close_str}'

    print(list_files_name)

    for file in list_files_name:
        with open(f'{path_save_json}', 'a', encoding='utf8') as file_jsonl:
            with open(f'{path_list_txt}/{file}', 'r', encoding='utf8') as file_txt:
                file_contents = file_txt.read()
                file_jsonl.write(format_jsonl_with_db_prodigy(file_contents))


def renames_all_files(path, extesion):
    for file in get_list_name_files(path, extesion):
        old_name_file = f'{path}/{file}'
        new_name_file = f'{path}/{str(uuid.uuid4())}.{extesion}'
        os.rename(old_name_file, new_name_file)
