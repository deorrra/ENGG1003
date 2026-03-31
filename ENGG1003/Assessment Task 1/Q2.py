def char_to_num(ch):
    if type(ch) is not str or len(ch) != 1:
        raise Exception(f"Incorrect usage of char_to_num. Expect a single character but got {ch} of type: {type(ch)}")

    ascii_char = ord(ch)

    if ascii_char < ord("a") or ascii_char > ord("z"):
        raise Exception(f"Incorrect usage of char_to_num. We expect the character to be a letter from a to z.Received: {ch}")

    return ord(ch) - ord("a") + 1

def num_to_char(num):
    if type(num) is not int or num < 0:
        raise Exception(f"Incorrect usage of num_to_char. We expect a positive integer. Received: {num}")

    return chr(((num - 1) % 26) + ord("a"))

# The method of ‘encryption’ for a single character is as follows:
# 1. If the character when converted to a number is divisible by 2 then multiply the number by 8.
# 2. If the character when converted to a number is divisible by 3 then add 101 to the number.
# 3. If the character when converted to a number is divisible by both 2 and 3 then multiply the number by 17.
# 4. Convert this number back to a character. This is the new ‘encrypted’ character.

# Part a

def encrypt_char(ch):
    if char_to_num(ch) / 2 == int and char_to_num(ch) / 3 == int:
        ch = char_to_num(ch) * 17
    elif char_to_num(ch) / 2 == int:
        ch = char_to_num(ch) * 8
    elif char_to_num(ch) / 3 == int:
        ch = char_to_num(ch) + 101
    else:
        ch = char_to_num(ch)

    return num_to_char(ch)



# Part b

def decrypt_word(word):
     return word

