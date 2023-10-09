import unittest
from CariBilanganGenap import cari_bilangan_genap

# ! Cara run php test: python -m unittest test_CariBilanganGenap

class TestCariBilanganGenap(unittest.TestCase):
    def test_cari_bilangan_genap(self):
        array1 = [5, 2, 8, 1, 6]
        hasil1 = cari_bilangan_genap(array1)
        self.assertEqual(hasil1, [2, 8, 6], 'Test case 1: Array dengan beberapa bilangan genap')

        array2 = [1, 3, 5, 7]
        hasil2 = cari_bilangan_genap(array2)
        self.assertEqual(hasil2, [], 'Test case 2: Array tanpa bilangan genap')

        array3 = [10, 20, 30, 40]
        hasil3 = cari_bilangan_genap(array3)
        self.assertEqual(hasil3, [10, 20, 30, 40], 'Test case 3: Array dengan semua bilangan genap')

if __name__ == '__main__':
    unittest.main()

"""
    Jika Anda menjalankan unit test yang disediakan, maka Anda akan mendapatkan hasil berikut:
    Test case 1: Array dengan beberapa bilangan genap
    Hasil yang diharapkan: [2,8,6]
    Test case 2: Array tanpa bilangan genap
    Hasil yang diharapkan: []
    Test case 3: Array dengan semua bilangan genap
    Hasil yang diharapkan: [10, 20, 30, 40]
"""