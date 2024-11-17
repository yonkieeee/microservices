import threading
import subprocess


def run_user_service():
    subprocess.run(["python", "user_service/user_app.py"])


def run_thing_service():
    subprocess.run(["python", "thing_service/thing_app.py"])


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