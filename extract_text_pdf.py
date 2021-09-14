import sys
from pipeline_tools.utils_tools import extract_text_on_pdf

sys.argv[0] = 'extract_text_pdf.py'
PATH_FILES = str(sys.argv[1])  # path directory with list of files

if __name__ == '__main__':
    extract_text_on_pdf(PATH_FILES)
    print("Done!")
