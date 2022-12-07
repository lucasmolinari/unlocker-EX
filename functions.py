import os
import shutil
from zipfile import ZipFile


# Copies the .xls* files to a new folder
def copy_xls(xls_path, index=0):
    _, tail = os.path.split(xls_path)
    xls_name, xls_extension = os.path.splitext(tail)
    print('\n[WORKING ON]\nName: %s \nExtension: %s' % (xls_name, xls_extension))
    os.makedirs('../_copies', exist_ok=True)
    print('[COPYING FILE]')
    copy_path = '../_copies/' + xls_name + '_copy' + str(index) + xls_extension
    print(copy_path)
    shutil.copyfile(xls_path, copy_path)
    print('[COPIED]')
    return copy_path


# Converts a file to another extension
def convert_file(file, extension):
    file_name, file_extension = os.path.splitext(file)
    print('[CONVERTING FILE %s TO %s]' % (file_name, extension))
    os.rename(file, file_name + extension)
    print('[DONE]')


# Unzip a file
def unzip_files(file):
    # creating a directory for each file
    zip_name, zip_extension = os.path.splitext(file)
    os.makedirs(zip_name)
    print('Folder created: ' + zip_name)
    print(zip_name, zip_extension)

    with ZipFile(zip_name + '.zip', 'r') as zip_file:
        print('[EXTRACTING]')
        zip_file.extractall(path=zip_name)
        print('[EXTRACTION COMPLETE]\n')

        extract_paths = zip_name
    return extract_paths


# Removes the tag <sheetProtection>
def remove_sheet_protection(sheet):
    print('[REMOVING EXISTING PROTECTIONS]')
    if sheet.is_file():
        sections = []
        unprotected_sections = []
        with open(sheet.path, encoding='utf-8') as fin:
            for line in fin:
                sections.append(line.split('>'))

        for p in sections:
            for section in p:
                section += '>'
                if 'sheetProtection' not in section and section != '>':
                    unprotected_sections.append(section)

        fin.close()

        # Removes extra sections that can corrupt the file
        if '\n>' in unprotected_sections:
            unprotected_sections.remove('\n>')
        if '>' in unprotected_sections:
            unprotected_sections.remove('>')
        print(unprotected_sections)

        # Writes a new file to replace the original
        with open(sheet.path, 'w+', encoding='utf-8') as fout:
            for section in unprotected_sections:
                fout.write(section)
        fout.close()


# Zips the files and converts to .xls* again
def zipfolder(folder_name, target_dir, extension):
    zipobj = ZipFile(folder_name + '_unlocked' + extension, 'w')
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])


# Tries to remove the ../copies folder
def delete_copies():
    try:
        shutil.rmtree('../_copies')
    except Exception as e:
        print(e)
