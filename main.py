from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
print(__name__)

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

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/translate", methods=["POST"])
def translate():
    morse = ""
    text_to_translate = request.form.get('translate').upper()

    for word in text_to_translate:
        morse += " " + (morse_alphabet[word])
    return render_template('index.html', code=morse, word=text_to_translate)


@app.route("/untranslate", methods=["POST"])
def untranslate():
    morse_to_translate = request.form.get('untranslate', '')
    mot = ""

    # Split Morse code into words using " / " as the delimiter
    words = morse_to_translate.split(' / ')
    translated_words = []

    for word in words:
        # Split each word into Morse letters
        letters = word.split(' ')
        # Translate each letter using the reversed dictionary
        translated_word = ''.join(word_alphabet.get(letter, '?') for letter in letters)
        # Append the translated word to the list
        translated_words.append(translated_word)

    # Join all translated words with a space
    mot = ' '.join(translated_words)

    return render_template('index.html', mot=mot)




if __name__ == "__main__":
    app.run()