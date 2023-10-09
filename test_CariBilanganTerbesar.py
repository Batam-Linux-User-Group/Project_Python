import unittest
from CariBilanganTerbesar import cari_bilangan_terbesar

# ! Cara run Python test: python -m unittest test_CariBilanganTerbesar

class TestCariBilanganTerbesar(unittest.TestCase):
    def test_cari_terbesar(self):
        array1 = [5, 8, 2, 10, 3]
        hasil1 = cari_bilangan_terbesar(array1)
        self.assertEqual(hasil1, 10, 'Test case 1: Array dengan bilangan terbesar di tengah')

        array2 = [22, 12, 8, 4, 18]
        hasil2 = cari_bilangan_terbesar(array2)
        self.assertEqual(hasil2, 22, 'Test case 2: Array dengan bilangan terbesar di awal')

        array3 = [7, 1, 9, 5, 14]
        hasil3 = cari_bilangan_terbesar(array3)
        self.assertEqual(hasil3, 14, 'Test case 3: Array dengan bilangan terbesar di akhir')

if __name__ == '__main__':
    unittest.main()


"""
Jika Anda menjalankan unit test yang disediakan, maka Anda akan mendapatkan hasil berikut:
Test case 1: Array dengan bilangan terbesar di tengah
Hasil yang diharapkan: 10
Test case 2: Array dengan bilangan terbesar di awal
Hasil yang diharapkan: 22
Test case 3: Array dengan bilangan terbesar di akhir
Hasil yang diharapkan: 14
"""
