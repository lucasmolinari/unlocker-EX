from functions import *

for file in os.scandir('.'):
    if file.is_file():
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.xlsx' or file_extension == '.xlsm':

            copy_path = copy_xls(file, file_name.replace('.\\', ''), file_extension)
            print('COPY PATH: ' + copy_path)
            convert_file(copy_path, '.zip')
            extraction_paths = unzip_files(copy_path)

            # Loop through each extracted folder
            for path in extraction_paths:
                print('EXTRACTION PATH: ' + path)
                sheets_path = path + r'\xl\worksheets'
                # Loop through each file from the path 'sheets_path'
                for sheet in os.scandir(sheets_path):
                    convert_file(sheet, '.txt')
                for sheet in os.scandir(sheets_path):
                    remove_sheet_protection(sheet)
                    convert_file(sheet, '.xml')

                zipfolder(file_name, path, file_extension)
                print('EXTRACTION PATH: ' + path)


print('[DELETING EXTRA FOLDERS]')
shutil.rmtree('./_copies')
input("\n[PROCESS COMPLETED]")