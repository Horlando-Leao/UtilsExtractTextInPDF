import sys
from cli.main.utils_tools import renames_all_files, extractPDF_text, clear_text_file_non_ut8
from cli.main.utils_tools import make_database_for_prodigy, get_number_of_files

sys.argv[0] = '__main__.py'
PATH_FILES_FIND_PDF = None
PATH_FILES_TXT      = None
PATH_SAVE_TXT_CLEAN = None
PATH_SAVE_JSONL     = None

try:
    PATH_FILES_FIND_PDF = str(sys.argv[1]) # path directory
except IndexError:
    PATH_FILES_FIND_PDF = input(str("Diretorio de arquivos de pdf para extrair e mudar o nome: "))

try:
    PATH_FILES_TXT      = str(sys.argv[2]) # Path find txt for clean garbage
except IndexError:
    PATH_FILES_TXT = input(str("Diretorio de arquivos de txt sujos: "))

try:
    PATH_SAVE_TXT_CLEAN = str(sys.argv[3]) # path for save new txt clean
except IndexError:
    PATH_SAVE_TXT_CLEAN = input(str("Diretorio para salvar arquivos os txt limpos: "))

try:
    PATH_SAVE_JSONL     = str(sys.argv[4]) # path save for new txt
except IndexError:
    PATH_SAVE_JSONL = input(str("Diretorio para salvar arquivo jsonl: "))


if __name__ == '__main__' and get_number_of_files(PATH_FILES_FIND_PDF, 'pdf') > 0:

    renames_all_files(PATH_FILES_FIND_PDF, 'pdf')
    
    extractPDF_text(PATH_FILES_FIND_PDF)

    clear_text_file_non_ut8(PATH_FILES_TXT, PATH_SAVE_TXT_CLEAN, 'txt')

    make_database_for_prodigy(PATH_SAVE_TXT_CLEAN, PATH_SAVE_JSONL, 'txt')

    print("Done!")