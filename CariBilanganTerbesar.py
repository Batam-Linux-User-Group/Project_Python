"""
 * Buatlah sebuah fungsi Python yang menerima sebuah array bilangan bulat dan mengembalikan bilangan terbesar dalam array tersebut.
 * Contoh:
 * Input: [5, 8, 2, 10, 3]
 * Output: 10
"""

def cari_bilangan_terbesar(array):
    terbesar = array[0] if array else None  # Anggap elemen pertama sebagai terbesar awalnya
    for bilangan in array:
        if bilangan > terbesar:
            terbesar = bilangan  # Jika bilangan lebih besar, perbarui nilai terbesar
    return terbesar
