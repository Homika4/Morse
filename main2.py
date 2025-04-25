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

word_alphabet = {v: k for k, v in morse_alphabet.items()}




# Morse code sentence to decode
morse_to_translate = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

# Split Morse code into words using " / " as the delimiter
words = morse_to_translate.split(' / ')
print(f'words : {words}')
translated_words = []

for word in words:
    # Split each word into Morse letters
    letters = word.split(' ')
    # Translate each letter using the reversed dictionary
    translated_word = ''.join(word_alphabet.get(letter, '?') for letter in letters)
    # Append the translated word to the list
    translated_words.append(translated_word)

# Join all translated words with a space to form the final sentence
mot = ' '.join(translated_words)

print("Translated Text:", mot)