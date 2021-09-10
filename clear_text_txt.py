import sys
from utils_tools import clear_text_file_non_ut8

sys.argv[0]='clear_text_txt.py'

PATH_FILES = str(sys.argv[1]) #path directory list files 
PATH_SAVE = str(sys.argv[2]) #path directory save files 
EXTESION_FILES = 'txt'

clear_text_file_non_ut8(PATH_FILES, PATH_SAVE, EXTESION_FILES)