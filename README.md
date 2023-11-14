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
    - return `HttpResponse` with rendered template (use `render`).
4. Before you create a template you have to create styles for the 
template. Create directory `static` next to the directory `taxi`. Inside this 
directory create a file with the following path `css/styles.css`. Don't forget to do all necessary steps so that Django can serve these static files.
5. Create directory `templates` next to the directory `taxi`. There you will
store templates for pages. Edit settings so that engine knows where to look for template source files.
6. Всередині каталогу `templates` створіть шаблон `base.html`, він є батьківським
шаблон, інші шаблони розширять `base.html`. Всередині `base.html`:
   - Всередині `<head>`:
      - Створіть блок `title` із заголовком `Taxi Service` всередині
      - Завантажте статику та імпортуйте `styles.css`
   - Всередині `<body>`:
      - Створити блок `sidebar`
      - Створення блоку `content`
7. Всередині `templates` створіть каталог `taxi`. Там ви будете зберігати шаблони
для програми `таксі`. Створіть там `index.html`. Всередині `index.html`:
    - Замінити блок `content` і розмістити (у вигляді списку) інформацію про:
        - Кількість автомобілів
        - Кількість водіїв
        - Кількість виробників
8. Inside `templates` create a directory `includes`. There you will store includes. 
Create `sidebar.html` there. Inside `sidebar.html`:
    - Write realization of `sidebar` include that must have a list of empty links:
        - Home page
        - Manufacturers
        - Cars
        - Drivers
    - In `base.html` include `sidebar.html`, so all these links will be accessible on all pages.
9. Check that you put empty lines at the end of each HTML file.
10. Run server, open `http://127.0.0.1:8000/`, check if the information is there and if it is correct.
11. Run `python manage.py test` to check your code results.
12. Don't push a lot of extra files(`venv`, `pycache`, `.idea`, etc.) and don't forget to add `.gitignore` to your PR.

### Note: Attach screenshots of all created or modified pages to pull request. 

1) Attach screenshots to the comment, NOT in commit. 
2) It's important to **attach images** not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
