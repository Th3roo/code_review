import os

RUSSIAN_FILE_PATH = "russian_words.txt"
ENGLISH_FILE_PATH = "english_words.txt"


def load_word_pairs(rus_path, eng_path):
    """Loads word pairs from Russian and English vocabulary files."""
    try:
        with open(rus_path, 'r', encoding='utf-8') as rf, \
             open(eng_path, 'r', encoding='utf-8') as ef:
            russian_words = [line.strip() for line in rf if line.strip()]
            english_words = [line.strip() for line in ef if line.strip()]
    except FileNotFoundError:
        print(
            f"Ошибка: Один или оба файла не найдены ('{rus_path}', '{eng_path}')."
        )
        print(
            "Убедитесь, что файлы находятся в том же каталоге, что и скрипт, или укажите правильный путь."
        )
        return None
    except IOError as e:
        print(f"Ошибка чтения файлов: {e}")
        return None

    if len(russian_words) != len(english_words):
        print("Ошибка: Количество слов в файлах не совпадает. "
              "Проверьте содержимое файлов.")
        print(
            f"Русских слов: {len(russian_words)}, Английских: {len(english_words)}"
        )
        return None

    if not russian_words:  # Handles if both files are empty and len matches (0==0)
        print("Файлы словарей пусты. Нет слов для тестирования.")
        return None

    return list(zip(russian_words, english_words))


def conduct_vocabulary_test(word_pairs_list):
    """Conducts the vocabulary test for the given word pairs."""
    if not word_pairs_list:
        # This case should be caught by load_word_pairs, but as a safeguard
        print("Нет слов для проведения теста.")
        return 0, 0  # correct_answers, total_questions

    correct_answers = 0
    total_questions = len(word_pairs_list)

    print("\n--- Начинаем тест на знание слов ---")
    print("Введите английский перевод для каждого русского слова.")
    print("Чтобы пропустить слово, просто нажмите Enter.")

    for i, (russian_word, english_word) in enumerate(word_pairs_list):
        print(f"\nВопрос {i+1}/{total_questions}")
        print(f"Переведите на английский: {russian_word}")
        user_translation = input("Ваш перевод: ").strip()

        if not user_translation:
            print(f"Пропущено. Правильный ответ был: {english_word}")
            continue

        if user_translation.lower() == english_word.lower():
            print("Верно!")
            correct_answers += 1
        else:
            print(f"Неверно. Правильный ответ: {english_word}")

    return correct_answers, total_questions


def display_test_results(correct_answers, total_questions):
    """Displays the results and grade for the test."""
    if total_questions == 0:
        print("\nТест не содержал вопросов.")
        return

    score_percentage = (correct_answers / total_questions) * 100

    # Оценивание
    if score_percentage >= 90:
        grade_text = "Отлично"
    elif score_percentage >= 75:
        grade_text = "Хорошо"
    elif score_percentage >= 50:
        grade_text = "Удовлетворительно"
    else:
        grade_text = "Неудовлетворительно"

    print(
        f"\n--- Тест завершен ---"
        f"\nВы ответили правильно на {correct_answers} из {total_questions} вопросов."
    )
    print(f"Ваша оценка: {grade_text} ({score_percentage:.2f}%)")


def main():
    """Main function to run the vocabulary tester."""
    print("--- Тестирование словарного запаса ---")

    # Determine the directory of the script
    script_dir = os.path.dirname(__file__) if '__file__' in locals() else '.'
    # Construct absolute paths to the vocabulary files
    abs_rus_path = os.path.join(script_dir, RUSSIAN_FILE_PATH)
    abs_eng_path = os.path.join(script_dir, ENGLISH_FILE_PATH)

    word_pairs = load_word_pairs(abs_rus_path, abs_eng_path)

    if word_pairs is None:
        print("Не удалось загрузить слова для теста. Завершение.")
        return

    correct, total = conduct_vocabulary_test(word_pairs)
    display_test_results(correct, total)


if __name__ == "__main__":
    main()
