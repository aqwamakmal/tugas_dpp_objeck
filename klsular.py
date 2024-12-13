from animals import Animal

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

# Membuat objek dari kelas Ular
    ular =("Ular Piton", "Mamalia", "Daratan", "Bertelur", 5, True)
    
print ("## informasi ular ##")