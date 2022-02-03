def rule():
    print("                Игра: крестики-нолики")
    print("Правила игры: Игроки по очереди ставят на свободные клетки поля 3×3 знаки")
    print(" (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3")
    print(" своих фигуры по вертикали, горизонтали или диагонали, выигрывает.")
    print("Первый ход делает игрок, ставящий крестики.")
    print(" ")
    print("Ввод координат производится в два этапа, сперва вводится координата строки,")
    print(" далее координата столбца.")
    print(" ")

def show():
    print(f"   | 0 | 1 | 2")
    for i in range(3):
        print(f" {i} | {field[i][0]} | {field[i][1]} | {field[i][2]}")

def turn():
    while True:
        x = input("строка (введите число от о до 2) - ")
        y = input("столбец (введите число от 0 до 2) - ")

        if not(x.isdigit()) or not(y.isdigit()):
            print("введите число")
            continue

        x = int(x)
        y = int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == " ":
                return x, y
            else:
                print("клетка занята")
        else:
            print("вне диапазона")

def win_condition():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (1, 1), (2,2)), ((2, 0), (1, 1), (0, 2)))
    for combination in win_comb:
        symbols = []
        for a in combination:
            symbols.append(field[a[0]][a[1]])
        if symbols == ["x", "x", "x"]:
            print("Победил x!")
            return True
        if symbols == ["o", "o", "o"]:
            print("Победил о!")
            return True
    return False


rule()

field = [[" "]*3 for i in range(3)]
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("ходит первый игрок (x)")
    else:
        print("ходит второй игрок (o)")

    x, y = turn()
    if num%2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "o"

    if win_condition():
        break

    if num == 9:
        print("Ничья")
        break

