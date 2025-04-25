morse_alphabet = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

    " ": "/",  # Space between words in Morse Code
    ".": ".-.-.-",  # Period
    ",": "--..--",  # Comma
    "?": "..--..",  # Question mark
    "'": ".----.",  # Apostrophe
    "!": "-.-.--",  # Exclamation mark
    "/": "-..-.",  # Slash
    "(": "-.--.",  # Open parenthesis
    ")": "-.--.-",  # Close parenthesis
    "&": ".-...",  # Ampersand
    ":": "---...",  # Colon
    ";": "-.-.-.",  # Semicolon
    "=": "-...-",  # Equals sign
    "+": ".-.-.",  # Plus
    "-": "-....-",  # Minus or hyphen
    "_": "..--.-",  # Underscore
    "\"": ".-..-.",  # Quotation mark
    "$": "...-..-",  # Dollar sign
    "@": ".--.-.",  # At symbol (@)
    "#": "......"  # Placeholder (not standard in Morse but could be customized)
}


# text_to_decode = input("Word to encode")
text_to_decode = input("Morse word to encode\n").upper()
morse = ""
for word in text_to_decode:
    morse += (morse_alphabet[word])

print(morse)
print(morse_alphabet)