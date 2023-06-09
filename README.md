## Проект YaMDb

Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список **категорий (Category)** может быть расширен администратором.

Сами произведения в **YaMDb** не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть **произведения**: книги, фильмы или музыка. Например, в категории "Книги" могут быть произведения "Винни Пух и все-все-все" и "Марсианские хроники", а в категории "Музыка" — песня "Давеча" группы "Насекомые" и вторая сюита Баха.

Произведению может быть присвоен **жанр** (**Genre**) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые **отзывы** (**Review**) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.



## Ресурсы API YaMDb

- Ресурс **auth**: аутентификация.

- Ресурс **users**: пользователи.

- Ресурс **titles**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

- Ресурс **categories**: категории (типы) произведений («Фильмы», «Книги», «Музыка»).

- Ресурс **genres**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

- Ресурс **reviews**: отзывы на произведения. Отзыв привязан к определённому произведению.

- Ресурс **comments**: комментарии к отзывам. Комментарий привязан к определённому отзыву.



## Пользовательские роли

- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

- **Аутентифицированный пользователь (user)** — может читать всё, как и 

- **Аноним**, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.

- **Модератор (moderator)** — те же права, что и у **Аутентифицированного пользователя**, плюс право удалять и редактировать **любые** отзывы и комментарии.

- **Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

- **Суперюзер Django** должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.



## Установка

Для запуска приложения проделайте следующие шаги:

1. Склонируйте репозиторий:
```
git clone git@github.com:Slexvik/api_yamdb.git
```

2. Перейдите в папку с кодом и создайте виртуальное окружение:
```
Для Windows:
cd api_yamdb
python -m venv venv
```
```
Для Linux/macOS:
cd api_yamdb
python3 -m venv venv
```

3. Активируйте виртуальное окружение:
```
Для Windows:
source venv\Scripts\activate
```
```
Для Linux/macOS:
source venv\bin\activate
```
4. Установите зависимости:
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
5. Выполните миграции:
```
python manage.py migrate
```
6. Импортируйте данные из csv:
```
python manage.py import_csv
```
7. Создайте суперпользователя:
```
python manage.py createsuperuser
```
8. Запустите сервер:
```
python manage.py runserver
```


## Документация

 http://127.0.0.1:8000/redoc/


 ## Авторы проекта:

- Auth/Users: Алексей [Github](https://github.com/Slexvik)
- Titles/Category/Genre: Константин [Github](https://github.com/realkast7)
- Reviews/Comments: Ольга [Github](https://github.co/Xiaoan2805)