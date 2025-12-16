def count_words(input: str):
    words = input.split();
    return len(words)

def count_character_occurance(input: str):
    stats = {}
    normalised = input.lower()
    characters = list(normalised)
    for x in characters:
        stats[x] = stats.get(x, 0) + 1
    return stats

def sorted_list_stats(stats: dict):
    result = []
    for i in sorted(stats.items(), key=lambda x:x[1], reverse=True):
        result.append({"char": i[0], "num": i[1]})
    return result

