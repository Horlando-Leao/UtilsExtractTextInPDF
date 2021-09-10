import os
import subprocess
import uuid

def get_list_name_files(APP_FOLDER:str, EXTESION_FILES:str) -> list:

    NameFiles = []
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching files in : ',base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                NameFiles.append(Files)
    return NameFiles

def get_number_of_files(APP_FOLDER:str, EXTESION_FILES:str) -> int:

    totalFiles = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching number of files in : ',base)
        for Files in files:
            if Files.lower().endswith(f'.{EXTESION_FILES}'):
                totalFiles += 1
    print('Total number of files',totalFiles)
    return int(totalFiles)

def get_platform():
    import platform
    PLTAFORM = platform.system()
    if PLTAFORM == 'Windows':
        return 'Windows'
    elif PLTAFORM == 'Linux' or PLTAFORM == 'Linux2' or PLTAFORM == 'Linux3':
        return 'Linux'
    else:
        return 'Others Plataforms'
    
def generate_file_bat(list_commands:list = [], path_save:str="bin/windows/executable.bat"):
    if len(list_commands) > 0:
        with open(path_save, 'w') as file_bat:
            for command in list_commands:
                file_bat.write(f'{command}\n')

def extractPDF_text(PATH_FILES:str):
    if get_platform() == 'Windows':
        try:
            list_files = get_list_name_files(PATH_FILES, 'pdf')
            list_commands = []
            for file in list_files:
                list_commands.append(f'START /WAIT java -jar ./bin/java/pdfbox-app-2.0.19.jar ExtractText {PATH_FILES}/{file}')
            
            generate_file_bat(list_commands)
            path_bat  = os.path.abspath("bin/windows/executable.bat")
            subprocess.call([r'{0}'.format(path_bat)])
            
        except FileNotFoundError:
            raise FileNotFoundError("File ./bin/windows/executable.bat not found")

def clear_text_file_non_ut8(path:str='', path_save:str='', extension:str='txt'):
    list_files = get_list_name_files(path, extension)
    print(list_files)

    for file in list_files:
        with open(f'{path}/{file}', 'r', encoding='utf8') as file_txt:

            file_contents = file_txt.read()
            file_contents.encode('utf-8','ignore').decode("utf-8")

            with open(f'{path_save}/{str(uuid.uuid4())}.{extension}', 'w', encoding='utf8') as new_file_txt:
                new_file_txt.write(file_contents)