"""
 * Buatlah sebuah fungsi Python yang menerima sebuah array nilai numerik dan menghitung rata-rata nilai dari array tersebut.
 * Contoh:
 * Input: [80, 90, 75, 60, 85]
 * Output: 78
"""

def hitung_rata_rata(nilai):
    total = sum(nilai)
    jumlah = len(nilai)
    if jumlah > 0:
        return round(total / jumlah)
    else:
        return 0
