# unlocker-EX
Script to remove sheet protection from excel files
en-US:

-> Excel Workbooks Structure
- Uses Open Office XML File Format
- Changing .xls* extension to .zip, you can take a look in the structure of the workbook:
	- It's made of folders and XML files.
	- XML files are split in sections, similar to HTML:
	<workbook>placeholder</workbook>
	- One of the tags is the <sheetProtection> one, which contains the protection information of each
	sheet from the workbook.

-> Objetive
- Acess the workbook's XML files to remove <sheetProtection> from each sheet.

-> Script step by step:
- 1°. First we confirm if the file has one of the .xls* extensions.
- 2°. A copy of the file is created, this way the original workbook it's not affected.
- 3°. The copied file's extension is converted to zip, and we extract it to another folder
- 4°. The information of each sheet is in the path {worbook}/xl/worksheet, so we acess this folder.
- 5°. Each file .xml file is converted to .txt, to make edition possible.
- 6°. The way we search for the <sheetProtection> tag in each sheet file is:
	- Divide the sections (tags) with .split() function, and them we iterate in each one.
	- All the sections that don't have the value 'sheetProtection' are add to a new file, which will replace 
	the original.
- 7°. Now we just need to make the reverse:
	- Convert the files to .xml again
	- Compress the files in .zip format (Important to be exactly .zip)
	- Change the extension to be the same as the original file, .xlsx for example.

-----------------------------------------------------------------------------------------------------------------------------
pt-Br:


-> Estrutura dos Workbooks de Excel
- Usa Open Office XML File Format.
- Trocando a extensão do arquivo de .xls* para .zip, podemos 
observar:
	- Cada arquivo Excel é formado por vários diretórios contendo
	arquivos XML.
	- Os arquivos XML são divididos em tags, parecido com html:
	<workbook>placeholder</workbook>
	- Uma das tags é a <sheetProtection>, que armazena as informações
	de proteção de cada página do workbook.


-> Objetivo
- Acessar os arquivos XML do workbook e remover <sheetProtection> de todas as páginas.

-> Funcionamento do Script:

- 1°. Primeiro confirmamos se o arquivo que estamos trabalhando tem a extensão .xlsx ou .xlsm
- 2°. Criamos uma cópia do arquivo, caso algo aconteca o arquivo principal não será afetado.
- 3°. Convertemos o arquivo-cópia para .zip e extraímos para uma pasta separada.
- 4°. Acessamos o caminho {workbook}/xl/worksheets, que é onde os arquivos XML de cada página estão armazenados.
- 5°. Convertemos todos os arquivos .xml para .txt, para possibilitar a edição dos arquivos.
- 6°. Procuramos pela tag <sheetProtection> e a removemos da seguinte forma:
	- Dividimos as seções com a função .split(), e iteramos por cada seção.
	- Todas as seções que não tiverem o valor 'sheetProtection' são adicionadas a um novo arquivo, que substituirá
	o original.
- 7°. Agora é só fazer o caminho inverso:
	- Convertemos os arquivos novamente para .xml
	- Comprimimos os arquivos no formato .zip (Importante ser zip, e não .rar ou qualquer outra extensão)
	- Depois simplesmente mudadamos a extensão para ser igual ao arquivo original, .xlsx por exemplo.
