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