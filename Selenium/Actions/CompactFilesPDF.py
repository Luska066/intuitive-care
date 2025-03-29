import os
import zipfile

from Selenium.Enums.DirectoryEnum import DirectoryEnum
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping

class CompactFilesPDF(ExecuteScrapping):
    file_name = DirectoryEnum.ZIP.value+'/Teste_lucas.zip'
    def execute(self):
        print("Compactando Arquivos...")
        with zipfile.ZipFile(self.file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(DirectoryEnum.PDF.value):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.basename(file_path))
        print("Arquivos compactados com sucesso!")