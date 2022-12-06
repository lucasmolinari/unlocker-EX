# unlocker-EX
Script to remove sheet protection from excel files

- en-US:
- How to use:
  - Download all the files, including subfolders
  - Run 'main.py'
  - Select the workbook and press 'unlock'
  - The original workbooks won't be changed, in the end of the process you can choose where the unlocked workbook can be saved.



- Excel Workbooks Structure
  - Uses Open Office XML File Format
  - Changing .xls* extension to .zip, you can take a look in the structure of the workbook:
	  - It's made of folders and XML files.
	  - XML files are split in sections, similar to HTML
	  - One of the tags is the sheetProtection one, which contains the protection information of each
	sheet from the workbook.


------------------------------------------------------------- 

- pt-Br:

- Como usar:
  - Faça download de todos os arquivos, incluindo as subpastas.
  - Execute main.py
  - Selecione a planilha e clique em 'unlock'.
  - Os arquivos originais não serão afetados, no final do processo você pode escolher onde salvar a planilha desbloqueada.
  

- Estrutura dos Workbooks de Excel
  - Usa Open Office XML File Format.
  - Trocando a extensão do arquivo de .xls* para .zip, podemos 
  observar:
    - Cada arquivo Excel é formado por vários diretórios contendo
	arquivos XML.
	  - Os arquivos XML são divididos em tags, parecido com html
	  - Uma das tags é a sheetProtection, que armazena as informações
	de proteção de cada página do workbook.
