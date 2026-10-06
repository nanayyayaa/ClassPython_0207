class PersegiPanjang:
    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar == 0:
            raise ValueError("Nilai panjang dan lebar tidak boleh 0!")
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    