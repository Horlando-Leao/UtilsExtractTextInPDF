"""
Script python para renomar todos os arquivos de um diretorio
Os nomes serão uma cadeia de caracteres aleatorios
Esse script recebe apenas dois argumentos posicionais: 
1=<Caminho do diretorio>, 
2=<extensão do arquivo para match>.
"""
import sys
from pipeline_tools.main.utils_tools import get_number_of_files, renames_all_files

sys.argv[0]='rename_files.py'

PATH_FILES = str(sys.argv[1]) #path directory
EXTESION_FILES = str(sys.argv[2]).lower()# set extension pdf or doc or others, without dot "."

if __name__ == '__main__' and get_number_of_files(PATH_FILES, EXTESION_FILES) > 0:
    renames_all_files(PATH_FILES, EXTESION_FILES)

