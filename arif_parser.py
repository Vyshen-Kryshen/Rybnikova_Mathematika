from string import ascii_letters
from schyot import *
from numrat import *
operators: list[str] = ["вычесть_из", "сложить", "суммировать", "умножить", "степень"]
logic_separators: list[str] = ["и", "ещё", "также"]
unnecessary_separators: list[str] = [".", ",", ":", ";", "-", ">", "<"]


def parsing(file_path: str) -> None:
    """
    Функция парсинга математических выражений с файлов формата '.rm'.
    """
    text: str = ""
    uses_operators: list[str] = []
    pre_eval_code: list[list[str]] = []
    eval_code: str = ""
    if ".rm" in file_path[len(file_path) - 3: len(file_path)]:
        with open(file_path, "r+", encoding="UTF-8") as f:
            text = f.read()
        string: list[str] = text.split("\n")
        rows: list[str] = []

        def separation() -> None:
            """
            Подфункция разделения кода на строки, а в свою очередь строки уже на элементы, и дальнйший их синтаксический анализ.
            """
            for substring in string:
                rows.append(substring.split())
            for row in rows:
                for elem in row:
                    for letter in ascii_letters:
                        if letter in elem:
                            raise SyntaxError("Англосаксонский алфавит неподдерживается.")
                    for separator in unnecessary_separators:
                        if separator in elem:
                            raise SyntaxError("Вызвано исключение в связи с использованием ненужного сепаратора.")
                        else:
                            uses_operators.append(elem)
                    if row[0] not in operators:
                        raise SyntaxError("Почему у тебя в начале строки нет вызова ключевой операции?")
                    if len(row) > 1:
                        if row[1] in operators:
                            raise SyntaxError("")
                else:
                    pre_eval_code.append(row)
            else:
                pass
        
        def translanguager() -> None:
            """
            Подфункция переводчика RM-выражений в Python-код. Сначала цикл проходится по рядам преэвалюированного кода,
            после чего проходить поэлементо по каждому из рядов, затем проверяет, является ли элемент числом или оператором.
            Ежи тот оператор, то далее он пытается идентифицировать его, добавляю узнанное им значение в переменную 'eval_code'.
            После окончания цикла, я реализую костыль ввиде среза строки и добавки символ ')' в конец строки.
            Затем идём алгоритм сортированное заполнения матрицы 'nums_arrays'. 
            """
            global operators
            nonlocal eval_code
            nums: list[list[int, int]] = []
            for row in pre_eval_code:
                for elem in row:
                    if elem in operators:
                        if elem == operators[0]:
                            if row[row.index(elem) - 1].isdigit:
                                eval_code += ")"
                                eval_code += " deduction("
                            else:
                                eval_code += " deduction("
                        elif elem == operators[1]:
                            if row[row.index(elem) - 1].isdigit:
                                eval_code += ")"
                                eval_code += " livewithlies("
                            else:
                                eval_code += " livewithlies("
                        elif elem == operators[2]:
                            if row[row.index(elem) - 1].isdigit:
                                eval_code += ")"
                                eval_code += " summation("
                            else:
                                eval_code += " summation("
                        elif elem == operators[3]:
                            if row[row.index(elem) - 1].isdigit:
                                eval_code += ")"
                                eval_code += " smartlife("
                            else:
                                eval_code += " smartlife("
                        elif elem == operators[4]:
                            if row[row.index(elem) - 1].isdigit:
                                eval_code += ")"
                                eval_code += " smartlife("
                            else:
                                eval_code += " smartlife("
                    elif elem.isdigit():
                        eval_code += elem
                        nums.append([elem, pre_eval_code.index(row)])
            else:
                if ")" == eval_code[0]:
                    eval_code += ")"
                    eval_code = eval_code[2:]
                nums_arrays: list[list[int]] = []
                conc_array: list[list[int]] = []
                for i in range(0, len(pre_eval_code)):
                    nums_arrays.append([])
                for i in range(0, len(nums_arrays)):
                    conc_array.append([])
                for elem in nums:
                    nums_arrays[elem[1]].append(elem[0])
                for elem in nums_arrays:
                    for char in elem:
                        conc_array[nums_arrays.index(elem)].append(int(char))
                for elem in eval_code.split(" "):
                    number: str = ""
                    for char in elem:
                        if char.isdigit():
                            number += char
                    new_eval_code = eval_code.replace(number, str(conc_array[eval_code.split(" ").index(elem)])[1:-1].replace(" ", ""))
                    for elem in new_eval_code.split(" "):
                        if "," in elem:
                            print(eval(elem))
        separation()
        translanguager()
    else:
        raise ValueError(f"Поддерживаются файлы только '.rm' формата, а не: {file_path[-2:0]}")


if __name__ == "__main__":
    parsing('test.rm')
