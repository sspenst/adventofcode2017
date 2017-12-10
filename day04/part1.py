def valid_passphrase(line):
    wordlist = line.split(" ")
    seen_words = []
    for word in wordlist:
        if word not in seen_words:
            seen_words.append(word)
        else:
            return False
    return True

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")
    total = 0
    for line in lines:
        if valid_passphrase(line):
            total += 1
    print(total)
