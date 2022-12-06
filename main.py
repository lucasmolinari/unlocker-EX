import sys
from functions import *
from gui.pythongui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class UnlockerEX(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.buttonChooseFile.clicked.connect(self.open_file)
        self.buttonUnlock.clicked.connect(self.unlock)
        self.buttonSave.clicked.connect(self.save)
        self.file_name = None
        self.extraction_path = None
        self.file_extension = None
        # index used in the creation of folders. preventing the names to be equal.
        self.index = 0

    def open_file(self):
        try:
            file, _ = QFileDialog.getOpenFileName(
                self.centralwidget,
                'Open File',
                '../',
                '(*.xlsx *.xlsm)'
            )
            self.inputOpenFile.setText(file)
            self.file_name, self.file_extension = os.path.splitext(file)
            self.process_text = '[WORKING ON]\nName: %s \nExtension: %s\n' % (self.file_name, self.file_extension)
            self.labelProcess.setText(self.process_text + '\n[PRESS UNLOCK]')
        except Exception as e:
            print(e)

    def unlock(self):
        file = self.inputOpenFile.text()
        if self.inputOpenFile.text():
            try:
                self.labelProcess.setText(self.process_text)

                # copying the original file to a work folder

                copy_path = copy_xls(file, index=self.index)
                self.process_text += 'COPY PATH: ' + copy_path
                self.labelProcess.setText(self.process_text)

                # converting the copy to .zip and then extracting it

                convert_file(copy_path, '.zip')
                self.extraction_path = unzip_files(copy_path)

                sheets_path = self.extraction_path + r'\xl\worksheets'

                # changing the extension from each sheet to make it editable

                for sheet in os.scandir(sheets_path):
                    if sheet.is_file():
                        convert_file(sheet, '.txt')

                # removing <sheetProtection> and converting back to .xml

                for sheet in os.scandir(sheets_path):
                    if sheet.is_file():
                        remove_sheet_protection(sheet)
                        convert_file(sheet, '.xml')

                self.index += 1
                self.process_text += '\n[PROCESS FINISHED][PRESS SAVE]'
                self.labelProcess.setText(self.process_text)
            except Exception as e:
                print(e)
                self.labelProcess.setText(e)

    def save(self):
        try:
            # get the directory where the user wants to save the file
            if self.inputOpenFile.text():
                path = QFileDialog.getExistingDirectory(
                    self.centralwidget,
                    'Save File',
                    '../'
                )
                head, tail = os.path.split(self.file_name)
                # zips the Excel files back where user wants to save it.
                print(path, tail)
                zipfolder(path + '/' + tail, self.extraction_path, self.file_extension)
                self.labelProcess.setText('[SAVED]')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    delete_copies()
    qt = QApplication(sys.argv)
    unlocker = UnlockerEX()
    unlocker.show()
    qt.exec_()

