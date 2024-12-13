class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def display_info(self):
        print(f"Nama: {self.name}")
        print(f"Makanan: {self.makanan}")
        print(f"Hidup: {self.hidup}")
        print(f"Berkembang Biak: {self.berkembang_biak}")

# Kelas Burung
class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis, sayap):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.sayap = sayap

    def terbang(self):
        print(f"{self.name} sedang terbang.")

    def display_info(self):
        super().display_info()
        print(f"Jenis: {self.jenis}")
        print(f"Sayap: {self.sayap}")

# Kelas Ikan
class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, sirip):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.sirip = sirip

    def berenang(self):
        print(f"{self.name} sedang berenang.")

    def display_info(self):
        super().display_info()
        print(f"Habitat: {self.habitat}")
        print(f"Sirip: {self.sirip}")

# Kelas Ular
class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.berbisa = berbisa

    def melata(self):
        print(f"{self.name} sedang melata.")

    def display_info(self):
        super().display_info()
        print(f"Panjang: {self.panjang} meter")
        print(f"Berbisa: {'Ya' if self.berbisa else 'Tidak'}")

# Membuat objek dari masing-masing kelas
if __name__ == "__main__":
    # Objek Burung
    burung1 = Burung("Elang", "Daging", "Udara", "Bertelur", "Raptor", "Lebar")
    burung2 = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Kolumbidae", "Kecil")
    burung3 = Burung("Burung Hantu", "Rodentia", "Udara", "Bertelur", "Strigidae", "Lebar")

    # Objek Ikan
    ikan1 = Ikan("Ikan Salmon", "Plankton", "Air", "Bertelur", "Sungai", "Kecil")
    ikan2 = Ikan("Ikan Koi", "Pakan Ikan", "Air", "Bertelur", "Kolam", "Kecil")
    ikan3 = Ikan("Ikan Betta", "Serangga", "Air", "Bertelur", "Akuarium", "Kecil")

    # Objek Ular
    ular1 = Ular("Ular Piton", "Mamalia", "Daratan", "Bertelur", 5, True)
    ular2 = Ular("Ular Kobra", "Rodentia", "Daratan", "Bertelur", 3, True)
    ular3 = Ular("Ular Sanca", "Burung", "Daratan", "Bertelur", 4, False)

    # Menampilkan informasi tentang setiap objek
    print("Informasi Burung:")
    burung1.display_info()
    burung1.terbang()
    print()
    burung2.display_info()
    burung2.terbang()
    print()
    burung3.display_info()
    burung3.terbang()
    print()

    print("Informasi Ikan:")
    ikan1.display_info()
    ikan1.berenang()
    print()
    ikan2.display_info()
    ikan2.berenang()
    print()
    ikan3.display_info()
    ikan3.berenang()
    print()

    print("Informasi Ular:")
    ular1.display_info()
    ular1.melata()
    print()
   