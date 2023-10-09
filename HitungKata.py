"""
 * Buatlah sebuah fungsi Javascript yang bernama hitungKata($kalimat) yang akan menerima satu parameter berupa string $kalimat. 
 * Fungsi ini harus mengembalikan jumlah kata dalam kalimat tersebut. 
 * Kata-kata dalam kalimat akan dipisahkan oleh spasi.
 * Contoh:
 * Input: "Halo nama saya Galih"
 * Output: 4
"""

def hitung_kata(kalimat):
    # Menghapus spasi berlebihan dan karakter whitespace di awal dan akhir kalimat
    kalimat = kalimat.strip()

    # Memecah kalimat menjadi kata-kata berdasarkan spasi
    kata_kata = kalimat.split()

    # Menghitung jumlah kata dengan memeriksa setiap kata
    jumlah_kata = len(kata_kata)

    return jumlah_kata
