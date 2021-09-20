# PROBLEM 0
#
# Из множества
#
# № 1 - удалите все числа 6.

# Множество № 1:
#
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.remove(6)
# print(dates_of_birth)

# PROBLEM 1
#
# Создайте SET состоящий из 3 вложенных SET.

#a = {1, 3, 5}
#b = {2, 6, 8}
#c = {4, 5, 7}

#fs = set()
#fs.update(a, b, c)
#print(fs)

#PROBLEM 2
#Во множестве №3 найдите объекты которых нет во множестве №2

#Множество № 3:
#
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
#
# #Множество № 2:
#
# farm_1 = {"dear", "cat", "mouse", "sheep"}
#
# farm_2 = farm_1
# a = farm_2
# a.difference()
# print(a)
#
#
# farm_1 = farm_2
# b = farm_1
# b.difference()
# print(b)

# PROBLEM 3
#
# Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
#
# А затем удалите через .pop() элемент и посмотрите что же вы удалили.

# t = {"esen", "azamat", 500, 123, 999}
# ds = {"azamatovaese"}
# ds.update(t)
# ds.pop()
# print(ds)

# PROBLEM 10:
# Из Dictionary №1:
# Добавьте в меню
# напитки как ключ "drinks",
# А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.

# Словарь №1:

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# x = menu.get("drinks")
# menu["drinks"] = {"Coca-Cola", "Sprite", "Fanta"}
# print(menu)

# PROBLEM 020:
# Создайте SET который хранит в себе все методы  для работы  с  SET.
#
# Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали.
#
# Проверьте какие методы похожи у этих типов данные.

# sets1 = {".add()", ".remove()", ".clear", ".update()", ".difference()", ".discard()", ".difference()" ".intersection()"}
# sets2 = {".clear()", ".keys()", ".item()", ".get()", ".values()", ".update()", "tuple()", "list()", "set()", "dict()"}
# print(sets1.difference(sets2))
# print(sets2.difference(sets1))

# PROBLEM 31:
# Создайте пустой словарь.
# Запустите цикл который 3 раза спросит его имя и его пароль.
# Записывайте имя пользователя как ключ, а пароль как его значение.

# u = dict()
# for i in range(3):
#     l = input("your name")
#     p = input("pasword")
#     u.update({l: p})
# print(u)


# PROBLEM 27:
# Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
# С помощь цикла for пройти вывести на экран строку:
#
# "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"
#
# profession = {'esen': 'Aitisnik', 'artur': 'artist', 'putin': 'deputat', 'arsen': 'president'}
# for key, values in profession.items():
#     print(f"Здравствуйте, {key}  Прекрасная профессия {values}")

# PROBLEM 22:
#
# Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
# Сделайте так чтобы эти данные уже никто не смог поменять позже.

# q = set()
# for i in range(10):
#     b = int(input('your number'))
#     q.add(b)
# print(q)

# PROBLEM 99:
#
# Из Dictionary №1:
#
# Добавьте в меню
#
#  'besh_barmak' который стоит  130 сом.
#
# Оказалось лагман слишком дешевый. Обновите цену на 135
#
# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
#
# Удалить borsh
#
# cafesmenu = {'lagman': 120, 'plov': 120, "borsh": 100}
# cafesmenu.update(besh_barmak = 130)
# print(cafesmenu)
# print("лагман слишком дешевый")
# cafesmenu.update(lagman = 130)
# print(cafesmenu)
# print("Ваш повар отвратительно готовит удалите борщ")
# cafesmenu.pop('borsh', 100)
# print(cafesmenu)

# PROBLEM 11:
#
# Есть список Южноамериканских стран
# СПИСОК №2
# в котором Суринам встречается два раза. Необходимо написать программу,
# которая удалит дублирующуюся запись, и возвратит в результате список.

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Surinam', 'Surinam', 'Uruguay', 'Venezuela']
# r = set(south_american_countries)
# print(list(r))

# PROBLEM 101:
#
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст:
# suitcase = []
# Однако он
# может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.
# Вы передумали, и решили убрать последнюю вещь.


# suitcase = []
# suitcase.append("штаны")
# suitcase.append("носки")
# suitcase.append("туфли")
# suitcase.append('рубашка')
# suitcase.append('трусы')
# print(suitcase)
# suitcase.pop()
# print(suitcase)

# PROBLEM 001:
#
# Из Множество 3 и 4
# Напишите код, который: Выведет новое множество, которое есть как в
# первой ферме, так и во второй.
# Выведет новое МНОЖЕСТВО, состоящее из животных,
# которые есть в первой ферме, но нет во второй.

