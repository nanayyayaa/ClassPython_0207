class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar == 0:
            raise ValueError("Nilai panjang dan lebar tidak boleh 0!")
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return "persegi panjang, panjang " + str(self.panjang) + " cm, dan lebar " + str(self.lebar) + " cm"

# Test
tugas_kotak = PersegiPanjang(3, 2)
print(tugas_kotak)
print("Keliling :", tugas_kotak.hitung_keliling(), "cm")
print("Luas     :", tugas_kotak.hitung_luas(), "cm persegi")

try:
    print("\n-- Mencoba masukin angka 0 --")
    kotak_error = PersegiPanjang(0, 5)
except ValueError as pesan_error:
    print("Error berhasil ditangkap:", pesan_error)
    