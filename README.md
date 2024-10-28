# Социальная сеть для путешественников

Данное приложение подразумевает, что пользователи будут писать посты для
каких-либо стран (страна выступает в качестве категории).

## Содержание

1. [Начало работы](#начало-работы)
   - [Требования](#требования)
   - [Установка](#установка)
2. [Настройка Docker](#настройка-docker)
   - [Сборка и запуск в Docker](#сборка-и-запуск-в-docker)
   - [Переменные окружения](#переменные-окружения)
3. [Использование](#использование)

---

## Начало работы

### Требования

Убедитесь, что установлены следующие компоненты:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ваш-юзернейм/название-репозитория.git
   cd название-репозитория
   ```

2. **Настройте переменные окружения:**
   ```bash
   cp .env.example .env
   ```
## Настройка Docker

### Сборка и запуск в Docker

1. **Соберите образы Docker:**
   ```bash
   docker-compose build
   ```

2. **Запустите контейнеры Docker:**
   ```bash
   docker-compose up -d
   ```

3. **Доступ к приложению:** Обычно ваше приложение будет доступно по адресу
   
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Переменные окружения

Добавьте информацию о необходимых переменных окружения в файл .env. Пример конфигурации:
   ```makefile
   SECRET_KEY=

   POSTGRES_DB=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_HOST=postgres_db # db for docker
   POSTGRES_PORT=5432
   
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   EMAIL_USE_TLS=True
   
   COUNTRY_LAYER_API_KEY=
   ```

## Использование

1. **Создайте суперпользователя (для доступа к админке):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

2. **Если данные городов пусты, то загрузите их с [API](https://countrylayer.com/):**
   ```bash
   docker-compose exec web python parser.py
   ```
