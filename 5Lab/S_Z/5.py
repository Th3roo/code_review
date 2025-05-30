# Задача 5: Тестирование словарного запаса
import os

def task_5_vocabulary_tester():
    """
    Решение задачи 5: Тестирование словарного запаса.
    Есть два текстовых файла: с русскими словами и их английскими
    переводами (построчно). Программа тестирует пользователя,
    выводит слова, ждет перевод, сравнивает и ставит оценку.
    """
    russian_file_name = "russian_words.txt"
    english_file_name = "english_translations.txt"

    def create_demo_files_if_not_exist():
        if not os.path.exists(russian_file_name) or \
           not os.path.exists(english_file_name):
            print(f"Файл(ы) '{russian_file_name}' и/или "
                  f"'{english_file_name}' не найдены.")
            print("Создаются демонстрационные файлы...")
            demo_rus_words = ["привет", "мир", "кот", "собака", "дом", "школа"]
            demo_eng_words = [
                "hello", "world", "cat", "dog", "house", "school"
            ]
            try:
                with open(russian_file_name, "w", encoding="utf-8") as f_rus:
                    for word in demo_rus_words:
                        f_rus.write(word + "\n")
                with open(english_file_name, "w", encoding="utf-8") as f_eng:
                    for word in demo_eng_words:
                        f_eng.write(word + "\n")
                print("Демонстрационные файлы успешно созданы.")
                return True
            except IOError as e:
                print(f"Ошибка при создании демонстрационных файлов: {e}")
                return False
        return True

    if not create_demo_files_if_not_exist():
        return

    try:
        with open(russian_file_name, "r", encoding="utf-8") as f_rus, \
             open(english_file_name, "r", encoding="utf-8") as f_eng:
            russian_words = [line.strip() for line in f_rus if line.strip()]
            english_translations = [
                line.strip() for line in f_eng if line.strip()
            ]
    except FileNotFoundError:
        print(f"Не удалось открыть файлы '{russian_file_name}' или "
              f"'{english_file_name}'.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файлов: {e}")
        return

    if not russian_words or not english_translations:
        print("Один из файлов пуст или оба пусты. Тестирование невозможно.")
        return

    if len(russian_words) != len(english_translations):
        print("Количество слов в файлах не совпадает. "
              "Проверьте содержимое файлов.")
        print(f"Русских слов: {len(russian_words)}, "
              f"Английских переводов: {len(english_translations)}")
        return

    correct_answers_count = 0
    total_questions_count = len(russian_words)

    print("\n--- Начинаем тест на знание слов ---")
    print("Введите английский перевод для каждого русского слова.")

    for i in range(total_questions_count):
        rus_word = russian_words[i]
        correct_translation = english_translations[i]

        user_answer = input(f"Русское слово: '{rus_word}'. Ваш перевод: ")
        user_answer_cleaned = user_answer.strip().lower()
        correct_translation_cleaned = correct_translation.strip().lower()

        if user_answer_cleaned == correct_translation_cleaned:
            print("Верно!")
            correct_answers_count += 1
        else:
            print(f"Неверно. Правильный ответ: '{correct_translation}'")
        print("-" * 20)

    print("\n--- Тест завершен ---")
    print(f"Всего вопросов: {total_questions_count}")
    print(f"Правильных ответов: {correct_answers_count}")

    if total_questions_count > 0:
        percentage = (correct_answers_count / total_questions_count) * 100
        print(f"Процент правильных ответов: {percentage:.2f}%")

        # Определение оценки (примерная система)
        if percentage == 100:
            grade = 5
            comment = "Отлично!"
        elif percentage >= 80:
            grade = 4
            comment = "Хорошо!"
        elif percentage >= 60:
            grade = 3
            comment = "Удовлетворительно."
        elif percentage >= 40:
            grade = 2
            comment = "Неудовлетворительно, нужно подучить."
        else:
            grade = 1 # или 2, в зависимости от системы
            comment = "Очень плохо, срочно учить слова!"
        print(f"Ваша оценка: {grade} ({comment})")
    else:
        print("Тест не содержал вопросов.")

if __name__ == '__main__':
    print("--- Задача 5: Тестирование словарного запаса ---")
    task_5_vocabulary_tester()