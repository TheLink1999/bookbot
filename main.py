def character_counts(content):
    stat = {}
    content = content.lower()

    for char in content:
        if char not in stat:
            stat[char]  = 1
        else:
            stat[char] += 1
    return stat

def word_counts(content):
    return len(content.split())

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counts(file_contents)} words found in the document")
    print("")

    for k,v in character_counts(file_contents).items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    else:
        print("--- End report ---")

