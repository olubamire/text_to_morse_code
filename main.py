morse=True
morse_code_dict= {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


while morse:

    word = []

    text=input('Enter the text that will be convert to morse code: ').upper()

    for letter in text:
        if letter in morse_code_dict:
            word.append(morse_code_dict[letter])
        else:
         word.append(f"{letter}")


    text_join=' '.join(word)
    print(f'The morse code for {text} is {text_join}')

    repeat_morse=input('Do you wan to repeat morse Yes or No : ').lower()

    if repeat_morse == 'yes' :
        print('\n\n')
        morse=True

    else:
     print('\n\n Good bye 🖐')
     morse=False
