import os
import shutil
from zipfile import ZipFile


# Looks for xls files in the script folder
def check_xls():
    print('[LOOKING FOR XLS FILE]')
    xls_files = []
    for file in os.scandir('.'):
        if file.path[-4:] == 'xlsx' or file.path[-4:] == 'xlsm' and file.is_file():
            xls_files.append(file)
    if not xls_files:
        print('No .xlsx file found.')
        shutil.rmtree('./_copies')
        input()
        quit()
    else:
        print('.xlsx/.xlsm found: %s' % xls_files)
        return xls_files


def copy_xls(xls, xls_name, xls_extension):
    print('\n[WORKING ON]\nName: %s \nExtension: %s' % (xls_name, xls_extension))
    os.makedirs('./_copies', exist_ok=True)
    print('[COPYING FILE]')
    copy_path = '_copies\\' + xls_name + '_copy' + xls_extension
    shutil.copyfile(xls.path, copy_path)
    print('[COPIED]')
    return copy_path


def convert_file(file, extension):
    file_name, file_extension = os.path.splitext(file)
    print('[CONVERTING FILE %s TO %s]' % (file_name, extension))
    os.rename(file, file_name + extension)
    print('[DONE]')


def unzip_files(file):
    extract_paths = []

    # creating a directory for each file
    zip_name, zip_extension = os.path.splitext(file)
    os.makedirs(zip_name)
    print('Folder created: ' + zip_name)
    print(zip_name, zip_extension)

    with ZipFile(zip_name + '.zip', 'r') as zip:
        print('[EXTRACTING]')
        zip.extractall(path=zip_name)
        print('[EXTRACTION COMPLETE]\n')

        extract_paths.append(zip_name)
    return extract_paths


def remove_sheet_protection(sheet):
    print('[REMOVING EXISTING PROTECTIONS]')
    if sheet.is_file():
        sections = []
        unprotected_sections = []
        with open(sheet.path) as fin:
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

        with open(sheet.path, 'w+') as fout:
            for section in unprotected_sections:
                fout.write(section)
        fout.close()


def zipfolder(foldername, target_dir, extension):
    zipobj = ZipFile(foldername + '_unlocked' + extension, 'w')
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
