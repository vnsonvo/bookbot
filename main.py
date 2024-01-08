def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)
        num_of_words = count_word(file_content)
        print("Number of words:", num_of_words)

def count_word(content):
    words = content.split()
    return len(words)

main()