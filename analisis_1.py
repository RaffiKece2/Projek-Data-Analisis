import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel("data_praktik.xlsx")



data["Total Harga"] = data["Jumlah"] * data["Harga Satuan"]


plt.figure(figsize=(10,6))
plt.bar(data["Kategori"],data["Total Harga"],color = "blue")
plt.title("Penjualan Harga Pak Joko")
plt.xlabel("Kategori")
plt.ylabel("Total Harga")
plt.tight_layout()
plt.show()

