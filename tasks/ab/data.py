# STRINGS

def wordcount(s: str):
    """
    Функция принимает строку s и возвращает словарь, считающий количество
    вхождений каждого слова в нее
    (слова стоит рассматривать без учета регистра и без знаков препинания)
    """
    #words = re.findall(r'\b\w+\b', s)
    sl = s.split()
    d = dict()
    for i in sl:
        count = sl.count(i)
        d[i] = count

    return d
print(wordcount('one two and two ones'))
def caesar_encode(s: str, shift: int):
    """
    Функция принимает строку s и величину сдвига shift и возвращает результат
    применения шифра Цезаря к строке, со сдвигом на shift влево
    """
    n = shift


    word = s.split()
    def ceasar(s, n):
        deskryp = ""
        up = False
        for i in range(0, int(len(s))):
            if s[i].isupper():
                oldch = int(ord(s[i].lower()))
                up = True
            else:
                oldch = int(ord(s[i]))
            newch = (oldch - n)
            if ((newch) < 97):
                newch = 26 + (oldch - n)
            if (newch > 122):
                newch = -26 + (oldch - n)
            sim = chr(newch)
            if up:
                sim = sim.upper()
                up = False

            deskryp += sim
        return deskryp
    for i in range(len(word)):
        word[i] = ceasar(word[i], n)

    itog = ' '.join(word)

    return itog

# Упражнение на функции:
# определите дешифратор для шифра Цезаря, используя только вызов шифратора
caesar_decode = lambda s, shift: caesar_encode(s, -shift)


# LISTS

def extract_each(array: list, k: int, cyclic: bool = False):
    """
    Функция принимает массив array и число k, и возвращает массив, состоящий из
    каждого k-го элемента массива array
    (если передан cyclic=True, при достижении конца массива выбор элементов
    продолжается с начала, пока не достигнет уже выбранного элемента)
    """
    itog = []
    o = 0
    if cyclic == False:

        while o<len(array):
            itog.append(array[o])

            o+=k
    else:

        while len(itog)<len(array):
            if array[o] in itog:
                break
            itog.append(array[o])

            o+=k
            if o >= len(array):
                o = o -len(array)
    return itog

# SETS

def compare(s1: set[int], s2: set[int]):
    """
    Функция принимает два множества чисел и возвращает результат их сравнения -
    меньшим считается то множество, в котором лежит наименьший из их не-общих
    элементов
    """
    s1dif = s1.difference(s2)
    s2dif = s2.difference(s1)

    if len(s1dif) == 0 and len(s2dif) != 0:
        return True
    elif len(s2dif) == 0:
        return False
    else:
        return min(s1dif) < min(s2dif)


# DICTIONARIES

def merge(d1: dict, d2: dict, recursive: bool = False):
    """
    Функция принимает два json-словаря и возвращает результат их объединения
    (при наличии одинаковых ключей recursive=False означает, что надо оставить
    значение из d1, а recursive=True - что значения надо объединить рекурсивно)
    """
    itog = d1
    for i in d2:
        if i in itog.keys():
            if recursive and type(itog[i]) is dict and type(d2[i]) is dict:
                itog[i] = merge(itog[i], d2[i], recursive=True)
        else:
            itog[i] = d2[i]

    return itog


def translate_back(d: dict[str, list[str]]):
    """
    Функция принимает словарь, задающий возможные способы перевода слов с
    одного языка на другой, и возвращает словарь, описывающий перевод в
    обратном направлении
    """
    itog = {}

    for i in d:
        for j in d[i]:
            if j in itog.keys():
                itog[j].append(i)
            else:
                itog[j] = [i]
    return itog

