
from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str

@dataclass
class MoveOfMainAssets:
    name: str
    code: int
    remainder: float
    received: float
    output: float
    year: float

type_array = []
type_array.append(TypeOfMainAssets(103, "англійський фунт стерлінгів"))
type_array.append(TypeOfMainAssets(104, "бельгійський франк"))
type_array.append(TypeOfMainAssets(105, "німецька марка"))
type_array.append(TypeOfMainAssets(106, "голандський гульден"))
type_array.append(TypeOfMainAssets(109, "канандський долар"))
type_array.append(TypeOfMainAssets(111, "долар США"))

move_array = []
move_array.append(MoveOfMainAssets("англійський фунт стерлінгів", 103, 5.65, 6.05, 10.03, 2003))
move_array.append(MoveOfMainAssets("бельгійський франк", 104, 1.13, 1.23, 2.00, 2003))
move_array.append(MoveOfMainAssets("німецька марка", 105, 2.28, 2.52, 4.12, 2003))
move_array.append(MoveOfMainAssets("голандський гульден", 106, 2.02, 2.24, 3.66, 2003))
move_array.append(MoveOfMainAssets("канадський долар", 109, 2.68, 3.18, 5.12, 2003))
move_array.append(MoveOfMainAssets("долар США", 111, 3.34, 3.96, 6.53, 2003))
move_array.append(MoveOfMainAssets("англійський фунт стерлінгів", 103, 1.10, 11.21, 13.50, 2004))
move_array.append(MoveOfMainAssets("бельгійський франк", 104, 2.50, 2.60, 2.75, 2004))
move_array.append(MoveOfMainAssets("німецька марка", 105, 4.44, 4.65, 4.70, 2004))
move_array.append(MoveOfMainAssets("голандський гульден", 106, 4.05, 4.25, 4.50, 2004))
move_array.append(MoveOfMainAssets("канадський долар", 109, 6.05, 6.30, 6.80, 2004))
move_array.append(MoveOfMainAssets("долар США", 111, 7.00, 7.25, 7.50, 2004))
move_array.append(MoveOfMainAssets("англійський фунт стерлінгів", 103, 13.64, 13.70, 13.80, 2005))
move_array.append(MoveOfMainAssets("бельгійський франк", 104, 2.80, 2.83, 2.85, 2005))
move_array.append(MoveOfMainAssets("німецька марка", 105, 4.75, 4.80, 4.85, 2005))
move_array.append(MoveOfMainAssets("голандський гульден", 106, 4.62, 4.64, 4.66, 2005))
move_array.append(MoveOfMainAssets("канадський долар", 109, 6.90, 6.95, 7.00, 2005))
move_array.append(MoveOfMainAssets("долар США", 111, 7.65, 7.75, 7.85, 2005))


def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Валюти"
    with names and values'''

    print("Валюта: {name}, Код валюти: {code}, Курс грн. на 1.10: {remainder}, Курс грн. на 1.11: {received} Курс грн. на 1.12: {output}, Рік {year}"
          .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                  received=moveOfMainAssets.received, output=moveOfMainAssets.output, year=moveOfMainAssets.year)) 
for data in move_array:
    printMoveOfMainAssets(data)



