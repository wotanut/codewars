def reverse_words(text):
    reversed = ""

    for word in text.split(" "):
        reversed += reverse_string(word) + " "

    reversed = reversed[:-1]

    print(reversed)
    return reversed

def reverse_string(word: str):
    reversed = ""

    for i in range(len(word)):
        reversed = word[i] + reversed
    
    return reversed

reverse_words("This is an example!")
reverse_words("double  spaces")