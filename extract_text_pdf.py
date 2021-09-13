import sys
from pipeline_tools.main.utils_tools import extractPDF_text

sys.argv[0]='extract_text_pdf.py'
PATH_FILES = str(sys.argv[1]) #path directory with list of files

if __name__ == '__main__':
    extractPDF_text(PATH_FILES)
