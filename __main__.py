import sys
from main.utils_tools import renames_all_files, extractPDF_text, clear_text_file_non_ut8
from main.utils_tools import make_database_for_prodigy, get_number_of_files

sys.argv[0] = '__main__.py'

PATH_FILES_FIND_PDF = str(sys.argv[1]) # path directory
PATH_FILES_TXT      = str(sys.argv[2]) # Path find txt for clean garbage
PATH_SAVE_TXT_CLEAN = str(sys.argv[3]) # path for save new txt clean
PATH_SAVE_JSONL     = str(sys.argv[4]) # path save for new txt


if __name__ == '__main__' and get_number_of_files(PATH_FILES_FIND_PDF, 'pdf') > 0:

    renames_all_files(PATH_FILES_FIND_PDF, 'pdf')
    
    extractPDF_text(PATH_FILES_FIND_PDF)

    clear_text_file_non_ut8(PATH_FILES_TXT, PATH_SAVE_TXT_CLEAN, 'txt')

    make_database_for_prodigy(PATH_SAVE_TXT_CLEAN, PATH_SAVE_JSONL, 'txt')

    print("Done!")