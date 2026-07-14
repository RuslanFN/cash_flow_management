# Идеально точный базовый образ под ваш Python
FROM python:3.14-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Оптимизация работы Python внутри Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8

# Обновляем pip
RUN pip install --no-cache-dir --upgrade pip

# Копируем ваш requirements.txt
COPY requirements.txt .

# Устанавливаем ваши зависимости (psycopg-binary установится мгновенно)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы и фикстуры вашего проекта
COPY . .

# Открываем порт для встроенного веб-сервера Django
EXPOSE 8000

# Команда для запуска (переопределяется в docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
