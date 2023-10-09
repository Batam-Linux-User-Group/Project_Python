import unittest
from HitungKata import hitung_kata

# ! Cara run php test: python -m unittest test_HitungKata

class TestHitungKata(unittest.TestCase):
    def test_hitung_kata_kalimat_kosong(self):
        hasil = hitung_kata(' ')
        self.assertEqual(hasil, 0, 'Test case 1: Kalimat kosong')

    def test_hitung_kata_satu_kata(self):
        hasil = hitung_kata('Halo')
        self.assertEqual(hasil, 1, 'Test case 2: Kalimat dengan satu kata')

    def test_hitung_kata_beberapa_kata(self):
        hasil = hitung_kata('Halo nama saya Galih')
        self.assertEqual(hasil, 4, 'Test case 3: Kalimat dengan beberapa kata')

    def test_hitung_kata_karakter_khusus(self):
        hasil = hitung_kata('Ini, kalimat dengan tanda baca!')
        self.assertEqual(hasil, 5, 'Test case 4: Kalimat dengan karakter khusus')

    def test_hitung_kata_spasi_ganda(self):
        hasil = hitung_kata('Ini   kalimat   dengan   spasi   ganda')
        self.assertEqual(hasil, 5, 'Test case 5: Kalimat dengan spasi ganda')

if __name__ == '__main__':
    unittest.main()

"""
    Jika Anda menjalankan unit test yang disediakan, maka Anda akan mendapatkan hasil berikut:
    Test case 1: Kalimat kosong
    Hasil yang diharapkan: 0
    Test case 2: Kalimat dengan satu kata
    Hasil yang diharapkan: 1
    Test case 3: Kalimat dengan beberapa kata
    Hasil yang diharapkan: 4
    Test case 4: Kalimat dengan karakter khusus
    Hasil yang diharapkan: 5
    Test case 5: Kalimat dengan spasi ganda
    Hasil yang diharapkan: 5
"""
