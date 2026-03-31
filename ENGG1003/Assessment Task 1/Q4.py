# Part a

def word_count(speech):
    return len(speech.split(" "))


# Part b

def vowel_words(speech):
    vowel_count = 0
    for i in range(word_count(speech)):
        words = speech[i]
        if words[0] == ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_count += 1
        i += 1

    return vowel_count

# Part c

def um_count(speech):
    um_count = 0
    for i in range(word_count(speech):
        word = speech[i]
        if word = 'um':
            um_count += 1
        i += 1

    return um_count

# Part d

def num_breaths(speech):
    breaths = 0
    for i in range(word_count(speech):
        word = speech[i]
        if word = [',', '.', '?', '!']:
            breaths += 1
        i += 1

    return breaths

# Part e

def most_common_word(speech):
    return "one of them"