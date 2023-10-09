"""
 * Buatlah sebuah fungsi Python yang menerima sebuah array bilangan bulat dan mengembalikan semua bilangan genap yang ada dalam array tersebut dalam bentuk array baru.
 * Contoh:
 * Input: [5, 2, 8, 1, 6]
 * Output: [2, 8, 6]
"""

def cari_bilangan_genap(array):
    bilangan_genap = [bilangan for bilangan in array if bilangan % 2 == 0]
    return bilangan_genap
