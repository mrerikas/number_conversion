import unittest
from converter import convertNumberToEnglishText

class ConverterNumberToEnglishTest(unittest.TestCase):

    def test_print_negative_one(self):
        self.assertEqual(convertNumberToEnglishText(-1), 'negative one')
  
    def test_print_zero_for_0(self):
        self.assertEqual(convertNumberToEnglishText(0), 'zero')

    def test_print_zero_for_negative_0(self):
        self.assertEqual(convertNumberToEnglishText(-0), 'zero')

    def test_print_nineteen_for_19(self):
        self.assertEqual(convertNumberToEnglishText(19), 'nineteen')

    def test_print_twenty_for_20(self):
        self.assertEqual(convertNumberToEnglishText(20), 'twenty')

    def test_print_correctly_for_41(self):
        self.assertEqual(convertNumberToEnglishText(41), 'forty one')

    def test_print_correctly_for_100(self):
        self.assertEqual(convertNumberToEnglishText(100), 'one hundred')

    def test_print_correctly_for_101(self):
        self.assertEqual(convertNumberToEnglishText(101), 'one hundred one')

    def test_print_correctly_for_739(self):
        self.assertEqual(convertNumberToEnglishText(739), 'seven hundred thirty nine')

    def test_print_correctly_for_1234(self):
        self.assertEqual(convertNumberToEnglishText(1234), 'one thousand two hundred thirty four')

    def test_print_correctly_for_10000(self):
        self.assertEqual(convertNumberToEnglishText(10000), 'ten thousand')

    def test_print_correctly_for_60019(self):
        self.assertEqual(convertNumberToEnglishText(60019), 'sixty thousand nineteen')

    def test_print_correctly_for_67567(self):
        self.assertEqual(convertNumberToEnglishText(67567), 'sixty seven thousand five hundred sixty seven')

    def test_print_correctly_for_99999(self):
        self.assertEqual(convertNumberToEnglishText(99999), 'ninety nine thousand nine hundred ninety nine')
   
if __name__ == '__main__':
    unittest.main()
