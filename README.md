# SIDFIT-FOSTER-TANKS-Authorization
# Инструменты разработки

* Языки программирования: Python
* Редактор кода: Pycharm
  
Управление в игре:
Игрок 1 (синий танк): WASD - движение, Пробел - стрельба
Игрок 2 (красный танк): Стрелки - движение, Enter - стрельба
После окончания игры нажмите R для рестарта

### 1. Структура проекта
структура папок и файлов для проекта:
``` bash
Tank-Game/
├── assets/               # Папка для ресурсов (изображения, музыка и т.д.)
│   ├── icon.ico          # Иконка приложения
│   ├── TANK3.jpg         # Фоновое изображение
│   └── TANK-proezd_tanka.mp3  # Музыкальный файл
├── src/                  # Папка с исходным кодом
│   └── main.py           # Основной файл программы
├── users.json            # Файл для хранения данных пользователей
├── .gitignore            # Файл для игнорирования ненужных файлов
└── README.md             # Основная документация проекта
```
### 2. Перемещение файлов
Переместите все ресурсы (например, icon.ico, TANK3.jpg, TANK-proezd tanka.mp3) в папку assets.
Внесите изменения в пути к файлам в коде. Например:
``` bash
root.iconbitmap('assets/icon.ico')
image = Image.open("assets/TANK3.jpg")
pygame.mixer.music.load("assets/TANK-proezd_tanka.mp3")
```
### 3. Файл README.md
Создайте файл README.md с описанием проекта. Пример содержимого:
``` bash
# Tank Game

Проект представляет собой игру "Танки" с функционалом авторизации и регистрации пользователей. После входа в систему пользователь может запустить игру.

## Особенности
- Авторизация и регистрация пользователей.
- Сохранение данных пользователей в файл `users.json`.
- Мультиплеер на одном экране (два игрока).
- Добавлена фоновая музыка и возможность её отключения.
```
## Установка

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/yourusername/Tank-Game.git 
   cd Tank-Game
```
Установите необходимые зависимости:
``` bash
pip install -r requirements.txt
```
Запустите игру:
``` bash
python src/main.py
```

### Зависимости

| Python 3.x | Pygame | Tkinter | Pillow | Colorama |

Установите зависимости с помощью:
``` bash
pip install pygame pillow colorama
```
