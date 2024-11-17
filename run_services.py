import threading
import subprocess
import os
import sys

def run_user_service():
    # Вказуємо абсолютний шлях до activate скрипта
    activate_script = os.path.join(os.getcwd(), '.\\venv\\Scripts\\activate.bat')
    # Команда для активації середовища і запуску сервісу
    subprocess.run([activate_script, "&&", "python", "user_service/app.py"], shell=True)

def run_thing_service():
    # Вказуємо абсолютний шлях до activate скрипта
    activate_script = os.path.join(os.getcwd(), '.\\venv\\Scripts\\activate.bat')
    # Команда для активації середовища і запуску сервісу
    subprocess.run([activate_script, "&&", "python", "thing_service/app.py"], shell=True)

if __name__ == "__main__":
    # Створення потоків для кожного сервісу
    user_service_thread = threading.Thread(target=run_user_service)
    thing_service_thread = threading.Thread(target=run_thing_service)

    # Запуск потоків
    user_service_thread.start()
    thing_service_thread.start()

    # Очікуємо завершення всіх потоків
    user_service_thread.join()
    thing_service_thread.join()
