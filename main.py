def main():
    print_book_report("books/frankenstein.txt")

def print_book_report(file):
    txt = get_text_from_file(file)
    print("--- Begin report of {file} ---")
    print(f"{count_words(txt)} words found in the document")
    print("")
    letters = count_letters(txt)
    for l in letters:
        if not l.isalpha():
            continue
        print(f"The '{l}' character was found {letters[l]} times")
    print("--- End report ---")

def get_text_from_file(file):
    with open(file) as f:
        return f.read()

def count_words(txt):
    return len(txt.split())

def count_letters(txt):
    raw = {}
    for l in txt.lower():
        if not l in raw:
            raw[l] = 1
        else:
            raw[l] += 1
    tosort = []
    for l in raw:
        if not l.isalpha():
            continue
        tosort.append({
            "letter": l,
            "num": raw[l]
        })
    tosort.sort(reverse=True, key=sort_on_letter)
    out = {}
    for l in tosort:
        out[l["letter"]] = l["num"]
    return out

def sort_on_letter(dict):
    return dict["num"]

main()