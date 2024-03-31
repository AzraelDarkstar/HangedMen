import random                             # Для случайной генерации
from colorama import Fore, Style, init    # Для добавления цвета
import art                                # Для вывода текста с использованием ASCII-арт

init()   # Инициализация colorama

from var import stages, words, alpha   # Импорт переменных из других файлов

word = list(random.choice(words).lower())  # Выбор случайного слова из списка и преобразование его в список букв
art.tprint('The  Game  Has  Started')  


length = len(word)  # Длина загаданного слова
fails = 0  # Количество ошибок
guesses = 0  # Количество угаданных букв

# Строка, которая будет отображать угаданные буквы и пропуски
string = list("_" * length)

# Основной цикл
while length != guesses and fails != 6:
    print(f'{"".join(string)}    Осталось {length - guesses}')  # Вывод текущего состояния слова и оставшихся попыток
    
    inp = input('Введите букву:').lower()  # Получение ввода от пользователя и преобразование его в нижний регистр
    
    if inp not in alpha:  # Проверка, является ли введенный символ буквой из алфавита
        print(Fore.YELLOW + 'Введена неверная буква' + Style.RESET_ALL)  
    elif inp in word:  # Проверка, есть ли введенная буква в загаданном слове
        print(Fore.GREEN + 'Эта буква есть в слове' + Style.RESET_ALL) 
        for i in range(word.count(inp)):  # Цикл для обновления строки с угаданными буквами
            index = word.index(inp)  # Поиск индекса угаданной буквы в слове
            string[index] = word[index]  # Обновление строки с угаданными буквами
            word[index] = '_'  
            guesses += 1  
            alpha.remove(inp)  # Удаление угаданной буквы из списка доступных букв
    else:
        print(Fore.RED + 'Этой буквы нет в слове' + Style.RESET_ALL)  # Вывод сообщения о том, что буквы нет в слове
        fails += 1  

    print(stages[fails])  # Вывод текущего состояния виселицы

# Проверка на завершение игры (выигрыш или проигрыш) и вывод соответствующего сообщения
if guesses == length:
    print(Fore.GREEN + '')
    art.tprint('YOU  WIN')
    print('' + Style.RESET_ALL)
else:
    print(Fore.RED + '')
    art.tprint('YOU  LOSE')
    print('' + Style.RESET_ALL)
