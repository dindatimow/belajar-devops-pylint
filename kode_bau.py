"""Modul contoh untuk pengujian Pylint."""


def hitung_penjumlahan(angka_satu, angka_dua):
    """Menghitung penjumlahan dua angka."""
    hasil = angka_satu + angka_dua
    print(hasil)
    return hasil


if __name__ == "__main__":
    hitung_penjumlahan(1, 2)
