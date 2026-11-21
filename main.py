class Talaba:
    def __init__(self, ism, universitet):
        self.ism = ism
        self.universitet = universitet

    def malumot(self):
        print(f"Ism: {self.ism}")
        print(f"Universitet: {self.universitet}")

    def oqish(self):
        print("Talaba o'qimoqda.")


class ITTalaba(Talaba):
    def __init__(self, ism, universitet, mutaxassislik):
        super().__init__(ism, universitet)
        self.mutaxassislik = mutaxassislik

    def malumot(self):
        super().malumot()
        print(f"Mutaxassislik: {self.mutaxassislik}")

    def oqish(self):
        super().oqish()
        print(f"Talaba {self.mutaxassislik} yo'nalishida o'qimoqda.")


talaba = ITTalaba(
    "Muhammad",
    "Urganch davlat universiteti",
    "Backend dasturlash"
)

talaba.malumot()
talaba.oqish()
