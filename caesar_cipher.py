from string import ascii_lowercase
def caesar_cipher(string, num):
    '''
    :param string: string of letters
    :param num: number of shifting
    :return: shifted string
    '''
    shifted_str = ''
    letters = list(ascii_lowercase)

    for letter in string.lower():
        idx = letters.index(letter) + num
        if  idx > 25:
            idx -= 26
        shifted_str += letters[idx]

    return shifted_str

if __name__ == '__main__':
    print(caesar_cipher('xyzABC', 3))
