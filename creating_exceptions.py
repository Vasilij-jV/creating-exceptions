# -*- config: utf8 -*-

class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


class NumbersLine(Exception):
    pass


class Cyrillic(Exception):
    pass


class Latin(Exception):
    pass


class CountElem(Exception):
    pass


class MoreThenOne(Exception):
    pass


class LessThanSix(Exception):
    pass


def throwingExceptions(flag, *args):
    elem = None
    first_list = []
    second_list = []
    third_list = []

    try:
        if not flag:
            raise ProcessingException('Invalid flag')
    except ProcessingException as exc:
        print(f'Процесс не может быть запущен, так как у параметра "flag" недопустимое значение {flag}. Ошибка: {exc}')
        raise

    try:
        for elem in args:
            if not isinstance(elem, str | int):
                raise InvalidDataException('Неверные данные')
            elif isinstance(elem, str) and not elem.isalpha():
                raise NumbersLine('Недопустимые символы в строке')
            elif isinstance(elem, str) and len(elem) < 2:
                raise CountElem('В строке меньше двух знаков')
            elif isinstance(elem, str) and ord(elem[0]) > 1039:
                flag = True
                for i in elem:
                    for count in range(ord('А'), ord('я') + 1):
                        if ord(i) == count:
                            flag = False
                            break
                        else:
                            flag = True
                    if flag:
                        raise Cyrillic('Кириллица содержит латиницу')
                first_list.append(elem)
            elif isinstance(elem, str) and ord(elem[0]) < 1040:
                flag = True
                for i in elem:
                    for count in range(ord('A'), ord('z') + 1):
                        if ord(i) == count:
                            flag = False
                            break
                        else:
                            flag = True
                    if flag:
                        raise Latin('Латиница содержит кириллицу')
                second_list.append(elem)
            elif isinstance(elem, int) and len(str(elem)) < 2:
                raise MoreThenOne('Слишком маленькое число')
            elif isinstance(elem, int) and len(str(elem)) > 5:
                raise LessThanSix('Слишком большое число')
            elif isinstance(elem, int):
                third_list.append(elem)
            elem = elem
    except InvalidDataException as exc:
        print(f'Элемент {elem} не может быть обработан. Ошибка: {exc}')
        raise
    except NumbersLine as exc:
        print(f'Строка {elem} не может содержать число. Ошибка: {exc}')
        raise
    except Cyrillic as exc:
        print(f'Строка {elem} может состоять только из знаков кириллицы. Ошибка: {exc}')
        raise
    except Latin as exc:
        print(f'Строка {elem} может состоять только из знаков латиницы. Ошибка: {exc}')
        raise
    except CountElem as exc:
        print(f'Строка {elem} должна содержать больше одного знака. Ошибка: {exc}')
        raise
    except MoreThenOne as exc:
        print(f'Число {elem} должно быть двузначным или больше. Ошибка: {exc}')
        raise
    except LessThanSix as exc:
        print(f'Число {elem} не должно быть больше чем пятизначное. Ошибка: {exc}')
        raise

    return first_list, second_list, third_list


list_list = throwingExceptions(True, 'фы', 54, 8578, 'ылдgвоа', 'ertyt', 'sd')
print(list_list)
