

def text_reverser(text):
    t_text = ''
    for words in text.split():
        t_letter = ''
        t_word = list(words)
        t_n = 0
        for i, letters in enumerate(list(words)):
            n = i
            if not letters.isalpha():
                t_n -= 1
                continue
            else:
                while not t_word[len(t_word) - 1 - i - t_n].isalpha():
                    t_n += 1
                t_word[i] = words[len(t_word) - 1 - i - t_n]
        t_text += ' ' + ''.join(t_word)
    return t_text


print(text_reverser("abcd efgh"), text_reverser("a1bcd efg!h"))

if __name__ == '__main__':
    cases = [("abcd efgh", "dcba hgfe"),
             ("a1bcd efg!h", "d1cba hgf!e"),
             ]
    for text, reversed_text in cases:
        assert text_reverser(text) == reversed_text
