def analyze_text(text):
    count = 0
    letter_count = 0
    for char in text:
        if char.isalpha():
            count += 1
    for e in text:
        if e == "e" or e == "E":
            letter_count += 1
        p = float(letter_count)/float(count) * 100
    output = "The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'."
    print(output.format(count, letter_count, p))