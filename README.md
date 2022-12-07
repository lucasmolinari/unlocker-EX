# unlocker-EX
Script to remove sheet protection from excel files

- en-US:

- How to use:
  - You can just download the EXE file and you will not need to install any additional packages.
  - If you face any problem with the EXE file, you can:
  	- Download all the files, including subfolders
	- Install PyQT5, open a terminal and type "pip install pyqt5"
  	- Run 'main.pyw'


- Excel Workbooks Structure
  - Uses Open Office XML File Format
  - Changing .xls* extension to .zip, you can take a look in the structure of the workbook:
	  - It's made of folders and XML files.
	  - XML files are split in sections, similar to HTML
	  - One of the tags is the sheetProtection one, which contains the protection information of each sheet from the workbook.


------------------------------------------------------------- 

- pt-Br:

- Como usar:
  - Você pode simplesente baixar o arquivo EXE, sem precisar instalar nenhum pacote adicional.
  - Caso encontre algum problema com o EXE, faça o seguinte:
  	- Faça download de todos os arquivos, incluindo as subpastas.
	- Instale PyQT5 abrindo um terminal e executando o comando "pip install pyqt5"
  	- Execute main.pyw
  

- Estrutura dos Workbooks de Excel
  - Usa Open Office XML File Format.
  - Trocando a extensão do arquivo de .xls* para .zip, podemos 
  observar:
    - Cada arquivo Excel é formado por vários diretórios contendo arquivos XML.
    - Os arquivos XML são divididos em tags, parecido com html
    - Uma das tags é a sheetProtection, que armazena as informações de proteção de cada página do workbook.
