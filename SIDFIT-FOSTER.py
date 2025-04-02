from tkinter import *
from tkinter import messagebox
from colorama import *
# Добавления цвета
import json


# Функция для регистрации нового пользователя
def register():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        # Проверяем, существует ли пользователь
        if username in users:
            messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует!')
        else:
            # Сохраняем нового пользователя
            users[username] = password
            save_users()
            messagebox.showinfo('Успех', 'Регистрация прошла успешно!')
    else:
        messagebox.showerror('Ошибка', 'Заполните все поля!')
# Функция для авторизации
def click():
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Авторизация пройдена', f'{username}, {password}')

#Инициализация данных пользователей из файла
try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}



#Функция сохранения пользователей
def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)



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
username_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
username_entry.pack()
# Выводим в окно username_entry.pack()

# добавим поле password
password_lable = Label(root, text= 'Пароль', font='Arial 11 bold',bg='black', fg='white', padx=10, pady=8)
password_lable.pack()
# Выводим в окно password_lable.pack

# добавим поле для ввода пароля
password_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
password_entry.pack()
# Выводим в окно password_entry.pack()


# добавим кнопку
send_button = Button(root, text= 'Войти', command=click)
send_button.pack(padx=10, pady=8)
# Выводим в окно кнопку с размером send_button.pack(padx=10, pady=8)

# Функция для открытия окна регистрации
def open_register_window():
    # Создаем новое окно
    register_window = Toplevel(root)
    register_window.title("Регистрация")
    register_window.geometry("400x300")
    register_window.resizable(False, False)

# Добавим кнопку регистрации с переходом на новое окно
register_button = Button(root, text="Зарегистрироваться", command=open_register_window)
register_button.pack(padx=10, pady=8)

root.mainloop()


# init()
#print(Back.BLACK)
#print(Back.BLACK + Fore.RED + 'Добро пожаловать в "SIDFIT-FOSTER"')
#name = input(Fore.BLUE + Style.BRIGHT + 'Введите ваше имя: ')
#name1 ='Здравствуйте: '
#print(Fore.BLUE + name1 + name)