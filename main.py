def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)
        num_of_words = count_word(file_content)
        print("Number of words:", num_of_words)
        letter_dict = count_letter(file_content)
        print("Letter dict:", letter_dict)
        print_report(num_of_words, letter_dict)

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

def sort_elem(el):
    return el[1]

def print_report(num_of_words, letter_dict):
    print(f"{num_of_words} words found in the document\n")
    letter_list = []
    for key in letter_dict:
        if key.isalpha():
            letter_list.append((key, letter_dict[key]))
    letter_list.sort(reverse=True, key=sort_elem)
    for letter in letter_list:
        print(f"The '{letter[0]}' character was found {letter[1]} times")

    print("--- End Report ---")


main()
