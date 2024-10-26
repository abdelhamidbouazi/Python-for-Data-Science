import sys


def is_alnum_space(string):
    """check if the string contain alnum and spaces only"""
    for char in string:
        if not (char.isalnum() or char.isspace()):
            return False
    return True

def main(argv):
    """
    returns the elements that have length greater or equal
    to the length given by user
    """
    NESTED_MORSE = {
        ' ': '/ ',
        'A': '.- ',      'B': '-... ',    'C': '-.-. ',    'D': '-.. ',
        'E': '. ',       'F': '..-. ',    'G': '--. ',     'H': '.... ',
        'I': '.. ',      'J': '.--- ',    'K': '-.- ',     'L': '.-.. ',
        'M': '-- ',      'N': '-. ',      'O': '--- ',     'P': '.--. ',
        'Q': '--.- ',    'R': '.-. ',     'S': '... ',      'T': '- ',
        'U': '..- ',     'V': '...- ',    'W': '.-- ',     'X': '-..- ',
        'Y': '-.-- ',    'Z': '--.. ',
        '1': '.---- ',   '2': '..--- ',   '3': '...-- ',   '4': '....-' , 
        '5': '..... ',   '6': '-.... ',    '7': '--... ',    '8': '---.. ',
        '9': '----. ',   '0': '----- ',
    }
    try:
        assert len(argv) == 2, "the arguments are bad"
        assert is_alnum_space(argv[1]), "the arguments are bad"
        
        inp =  argv[1].upper()
        res = ''
        for c in inp :
            if c in NESTED_MORSE:
                res +=  NESTED_MORSE[c]
        print(res.rstrip())
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main(sys.argv)