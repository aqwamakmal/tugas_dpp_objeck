from animals import Animal

class ikan(Animal):
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
        
# Membuat objek dari kelas Ikan
    ikan = ikan("Ikan Salmon", "Plankton", "Air", "Bertelur", "Sungai", "Kecil")
    
print("## informasi ikan ##")
