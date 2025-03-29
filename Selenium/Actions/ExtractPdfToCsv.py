import csv

from exceptiongroup import catch

from Selenium.Enums.DirectoryEnum import DirectoryEnum
from Selenium.Interfaces.ExecuteScrapping import ExecuteScrapping
import os
import tabula


class ExtractPdfToCsv(ExecuteScrapping):

    def execute(self):
        for archive_name in os.listdir(DirectoryEnum.PDF.value):
            if archive_name.startswith('Anexo_I_'):
                path = os.path.join(DirectoryEnum.PDF.value, archive_name)
                if os.path.exists(path):
                    self.extractTable(path)
        pass

    def extractTable(self, path):
        path_anexo = os.path.join(DirectoryEnum.CSV.value, "Anexo_I.csv")
        print("Convertendo Anexo I para CSV...")
        tabula.convert_into(
            path,
            path_anexo,
            output_format="csv",
            pages="all"
        )
        self.cleanCsv(path_anexo)

    def cleanCsv(self,path):
        print("Limpando  Anexo_I.csv")
        lines = []
        with open(path,'r') as csvfile:
          for row in csv.reader(csvfile):
              if row:
                if not row[0].startswith("RN no"):
                    if row[3] == "OD": row[3] = str.upper("Seg. Odontológica")
                    if row[4] == "AMB": row[4] = str.upper("Seg. Ambulatorial")
                    lines.append(row)

        with open(path, 'w', newline='', encoding='utf-8') as newcsvfile:
            writer = csv.writer(newcsvfile)
            writer.writerows(lines)
