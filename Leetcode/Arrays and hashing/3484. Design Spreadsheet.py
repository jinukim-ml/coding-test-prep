from collections import defaultdict

class Spreadsheet:
    def __init__(self, rows: int):
        self.sheet = defaultdict(int)
    
    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula.split('+')
        a, b = formula[0][1:], formula[1]
        if a.isdecimal():
            a = int(a)
        else:
            a = self.sheet[a]
        if b.isdecimal():
            b = int(b)
        else:
            b = self.sheet[b]
        return a+b