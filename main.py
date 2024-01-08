def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)
        num_of_words = count_word(file_content)
        print("Number of words:", num_of_words)
        letter_dict = count_letter(file_content)
        print("Letter dict:", letter_dict)

def count_word(content):
    words = content.split()
    return len(words)

def count_letter(content):
    letter_dict = {}
    content_without_whitespace = content.strip()
    for char in content_without_whitespace:
        lowercase_char = char.lower()
        if lowercase_char not in letter_dict:
            letter_dict[lowercase_char] = 1
        else:
            letter_dict[lowercase_char] += 1
    return letter_dict
        

main()
