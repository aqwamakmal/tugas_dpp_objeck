from animals import Animal

class burung(Animal):
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

# Membuat objek dari kelas Burung
    burung = burung ("Elang", "Daging", "Udara", "Bertelur", "Raptor", "Lebar")
    
print("## informasi burung elang ##")
