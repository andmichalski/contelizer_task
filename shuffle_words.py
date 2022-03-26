import argparse
import random
import string


def shuffle_word(word):
    if word != '\n':
        letters = word.strip(string.punctuation + '\n')
        letters_inside = list(letters[1:-1])
        random.shuffle(letters_inside)
        new_letters = letters[0] + ''.join(letters_inside) + letters[-1]
        return word.replace(letters, new_letters)
    else:
        return word


def main(filename):

    with open(filename) as f:
        input = f.readlines()

    output = []

    for line in input:
        words = line.split(' ')
        shuffled_words = [shuffle_word(word) for word in words]
        new_line = ' '.join(shuffled_words)
        output.append(new_line)

    new_text = ''.join(output)

    with open("copy_" + filename, 'w') as f:
        f.write(new_text)
    return new_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='File name of text to process')
    args = parser.parse_args()
    main(args.filename)
