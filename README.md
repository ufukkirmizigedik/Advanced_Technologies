# AdvTech Web Site

## Описание проекта

AdvTech — это веб-сайт, разработанный с использованием Django. Сайт поддерживает два языка: русский и английский. Веб-сайт активно используется и доступен по адресу [www.advtech.kg](http://www.advtech.kg).

## Функции

- Двуязычная поддержка: Русский и Английский языки.
- Актуальная информация о продуктах и услугах компании.
- Интуитивно понятный интерфейс для пользователей.

## Установка и запуск

### Клонирование репозитория

```bash
git clone https://github.com/ufukkirmizigedik/advtech.git
cd advtech

Создайте виртуальное окружение и активируйте его:

python -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


