# При старте приложения запускаются три потока.
# Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список
# заполнен оба потока запускаются. Первый поток находит
# сумму элементов списка, второй поток среднеарифметическое значение в списке. Полученный список, сумма и
# среднеарифметическое выводятся на экран.



# import random
# import threading
#
#
# random_list = []
# list_filled_event = threading.Event()
#
#
# LIST_SIZE = 10
#
#
# def fill_list():
#     global random_list
#     random_list = [random.randint(1, 100) for _ in range(LIST_SIZE)]
#     print(f"Список заполнен: {random_list}")
#     list_filled_event.set()
#
#
# def calculate_sum():
#     list_filled_event.wait()
#     total_sum = sum(random_list)
#     print(f"Сумма элементов списка: {total_sum}")
#
#
# def calculate_average():
#     list_filled_event.wait()
#     average = sum(random_list) / len(random_list)
#     print(f"Среднее арифметическое значение: {average}")
#
#
# fill_thread = threading.Thread(target=fill_list)
# sum_thread = threading.Thread(target=calculate_sum)
# avg_thread = threading.Thread(target=calculate_average)
#
#
# fill_thread.start()
# sum_thread.start()
# avg_thread.start()
#
#
# fill_thread.join()
# sum_thread.join()
# avg_thread.join()


# Пользователь с клавиатуры вводит путь к файлу.
# После чего запускаются три потока. Первый поток заполняет файл случайными числами. Два других потока
# ожидают заполнения. Когда файл заполнен оба потока
# стартуют. Первый поток находит все простые числа, второй поток факториал каждого числа в файле. Результаты
# поиска каждый поток должен записать в новый файл.

# #
#
# import random
# import threading
# from math import factorial
#
#
# file_filled_event = threading.Event()
#
#
# NUMBER_COUNT = 10
# MAX_RANDOM = 50
#
#
# file_path = input("Введите путь к файлу для записи случайных чисел: ")
# prime_file_path = file_path + "_prime.txt"
# factorial_file_path = file_path + "_factorial.txt"
#
#
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def fill_file():
#     with open(file_path, 'w') as f:
#         random_numbers = [random.randint(1, MAX_RANDOM) for _ in range(NUMBER_COUNT)]
#         f.write(" ".join(map(str, random_numbers)))
#     print(f"Файл {file_path} заполнен случайными числами.")
#     file_filled_event.set()
#
#
# def find_primes():
#     file_filled_event.wait()
#     with open(file_path, 'r') as f:
#         numbers = list(map(int, f.read().split()))
#
#     primes = [num for num in numbers if is_prime(num)]
#
#     with open(prime_file_path, 'w') as f:
#         f.write(" ".join(map(str, primes)))
#     print(f"Простые числа записаны в файл {prime_file_path}.")
#
#
# def calculate_factorials():
#     file_filled_event.wait()
#     with open(file_path, 'r') as f:
#         numbers = list(map(int, f.read().split()))
#
#     factorials = [factorial(num) for num in numbers]
#
#     with open(factorial_file_path, 'w') as f:
#         f.write(" ".join(map(str, factorials)))
#     print(f"Факториалы чисел записаны в файл {factorial_file_path}.")
#
#
# fill_thread = threading.Thread(target=fill_file)
# prime_thread = threading.Thread(target=find_primes)
# factorial_thread = threading.Thread(target=calculate_factorials)
#
#
# fill_thread.start()
# prime_thread.start()
# factorial_thread.start()
#
#
# fill_thread.join()
# prime_thread.join()
# factorial_thread.join()

# Пользователь с клавиатуры вводит путь к существующей директории и к новой директории. После чего
# запускается поток, который должен скопировать содержимое директории в новое место. Необходимо сохранить
# структуру директории. На экран необходимо отобразить
# статистику выполненных операций.

#
# import os
# import shutil
# import threading
#
#
#
# def copy_directory(src_dir, dst_dir):
#     if not os.path.exists(src_dir):
#         print("Исходная директория не существует.")
#         return
#
#     if not os.path.exists(dst_dir):
#         os.makedirs(dst_dir)
#         print(f"Создана директория: {dst_dir}")
#
#
#     files_count = 0
#     directories_count = 0
#
#
#     for dirpath, dirnames, filenames in os.walk(src_dir):
#
#         relative_path = os.path.relpath(dirpath, src_dir)
#         destination_path = os.path.join(dst_dir, relative_path)
#
#
#         if not os.path.exists(destination_path):
#             os.makedirs(destination_path)
#             directories_count += 1
#
#
#         for filename in filenames:
#             src_file = os.path.join(dirpath, filename)
#             dst_file = os.path.join(destination_path, filename)
#             shutil.copy2(src_file, dst_file)
#             files_count += 1
#
#
#     print("Копирование завершено.")
#     print(f"Количество скопированных файлов: {files_count}")
#     print(f"Количество созданных директорий: {directories_count}")
#
#
#
# def start_copying_thread():
#     src_dir = input("Введите путь к существующей директории: ")
#     dst_dir = input("Введите путь к новой директории: ")
#
#
#     copy_thread = threading.Thread(target=copy_directory, args=(src_dir, dst_dir))
#     copy_thread.start()
#
#
#     copy_thread.join()
#
#
# if __name__ == "__main__":
#     start_copying_thread()
#
