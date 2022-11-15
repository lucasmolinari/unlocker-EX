# unlocker-EX
Script to remove sheet protection from excel files

- en-US:
- How to use:
  - Download main.py and functions.py
  - Create a folder containg the .py files and the Excel Workbooks you want to unlock.
  - Run main.py
  - The original workbooks won't be changed, a unlocked copy will be available in the same folder when the process is finished.



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
  - Faça download dos arquivos main.py e functions.py
  - Crie um diretório contendo ambos .py e os arquivos excel que deseja desbloquear.
  - Execute main.py
  - Os arquivos originais não serão afetados, uma cópia dos Workbooks estarão disponíveis no mesmo diretório.
  

- Estrutura dos Workbooks de Excel
  - Usa Open Office XML File Format.
  - Trocando a extensão do arquivo de .xls* para .zip, podemos 
  observar:
    - Cada arquivo Excel é formado por vários diretórios contendo
	arquivos XML.
	  - Os arquivos XML são divididos em tags, parecido com html
	  - Uma das tags é a sheetProtection, que armazena as informações
	de proteção de cada página do workbook.
