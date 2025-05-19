
import pygame
import random
import math
from tkinter import *
from tkinter import messagebox
from colorama import *
import json
import time
import sys
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

# Функция для очистки полей
def clear_fields():
    username_entry.delete(0, END)
    password_entry.delete(0, END)

# Функция для обновления времени
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Текущее время в формате часы:минуты:секунды
    time_label.config(text=f"{current_time}")  # Обновляем текст метки
    root.after(1000, update_time)  # Вызываем функцию снова через 1000 мс (1 секунду)

# Функция для сохранения пользователей в файл
def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)


# Функция для запуска игры "Танки"
def start_tanks_game():
    pygame.init()

    # Настройки экрана
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Танки")

    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Класс танка
    class Tank:
        def __init__(self, x, y, color, controls):
            self.x = x
            self.y = y
            self.color = color
            self.width = 40
            self.height = 40
            self.speed = 5
            self.direction = 0  # 0 - вверх, 1 - вправо, 2 - вниз, 3 - влево
            self.health = 100
            self.controls = controls
            self.cooldown = 0

        def draw(self):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

            if self.direction == 0:
                pygame.draw.rect(screen, BLACK, (self.x + self.width // 2 - 3, self.y - 15, 6, 15))
            elif self.direction == 1:
                pygame.draw.rect(screen, BLACK, (self.x + self.width, self.y + self.height // 2 - 3, 15, 6))
            elif self.direction == 2:
                pygame.draw.rect(screen, BLACK, (self.x + self.width // 2 - 3, self.y + self.height, 6, 15))
            elif self.direction == 3:
                pygame.draw.rect(screen, BLACK, (self.x - 15, self.y + self.height // 2 - 3, 15, 6))

            pygame.draw.rect(screen, RED, (self.x, self.y - 10, self.width, 5))
            pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, self.width * (self.health / 100), 5))

        def move(self, keys):
            if keys[self.controls["up"]]:
                self.y -= self.speed
                self.direction = 0
            if keys[self.controls["down"]]:
                self.y += self.speed
                self.direction = 2
            if keys[self.controls["left"]]:
                self.x -= self.speed
                self.direction = 3
            if keys[self.controls["right"]]:
                self.x += self.speed
                self.direction = 1

            self.x = max(0, min(WIDTH - self.width, self.x))
            self.y = max(0, min(HEIGHT - self.height, self.y))

            if self.cooldown > 0:
                self.cooldown -= 1

        def shoot(self):
            if self.cooldown == 0:
                self.cooldown = 30
                if self.direction == 0:
                    return Bullet(self.x + self.width // 2, self.y, 0, -10, self.color)
                elif self.direction == 1:
                    return Bullet(self.x + self.width, self.y + self.height // 2, 10, 0, self.color)
                elif self.direction == 2:
                    return Bullet(self.x + self.width // 2, self.y + self.height, 0, 10, self.color)
                elif self.direction == 3:
                    return Bullet(self.x, self.y + self.height // 2, -10, 0, self.color)
            return None

    # Класс пули
    class Bullet:
        def __init__(self, x, y, dx, dy, color):
            self.x = x
            self.y = y
            self.dx = dx
            self.dy = dy
            self.radius = 5
            self.color = color
            self.active = True

        def update(self):
            self.x += self.dx
            self.y += self.dy

            if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
                self.active = False

        def draw(self):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        def check_collision(self, tank):
            if (self.x > tank.x and self.x < tank.x + tank.width and
                    self.y > tank.y and self.y < tank.y + tank.height):
                tank.health -= 10
                self.active = False
                return True
            return False

    # Создание танков
    player1 = Tank(100, HEIGHT // 2, BLUE, {
        "up": pygame.K_w,
        "down": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
        "shoot": pygame.K_SPACE
    })

    player2 = Tank(WIDTH - 140, HEIGHT // 2, RED, {
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "shoot": pygame.K_RETURN
    })

    bullets = []
    clock = pygame.time.Clock()
    running = True
    game_over = False
    winner = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == player1.controls["shoot"]:
                    bullet = player1.shoot()
                    if bullet:
                        bullets.append(bullet)
                if event.key == player2.controls["shoot"]:
                    bullet = player2.shoot()
                    if bullet:
                        bullets.append(bullet)

        if not game_over:
            keys = pygame.key.get_pressed()
            player1.move(keys)
            player2.move(keys)

            for bullet in bullets[:]:
                bullet.update()
                if not bullet.active:
                    bullets.remove(bullet)
                else:
                    if bullet.color == BLUE:
                        if bullet.check_collision(player2):
                            if player2.health <= 0:
                                game_over = True
                                winner = "Игрок 1 (Синий)"
                    else:
                        if bullet.check_collision(player1):
                            if player1.health <= 0:
                                game_over = True
                                winner = "Игрок 2 (Красный)"

        screen.fill(WHITE)
        player1.draw()
        player2.draw()

        for bullet in bullets:
            bullet.draw()

        font = pygame.font.SysFont(None, 36)
        health_text1 = font.render(f"P1: {player1.health}", True, BLUE)
        health_text2 = font.render(f"P2: {player2.health}", True, RED)
        screen.blit(health_text1, (10, 10))
        screen.blit(health_text2, (WIDTH - 100, 10))

        if game_over:
            game_over_text = font.render(f"Победитель: {winner}!", True, BLACK)
            restart_text = font.render("Нажмите R для рестарта", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
            screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                player1 = Tank(100, HEIGHT // 2, BLUE, {
                    "up": pygame.K_w,
                    "down": pygame.K_s,
                    "left": pygame.K_a,
                    "right": pygame.K_d,
                    "shoot": pygame.K_SPACE
                })
                player2 = Tank(WIDTH - 140, HEIGHT // 2, RED, {
                    "up": pygame.K_UP,
                    "down": pygame.K_DOWN,
                    "left": pygame.K_LEFT,
                    "right": pygame.K_RIGHT,
                    "shoot": pygame.K_RETURN
                })
                bullets = []
                game_over = False
                winner = None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Функция для авторизации
def click():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo('Авторизация пройдена', f'{username}, вы успешно вошли!')
        open_new_window(username)  # Открываем новое окно после успешной авторизации
        # Очищаем поля при успешной авторизации
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    else:
        messagebox.showerror('Ошибка', 'Неправильное имя пользователя или пароль!')
        # Очищаем поля ввода
        username_entry.delete(0, END)
        password_entry.delete(0, END)

# Создание окна авторизации
root = Tk()
root.title('Авторизация')
root.geometry('450x280')
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

# Новая кнопка "Очистить"
clear_button = Button(root,
                     text='Очистить',
                     command=clear_fields,
                     bg='gray',
                     fg='white')
clear_button.pack(padx=10, pady=5)

# Метка для отображения времени
time_label = Label(root, font='Arial 10 bold', bg='black', fg='cyan')  # Цвет текста - синий
time_label.place(relx=0.95, rely=0.05, anchor='ne')  # Размещаем в правом верхнем углу

# Запускаем обновление времени
update_time()

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
    welcome_label.pack(pady=30)

    info_label = Label(new_window,
                      text='Вы успешно авторизовались в системе',
                      font='Arial 14',
                      bg='black',
                      fg='white')
    info_label.pack()

    game_button = Button(new_window,
                        text='Играть в Танки',
                        command=start_tanks_game,
                        font='Arial 14 bold',
                        bg='lime',
                        fg='black',
                        width=15,
                        height=2)
    game_button.pack(pady=30)




root.mainloop()

# init()
# print(Back.BLACK)
# print(Back.BLACK + Fore.RED + 'Добро пожаловать в "SIDFIT-FOSTER"')
# name = input(Fore.BLUE + Style.BRIGHT + 'Введите ваше имя: ')
# name1 = 'Здравствуйте: '
# print(Fore.BLUE + name1 + name)