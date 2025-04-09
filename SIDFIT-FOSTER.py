from tkinter import *
from tkinter import messagebox
from colorama import *
import json

# Инициализация данных пользователей
try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}

# Функция для регистрации нового пользователя
def register():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        if username in users:
            messagebox.showerror('Ошибка', 'Пользователь с таким именем уже существует!')
        else:
            users[username] = password
            save_users()
            messagebox.showinfo('Успех', 'Регистрация прошла успешно!')
    else:
        messagebox.showerror('Ошибка', 'Заполните все поля!')

# Функция для сохранения пользователей в файл
def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)

# Функция для авторизации
def click():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo('Авторизация пройдена', f'{username}, вы успешно вошли!')
        open_new_window(username)  # Открываем новое окно после успешной авторизации
    else:
        messagebox.showerror('Ошибка', 'Неправильное имя пользователя или пароль!')
        # Очищаем поля ввода
        username_entry.delete(0, END)
        password_entry.delete(0, END)

# Создание окна авторизации
root = Tk()
root.title('Авторизация')
root.geometry('450x230')
root.resizable(width=False, height=False)
root['bg'] = 'black'

main_label = Label(root, text='Авторизация', font='Arial 15 bold', bg='black', fg='white')
main_label.pack()

username_label = Label(root, text='Имя пользователя', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
username_label.pack()

username_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
username_entry.pack()

password_label = Label(root, text='Пароль', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
password_entry.pack()

# Кнопка входа
send_button = Button(root, text='Войти', command=click, bg='Lime')
send_button.pack(padx=10, pady=8)

# **Добавленная кнопка регистрации**
register_button = Button(root, text='Зарегистрироваться', command=register)
register_button.pack(padx=10, pady=8)
root.iconbitmap('D:/GitHub-Pycharm/icon.ico')

# Функция для открытия нового окна после авторизации
def open_new_window(username):
    new_window = Toplevel(root)
    new_window.title('Добро пожаловать')
    new_window.geometry('400x300')
    new_window.resizable(width=False, height=False)
    new_window['bg'] = 'black'

    welcome_label = Label(new_window,
                          text=f'Добро пожаловать, {username}!',
                          font='Arial 20 bold',
                          bg='black',
                          fg='lime')
    welcome_label.pack(pady=50)

    info_label = Label(new_window,
                       text='Вы успешно авторизовались в системе',
                       font='Arial 14',
                       bg='black',
                       fg='white')
    info_label.pack()




root.mainloop()

# init()
# print(Back.BLACK)
# print(Back.BLACK + Fore.RED + 'Добро пожаловать в "SIDFIT-FOSTER"')
# name = input(Fore.BLUE + Style.BRIGHT + 'Введите ваше имя: ')
# name1 = 'Здравствуйте: '
# print(Fore.BLUE + name1 + name)