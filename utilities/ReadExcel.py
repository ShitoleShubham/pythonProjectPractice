import openpyxl

class Readexcel:
    path=r'C:\Users\Mr.PerSeCuToR\PycharmProjects\pythonProjectPractice\testdata\testURL.xlsx'
    sheetname='Sheet1'

    @staticmethod
    def geturl(rows,columns,file=path,sheetname=sheetname):
        workbook=openpyxl.load_workbook(file)
        sheet=workbook[sheetname]
        return sheet.cell(rows,columns).value




