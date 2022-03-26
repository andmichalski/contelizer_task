import unittest

from validate_pesel import main


class ValidatePeselTests(unittest.TestCase):

    def test_validatePesel_SHOULD_raiseValueError_WHEN_numberIsTooShort(self):
        input_pesel = '8209215285'

        with self.assertRaises(ValueError) as e:
            main(input_pesel)

        self.assertEqual(str(e.exception), 'Not correct length or non number character exist!!!')

    def test_validatePesel_SHOULD_raiseValueError_WHEN_numberIsTooLong(self):
        input_pesel = '820921528589'

        with self.assertRaises(ValueError) as e:
            main(input_pesel)

        self.assertEqual(str(e.exception), 'Not correct length or non number character exist!!!')

    def test_validatePesel_SHOULD_raiseValueError_WHEN_notNumbersInId(self):
        input_pesel = '82092152A58'

        with self.assertRaises(ValueError) as e:
            main(input_pesel)

        self.assertEqual(str(e.exception), 'Not correct length or non number character exist!!!')

    def test_validatePesel_SHOULD_raiseValueError_WHEN_numberIsIncorrect(self):
        input_pesel = '48030546298'

        with self.assertRaises(ValueError) as e:
            main(input_pesel)

        self.assertEqual(str(e.exception), 'Not correct PESEL ID')

    def test_validatePesel_SHOULD_returnTrue_WHEN_peselIdIsCorrect(self):
        pesel_ids = [
            "00302859168",
            "82092152854",
            "69091875991",
            "00262318613",
            "04233163583",
            "48030546299",
            "49070732891",
            "76020895586",
            "99121766339",
            "98082298798"
        ]

        for pesel in pesel_ids:
            with self.subTest(pesel=pesel):
                out = main(pesel)
                self.assertTrue(out)


if __name__ == '__main__':
    unittest.main()
