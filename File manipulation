def count_word_occurrences(filename):
    word_counts = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()  # Convert to lowercase for case-insensitive counting
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def display_word_counts(word_counts):
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[0])
    for word, count in sorted_counts:
        print(f'{word}: {count}')


filename = input("enter the file name with .txt extension :")

word_counts = count_word_occurrences(filename)
display_word_counts(word_counts)
