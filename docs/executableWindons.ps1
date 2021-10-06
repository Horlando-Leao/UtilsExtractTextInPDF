#python ..\__main__.py 
#    <Diretorio de arquivos pdf> 
#    <Diretorio de arquivos txt> 
#    <Diretorio para salvar os arquivos txt pre processados>
#    <Diretorio para salvar arquivos jsonl/nome do arquivo>



python __main__.py folder_test folder_test folder_test/folder_test database.jsonl
python .\cli\make_txt_for_jsonl.py ..\folder_test\folder_test\ ..\folder_test\database.jsonl
python .\cli\clear_text_txt.py ..\folder_test ..\folder_test\folder_test
