from tkinter import *
from tkinter import messagebox
from colorama import *
# Добавления цвета


# Создание окна авторизации
root =Tk()
root.title('Авторизация')
# Добавим заголовок
root.geometry('450x230')
# Разрешение окна
root.resizable(width=False, height=False)
# Добавим запрет чтобы окно нельзя было растягивать
# (width=False-ширина),(height=False-высота)
root['bg'] = 'black'
# Добавим фон (balck-черный)

main_label = Label(root, text='Авторизация', font='Arial 15 bold', bg='black', fg='white' )
main_label.pack()
# выводим в окно main_label.pack()
username_lable = Label(root, text= 'Имя пользователя', font='Arial 11 bold',bg='black', fg='white', padx=10, pady=8)
username_lable.pack()
# выводим в окно username_lable.pack()


#добавляем поле для ввода текста
username_entry = Entry(root, bg='black', fg='lime', font='Arial 12 bold')
username_entry.pack()
# Выводим в окно

root.mainloop()


# init()
#print(Back.BLACK)
#print(Back.BLACK + Fore.RED + 'Добро пожаловать в "SIDFIT-FOSTER"')
#name = input(Fore.BLUE + Style.BRIGHT + 'Введите ваше имя: ')
#name1 ='Здравствуйте: '
#print(Fore.BLUE + name1 + name)
