import os

RUSSIAN_FILE_NAME = "russian_words.txt"
ENGLISH_FILE_NAME = "english_translations.txt"


def create_demo_files_if_not_exist():
    # Creates demo vocabulary files if they don't exist.
    # Returns True if files are ready or created, False on creation error.
    if not os.path.exists(RUSSIAN_FILE_NAME) or \
       not os.path.exists(ENGLISH_FILE_NAME):
        print(f"Файл(ы) '{RUSSIAN_FILE_NAME}' и/или "
              f"'{ENGLISH_FILE_NAME}' не найдены.")
        print("Создаются демонстрационные файлы...")
        demo_rus_words = ["привет", "мир", "кот", "собака", "дом", "школа"]
        demo_eng_words = ["hello", "world", "cat", "dog", "house", "school"]
        try:
            with open(RUSSIAN_FILE_NAME, "w", encoding="utf-8") as f_rus:
                for word in demo_rus_words:
                    f_rus.write(word + "\n")
            with open(ENGLISH_FILE_NAME, "w", encoding="utf-8") as f_eng:
                for word in demo_eng_words:
                    f_eng.write(word + "\n")
            print("Демонстрационные файлы успешно созданы.")
            return True
        except IOError as e:
            print(f"Ошибка при создании демонстрационных файлов: {e}")
            return False
    return True


def load_vocabulary():
    # Loads words from vocabulary files.
    # Returns (russian_words, english_translations) or (None, None) on error.
    try:
        with open(RUSSIAN_FILE_NAME, "r", encoding="utf-8") as f_rus, \
             open(ENGLISH_FILE_NAME, "r", encoding="utf-8") as f_eng:
            russian_words = [line.strip() for line in f_rus if line.strip()]
            english_translations = [
                line.strip() for line in f_eng if line.strip()
            ]
        return russian_words, english_translations
    except FileNotFoundError:
        # This case should ideally be handled by create_demo_files_if_not_exist
        # but kept as a safeguard.
        print(f"Не удалось открыть файлы '{RUSSIAN_FILE_NAME}' или "
              f"'{ENGLISH_FILE_NAME}'.")
        return None, None
    except Exception as e:
        print(f"Произошла ошибка при чтении файлов: {e}")
        return None, None


def validate_vocabulary(russian_words, english_translations):
    # Validates loaded vocabulary. Returns True if valid, False otherwise.
    if russian_words is None or english_translations is None:
        # Error already printed by load_vocabulary
        return False

    if not russian_words or not english_translations:
        print("Один из файлов пуст или оба пусты. Тестирование невозможно.")
        return False

    if len(russian_words) != len(english_translations):
        print("Количество слов в файлах не совпадает. "
              "Проверьте содержимое файлов.")
        print(f"Русских слов: {len(russian_words)}, "
              f"Английских переводов: {len(english_translations)}")
        return False
    return True


def run_test(russian_words, english_translations):
    # Conducts the vocabulary test.
    correct_answers_count = 0
    total_questions_count = len(russian_words)

    print("\n--- Начинаем тест на знание слов ---")
    print("Введите английский перевод для каждого русского слова.")
    print("Если хотите пропустить слово, просто нажмите Enter.")

    for i in range(total_questions_count):
        rus_word = russian_words[i]
        correct_translation = english_translations[i]

        user_answer = input(
            f"Русское слово: '{rus_word}'. Ваш перевод: ").strip()

        if not user_answer:  # User skips the word
            print(f"Пропущено. Правильный ответ был: '{correct_translation}'")
            print("-" * 30)  # Increased separator length
            continue

        user_answer_cleaned = user_answer.lower()
        correct_translation_cleaned = correct_translation.lower()

        if user_answer_cleaned == correct_translation_cleaned:
            print("Верно!")
            correct_answers_count += 1
        else:
            print(f"Неверно. Правильный ответ: '{correct_translation}'")
        print("-" * 30)  # Increased separator length

    return correct_answers_count, total_questions_count


def display_results(correct_answers_count, total_questions_count):
    # Displays the test results and grade.
    print("\n--- Тест завершен ---")
    print(f"Всего вопросов: {total_questions_count}")
    print(f"Правильных ответов: {correct_answers_count}")

    if total_questions_count > 0:
        percentage = (correct_answers_count / total_questions_count) * 100
        print(f"Процент правильных ответов: {percentage:.2f}%")

        if percentage == 100:
            grade = 5
            comment = "Отлично!"
        elif percentage >= 80:
            grade = 4
            comment = "Хорошо!"
        elif percentage >= 60:
            grade = 3
            comment = "Удовлетворительно."
        elif percentage >= 40:  # Adjusted threshold for grade 2
            grade = 2
            comment = "Неудовлетворительно, нужно подучить."
        else:
            grade = 1  # Or consider 2 as the lowest pass/fail grade
            comment = "Очень плохо, срочно учить слова!"
        print(f"Ваша оценка: {grade} ({comment})")
    else:
        print("Тест не содержал вопросов (возможно, файлы были пусты).")


def task_5_vocabulary_tester():
    if not create_demo_files_if_not_exist():
        print("Не удалось подготовить файлы для теста. Завершение.")
        return

    russian_words, english_translations = load_vocabulary()

    if not validate_vocabulary(russian_words, english_translations):
        print("Проверка словарных файлов не пройдена. Завершение.")
        return

    correct_answers, total_questions = run_test(russian_words,
                                                english_translations)
    display_results(correct_answers, total_questions)


if __name__ == '__main__':
    print("--- Задача 5: Тестирование словарного запаса ---")
    task_5_vocabulary_tester()
