FROM python:3.12-slim

# Встановлюємо робочий каталог в контейнері
WORKDIR /app

# Копіюємо requirements.txt і встановлюємо залежності
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо увесь код проєкту в контейнер
COPY . /app/

# Відкриваємо порт 8000 для доступу до застосунку
EXPOSE 8000

# Запускаємо ваш Python застосунок
CMD ["python","-m", "thing_app"]