import sys
from gui.pythongui import *
from functions import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class UnlockerEX(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.unlocked = False
        self.buttonChooseFile.clicked.connect(self.open_file)
        self.buttonUnlock.clicked.connect(self.unlock)
        self.buttonSave.clicked.connect(self.save)
        self.process_text = None
        self.file_name = None
        self.extraction_path = None
        self.file_extension = None
        self.previous_file = None
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
            if file:
                self.process_text = '[WORKING ON]\nName: %s \nExtension: %s\n' % (self.file_name, self.file_extension)
                self.labelProcess.setText(self.process_text + '\n[PRESS UNLOCK]')
        except Exception as e:
            print(e)

    def unlock(self):
        file = self.inputOpenFile.text()
        if self.inputOpenFile.text() and file != self.previous_file:
            self.process_text = '[STARTING UNLOCK PROCESS]'
            self.labelProcess.setText(self.process_text)
            self.progressBar.setValue(3)

            # copying the original file to a work folder
            self.process_text += '\n[CREATING COPY]'
            self.labelProcess.setText(self.process_text)
            copy_path = copy_xls(file, index=self.index)
            self.progressBar.setValue(10)
            self.process_text += ' COPY PATH: %s' % copy_path
            self.labelProcess.setText(self.process_text)

            # converting the copy to .zip and then extracting it
            self.process_text += '\n[CONVERTING FILE]'
            self.labelProcess.setText(self.process_text)
            convert_file(copy_path, '.zip')
            self.progressBar.setValue(25)
            self.process_text += '\n[EXTRACTING FILE]'
            self.labelProcess.setText(self.process_text)
            self.extraction_path = unzip_files(copy_path)
            self.progressBar.setValue(45)
            self.process_text += ' EXTRACTION PATH: %s' % self.extraction_path

            # changing the extension from each sheet to make it editable
            self.process_text += '\n[ACCESSING SHEETS]'
            sheets_path = self.extraction_path + r'\xl\worksheets'
            for sheet in os.scandir(sheets_path):
                if sheet.is_file():
                    convert_file(sheet, '.txt')
            self.progressBar.setValue(75)
            # removing <sheetProtection> and converting back to .xml
            self.process_text += '\n[REMOVING PROTECTION]'
            self.labelProcess.setText(self.process_text)
            for sheet in os.scandir(sheets_path):
                if sheet.is_file():
                    remove_sheet_protection(sheet)
                    convert_file(sheet, '.xml')
            self.progressBar.setValue(100)
            self.index += 1
            self.process_text += '\n[PROCESS FINISHED]\n[PRESS SAVE]'
            self.labelProcess.setText(self.process_text)
            self.unlocked = True
            self.previous_file = file

    def save(self):
        try:
            # get the directory where the user wants to save the file
            if self.unlocked:
                head, tail = os.path.split(self.file_name)
                path = QFileDialog.getExistingDirectory(
                    self.centralwidget,
                    'Save File',
                    head
                )
                # zips the Excel files back where user wants to save it.
                print('\nPATH: %s TAIL: %s' % (head, tail))
                zipfolder(path + '/' + tail, self.extraction_path, self.file_extension)
                delete_copies()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    delete_copies()
    qt = QApplication(sys.argv)
    unlocker = UnlockerEX()
    unlocker.show()
    qt.exec_()
