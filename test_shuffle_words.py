import unittest
from unittest.mock import mock_open, patch

from shuffle_words import main

TEST_TEXT = '''"Some!" words, ĄŃĘŻB\n
Newline and additional words
Last Line.'''


def shuffle(letters):
    return letters.insert(0, letters.pop(-1))


class ShuffleWordsTests(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data=TEST_TEXT)
    def test_shuffleWords_SHOULD_returnCorrectOutput(self, mock_open):
        expected_text = '''"Smoe!" wdors, ĄŻŃĘB\n
Nnewlie and aadditionl wdors
Lsat Lnie.'''

        with patch('random.shuffle', shuffle):
            out = main('test_filename')

        self.assertEqual(out, expected_text)


if __name__ == '__main__':
    unittest.main()
