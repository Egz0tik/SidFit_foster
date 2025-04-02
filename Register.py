from tkinter import *
from tkinter import messagebox

# Создаем окно авторизации
root = Tk()
root.title("Авторизация")
root.geometry("400x200")
root.resizable(False, False)

# Функция для открытия окна регистрации
def open_register_window():
    # Создаем новое окно
    register_window = Toplevel(root)
    register_window.title("Регистрация")
    register_window.geometry("400x300")
    register_window.resizable(False, False)

    # Добавляем поля для ввода данных
    Label(register_window, text="ФИО:").pack(pady=5)
    fio_entry = Entry(register_window)
    fio_entry.pack(pady=5)

    Label(register_window, text="Email:").pack(pady=5)
    email_entry = Entry(register_window)
    email_entry.pack(pady=5)

    Label(register_window, text="Имя пользователя:").pack(pady=5)
    username_entry = Entry(register_window)
    username_entry.pack(pady=5)

    Label(register_window, text="Пароль:").pack(pady=5)
    password_entry = Entry(register_window, show="*")
    password_entry.pack(pady=5)

    # Функция для сохранения данных
    def save_user():
        fio = fio_entry.get().strip()
        email = email_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not fio or not email or not username or not password:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return

        # Здесь можно добавить логику сохранения в базу данных или файл
        messagebox.showinfo("Успех", f"Регистрация прошла успешно!\nДанные:\nФИО: {fio}\nEmail: {email}")
        register_window.destroy()  # Закрываем окно регистрации

    # Кнопка для завершения регистрации
    register_btn = Button(register_window, text="Зарегистрироваться", command=save_user)
    register_btn.pack(pady=10)

# Кнопка регистрации
register_button = Button(root, text="Зарегистрироваться", command=open_register_window)
register_button.pack(padx=10, pady=8)

root.mainloop()