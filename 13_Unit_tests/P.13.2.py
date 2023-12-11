# -----------------------------------------------
# P.13.2
# -----------------------------------------------
# • Perdaryti 5 pamokos programą su klase Sakinys taip, kad:
#   • Visos funkcijos grąžintų duomenis (dabar kai kurios funkcijos tik
#     atspausdina reikšmes).
#   • Testavimui būtų sukurtas setUp() metodas, kuriame būtų inicijuotas klasės
#     objektas.
#   • Būtų sukurti UNIT testai visoms funkcijoms (kiekvienai funkcijai turėtų
#     būti mažiausiai 3 patikrinimai).
#   • Kodas būtų maksimaliai patobulintas, nuolatos vis leidžiant sukurtus UNIT
#     testus tam pasiekti.
# -----------------------
# English description will be added.
# -----------------------------------------------

import unittest
from test_P5_1 import Text


class TestText(unittest.TestCase):

    def setUp(self):
        self.object = Text('Zen of Python 123')

    def test_return_text_backwards(self):
        expectation = '321 nohtyP fo neZ'
        is_in = 'hello, wolrd'
        result = self.object.return_text_backwards()
        self.assertEqual(expectation, result)
        self.assertTrue(self.object.return_text_backwards())
        self.assertNotIn(result, is_in)

    def test_return_text_lowercase(self):
        expectation = 'zen of python 123'
        is_in = 'hello, wolrd'
        result = self.object.return_text_lowercase()
        self.assertEqual(expectation, result)
        self.assertTrue(self.object.return_text_lowercase())
        self.assertNotIn(result, is_in)

    def test_return_text_uppercase(self):
        expectation = 'ZEN OF PYTHON 123'
        is_in = 'hello, wolrd'
        result = self.object.return_text_uppercase()
        self.assertEqual(expectation, result)
        self.assertTrue(self.object.return_text_uppercase())
        self.assertNotIn(result, is_in)

    def test_return_index(self):
        expectation = 'Zen'
        is_in = 'Python'
        result = self.object.return_index(0)
        self.assertTrue(expectation, result)
        self.assertTrue(self.object.return_index(0))
        self.assertNotIn(result, is_in)

    def test_count_text_and_characters(self):
        expectation = (4, 17)
        is_in = (1, 5,)
        result = self.object.count_text_and_characters()
        self.assertEqual(expectation, result)
        self.assertTrue(self.object.count_text_and_characters())
        self.assertNotIn(result, is_in)

    def test_text_replace(self):
        expectation = 'hello of Python 123'
        is_in = 'hello, wolrd'
        result = self.object.text_replace('Zen', 'hello')
        self.assertEqual(expectation, result)
        self.assertTrue(self.object.text_replace('Zen', 'hello'))
        self.assertNotIn(result, is_in)

    def test_how_many_words(self):
        expectation = ('Words count: 4', 'Cap letters: 2', 'Low letters: 9', 'Numbers: 3')
        result = self.object.how_many_words()
        self.assertEqual(expectation, result)
        self.assertIsNotNone(expectation, result)
        self.assertTrue(expectation)

if __name__ == '__main__':
    unittest.main()
