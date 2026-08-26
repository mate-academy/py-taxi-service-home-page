# Taxi service home page

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Use the following command to load prepared data from fixture to test and debug your code:

  ```python manage.py loaddata taxi_service_db_data.json```.

Feel free to add more data using admin panel, if needed.

In this task, you should implement the home page of the site.

1. Inside `taxi_service.urls` add path to the `taxi.urls`. Don't forget to specify `namespace`.
2. Inside `taxi.urls` create a path for the home page. This
page should open when you are accessing `http://127.0.0.1:8000/`. Give this
path the name `index`.
3. Inside `taxi.views` create function `index`. In this function:
    - count the number of all drivers with `num_drivers` variable
    - count the number of all manufacturers with `num_manufacturers` variable
    - count the number of all cars with `num_cars` variable 
    - return `HttpResponse` with rendered template. Pass received data to this template.

4. Before you create a template you have to create styles for the 
template. Create directory `static` next to the directory `taxi`. Inside this 
directory create a file with the following path `css/styles.css`. Don't forget to do all necessary steps so that Django can serve these static files.
5. Create directory `templates` next to the directory `taxi`. There you will
store templates for pages. Edit settings so that engine knows where to look for template source files.
6. Inside directory `templates` create template `base.html`, it is a parent 
template, other templates will extend `base.html`. Inside `base.html`:
   - Inside `<head>`:
      - Create block `title` with `Taxi Service` title inside
      - Load static and import `styles.css`
   - Inside `<body>`:
      - Create block `sidebar`
      - Create block `content`
7. Inside `templates` create a directory `taxi`. There you will store templates
for the app `taxi`. Create `index.html` there. Inside `index.html`:
    - Override block `content` and place (as a list) information about:
        - Number of cars
        - Number of drivers
        - Number of manufacturers
8. Inside `templates` create a directory `includes`. There you will store includes. 
Create `sidebar.html` there. Inside `sidebar.html`:
    - Write realization of `sidebar` include that must have a list of empty links:
        - Home page
        - Manufacturers
        - Cars
        - Drivers
    - Anchor tags can serve as placeholder links for this task, meaning the actual destination of the link is not a concern.
      For example, you can use `href="#"` as the link destination.

    - In `base.html` include `sidebar.html`, so all these links will be accessible on all pages.
9. Check that you put empty lines at the end of each HTML file.
10. Run server, open `http://127.0.0.1:8000/`, check if the information is there and if it is correct.
11. Run `python manage.py test` to check your code results.
12. Avoid adding unnecessary files (like `venv`, `pycache`, `.idea`, `db.sqlite3`) and remember to include a `.gitignore` file in your PR.

### Note: Attach screenshots of all created or modified pages to pull request. 

1) Attach screenshots to the comment, NOT in commit. 
2) It's important to **attach images** not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)






# Головна сторінка сервісу таксі

- Перед початком роботи ознайомтеся з [інструкцією](https://github.com/mate-academy/py-task-guideline/blob/main/README.md).
- Використовуйте таку команду для завантаження підготовлених даних із фікстури (fixture) для тестування та налагодження коду:

  ```python manage.py loaddata taxi_service_db_data.json```.

За потреби ви можете додати більше даних через панель адміністратора.

У цьому завданні вам потрібно реалізувати головну сторінку сайту.

1. У файлі `taxi_service.urls` додайте шлях до `taxi.urls`. Не забудьте вказати `namespace`.
2. У файлі `taxi.urls` створіть шлях для головної сторінки. Ця
   сторінка має відкриватися за адресою `http://127.0.0.1:8000/`. Назвіть цей
   шлях `index`.
3. У файлі `taxi.views` створіть функцію `index`. У цій функції:
    - підрахуйте кількість усіх водіїв і збережіть її у змінній `num_drivers`
    - підрахуйте кількість усіх виробників і збережіть її у змінній `num_manufacturers`
    - підрахуйте кількість усіх автомобілів і збережіть її у змінній `num_cars`
    - поверніть `HttpResponse` із відрендереним шаблоном. Передайте отримані дані в цей шаблон.

4. Перш ніж створювати шаблон, потрібно підготувати для нього стилі. Створіть директорію `static` поруч із директорією `taxi`. У цій
   директорії створіть файл за шляхом `css/styles.css`. Не забудьте виконати всі необхідні дії, щоб Django міг обслуговувати ці статичні файли.
5. Створіть директорію `templates` поруч із директорією `taxi`. Там ви
   зберігатимете шаблони сторінок. Налаштуйте параметри проєкту так, щоб рушій шаблонів знав, де шукати вихідні файли шаблонів.
6. У директорії `templates` створіть шаблон `base.html` — це базовий (батьківський)
   шаблон, від якого успадковуватимуться інші шаблони. У файлі `base.html`:
   - Усередині `<head>`:
      - Створіть блок `title` із заголовком `Taxi Service` всередині
      - Завантажте статичні файли (static) та підключіть `styles.css`
   - Усередині `<body>`:
      - Створіть блок `sidebar`
      - Створіть блок `content`


7. Усередині папки `templates` створіть директорію `taxi`. Там ви зберігатимете шаблони для застосунку `taxi`. Створіть там файл `index.html`. Усередині `index.html`:
    - Перевизначте блок `content` і розмістіть (у вигляді списку) інформацію про:
        - Кількість автомобілів
        - Кількість водіїв
        - Кількість виробників
8. Усередині `templates` створіть директорію `includes`. Там ви зберігатимете файли для включення (includes). Створіть там файл `sidebar.html`. Усередині `sidebar.html`:
    - Реалізуйте бічну панель (`sidebar`), яка міститиме список посилань-заглушок:
        - Головна сторінка
        - Виробники
        - Автомобілі
        - Водії
    - Для цього завдання можна використовувати теги `<a>` із посиланнями-заглушками (тобто конкретна адреса переходу не має значення).
      Наприклад, можна використовувати `href="#"`.

    - Підключіть `sidebar.html` у файлі `base.html`, щоб ці посилання були доступні на всіх сторінках.
9. Переконайтеся, що в кінці кожного HTML-файлу є порожній рядок.
10. Запустіть сервер, відкрийте `http://127.0.0.1:8000/`, перевірте наявність і правильність відображення інформації.
11. Запустіть `python manage.py test`, щоб перевірити результати виконання коду.
12. Уникайте додавання зайвих файлів (таких як `venv`, `pycache`, `.idea`, `db.sqlite3`) і не забудьте додати файл `.gitignore` до свого PR.

### Примітка: Додайте скріншоти всіх створених або змінених сторінок до pull request.

1) Додавайте скріншоти до коментаря, а НЕ до коміту.
2) Важливо **прикріплювати самі зображення**, а не посилання на них. Див. приклад:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)