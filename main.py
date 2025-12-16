from stats import count_words, count_character_occurance, sorted_list_stats 

def get_book_text():
  with open('./books/frankenstein.txt') as f:
    contents = f.read()
    return contents
  

def format_report(word_count: str, formatted_character_stats: str):
  return (
    "============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------\n"
    f"Found {word_count} total words\n"
    "--------- Character Count -------\n"
    f"{formatted_character_stats}\n"
    "============= END ==============="
  )

def main():
  text = get_book_text()
  word_count = count_words(text)
  stats = count_character_occurance(text)
  filtered = list(filter(lambda x: x['char'].isalpha(), sorted_list_stats(stats)))
  formatted_character_stats = "\n".join(map(lambda x: f"{x['char']}: {x['num']}", filtered))
  report = format_report(word_count, formatted_character_stats)
  print(report)
  
main()
