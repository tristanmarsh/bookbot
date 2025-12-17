import sys
from stats import count_words, count_character_occurance, sorted_list_stats


def get_file_path():
    try:
        path = sys.argv[1]
        return path
    except Exception as error:
        print("Error: Invalid argument, please provide path to .txt file to analyse")
        print("Usage: python3 main.py <path_to_book>")
        print(error)


def get_book_text(path: str):
    try:
        with open(path) as f:
            contents = f.read()
            return contents
    except Exception as error:
        print(
            "Error: Unable to read book, please confirm the book is at the provided path"
        )
        print(error)


def format_report(file_path: str, word_count: str, formatted_character_stats: str):
    return (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {file_path}...\n"
        "----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        "--------- Character Count -------\n"
        f"{formatted_character_stats}\n"
        "============= END ==============="
    )


def main():
    file_path = get_file_path()
    if not file_path:
        exit(1)
    text = get_book_text(file_path)
    word_count = count_words(text)
    stats = count_character_occurance(text)
    filtered = list(filter(lambda x: x["char"].isalpha(), sorted_list_stats(stats)))
    formatted_character_stats = "\n".join(
        map(lambda x: f"{x['char']}: {x['num']}", filtered)
    )
    report = format_report(file_path, word_count, formatted_character_stats)
    print(report)
    sys.exit(0)


main()
