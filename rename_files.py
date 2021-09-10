"""
Script python para renomar todos os arquivos de um diretorio
Os nomes serão uma cadeia de caracteres aleatorios
Esse script recebe apenas dois argumentos posicionais: 
1=<Caminho do diretorio>, 
2=<extensão do arquivo para match>.
"""

import os
import sys
import uuid
from utils_tools import get_list_name_files, get_number_of_files

sys.argv[0]='rename_files.py'

PATH_FILES = str(sys.argv[1]) #path directory
EXTESION_FILES = str(sys.argv[2]).lower()# set extension pdf or doc or others, without dot "."

if __name__ == '__main__' and get_number_of_files(PATH_FILES, EXTESION_FILES) > 0:
    for file in get_list_name_files(PATH_FILES, EXTESION_FILES):
        old_name_file = f'{PATH_FILES}/{file}'
        new_name_file = f'{PATH_FILES}/{str(uuid.uuid4())}.{EXTESION_FILES}'
        os.rename(old_name_file, new_name_file)


