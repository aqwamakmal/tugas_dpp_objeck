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


if __name__ == "__main__":
   
    kucing = Animal("Kucing", "Ikan", "Daratan", "Melahirkan")
    anjing = Animal("Anjing", "Daging", "Daratan", "Melahirkan")
    
    
    print("Informasi Kucing:")
    kucing.display_info()
    print("\nInformasi Anjing:")
    anjing.display_info()