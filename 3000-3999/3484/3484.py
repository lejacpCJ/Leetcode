from collections import defaultdict
import string

class Spreadsheet:

    def __init__(self, rows: int):
        # 26 columns 'A'..'Z', each column is a list of length rows initialized to 0
        self.sheet = defaultdict(list)
        for ch in string.ascii_uppercase:
            self.sheet[ch] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:]) - 1
        self.sheet[col][row] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:]) - 1
        self.sheet[col][row] = 0

    def getValue(self, formula: str) -> int:
        # formula format: "=X+Y"
        parts = formula[1:].partition('+')
        left, right = parts[0], parts[2]

        def getCellValue(token: str) -> int:
            if token.isnumeric():
                return int(token)
            col = token[0]
            row = int(token[1:]) - 1
            return self.sheet[col][row]

        return getCellValue(left) + getCellValue(right)