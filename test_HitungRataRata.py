import unittest
from HitungRataRata import hitung_rata_rata

# ! Cara run php test: python -m unittest test_HitungRataRata

class TestHitungRataRata(unittest.TestCase):
    def test_hitung_rata_rata(self):
        nilai1 = [80, 90, 75, 60, 85]
        hasil1 = hitung_rata_rata(nilai1)
        self.assertEqual(hasil1, 78, 'Test case 1: Rata-rata dari nilai-nilai')

        nilai2 = [100, 100, 100, 100]
        hasil2 = hitung_rata_rata(nilai2)
        self.assertEqual(hasil2, 100, 'Test case 2: Rata-rata dari nilai-nilai yang sama')

        nilai3 = []
        hasil3 = hitung_rata_rata(nilai3)
        self.assertEqual(hasil3, 0, 'Test case 3: Rata-rata dari array kosong')

if __name__ == '__main__':
    unittest.main()

"""
    Jika Anda menjalankan unit test yang disediakan, maka Anda akan mendapatkan hasil berikut:
    Test case 1: Rata-rata dari nilai-nilai
    Hasil yang diharapkan: 78
    Test case 2: Rata-rata dari nilai-nilai yang sama
    Hasil yang diharapkan: 100
    Test case 3: Rata-rata dari array kosong
    Hasil yang diharapkan: 0
"""