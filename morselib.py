# Define the Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
    return morse_code.strip()

def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_code_dict.items():
            if code == morse:
                text += char
                break
    return text

# Example usage
input_text = input("Enter text or Morse code: ")
if input_text[0] in ['.', '-']:
    translated_text = morse_to_text(input_text)
else:
    translated_text = text_to_morse(input_text)
print("Translated text:", translated_text)
