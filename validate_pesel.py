import argparse
import re


def validate(pesel: str):
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    results = []
    for i, number in enumerate(pesel[:-1]):
        results.append(int(number) * multipliers[i])

    control_number = 10 - (sum(results) % 10)
    if control_number == 10:
        control_number = 0

    if control_number == int(pesel[-1]):
        return True
    else:
        raise ValueError('Not correct PESEL ID')


def main(pesel):
    if re.match(r"^\d{11}$", pesel):
        out = validate(pesel)
        return out
    else:
        raise ValueError('Not correct length or non number character exist!!!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pesel', help='PESEL number')
    args = parser.parse_args()
    out = main(args.pesel)
    if out:
        print('Validation successfull !!!')
