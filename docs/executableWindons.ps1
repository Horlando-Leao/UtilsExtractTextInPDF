#python ..\__main__.py 
#    <Diretorio de arquivos pdf> 
#    <Diretorio de arquivos txt> 
#    <Diretorio para salvar os arquivos txt pre processados>
#    <Diretorio para salvar arquivos jsonl/nome do arquivo>



python __main__.py cvs_database cvs_database cvs_database/cv_clean cvs_database/cv_clean/database.jsonl
python .\cli\make_txt_for_jsonl.py ..\cv_aundes_txt\cv_clean\ ..\cv_aundes_txt\database.jsonl
python .\cli\clear_text_txt.py ..\cv_aundes_txt ..\cv_aundes_txt\cv_clean