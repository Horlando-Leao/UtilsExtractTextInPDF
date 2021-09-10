import sys
from utils_tools import make_database_for_prodigy

sys.argv[0]='make_txt_for_jsonl.py'

path_list_txt = str(sys.argv[1]) #find path directory with files txt
path_save_json = str(sys.argv[2]) #path e name files for save file jsonl 
print('path find:', path_list_txt,'\njsonl save:', path_save_json)

extension_find_path = 'txt'

if __name__ == '__main__':
    make_database_for_prodigy(path_list_txt, path_save_json, extension_find_path)
