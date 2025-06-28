import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd


data = pd.read_excel("data_praktik.xlsx")


data["Total Penjualan"] = data["Jumlah"] * data["Harga Satuan"]

data["Tanggal"] = pd.to_datetime(data["Tanggal"],errors= "coerce")
data = data.dropna(subset=["Tanggal"])


data_harian = data.groupby("Tanggal",as_index=False)["Total Penjualan"].sum()

data_harian["Tanggal Ordinal"] = data_harian["Tanggal"].map(lambda x: x.toordinal())

X = data_harian[["Tanggal Ordinal"]]
y = data_harian["Total Penjualan"]

model = LinearRegression()


model.fit(X,y)


tanggal_prediksi = pd.date_range(start=data_harian["Tanggal"].max() + pd.Timedelta(days= 1),periods= 7)
tanggal_ordinal = tanggal_prediksi.map(lambda x: x.toordinal()).values.reshape(-1,1)
prediksi_jual = model.predict(tanggal_ordinal)



data_prediksi = pd.DataFrame({
    "Tanggal": tanggal_prediksi,
    "Total Penjualan": prediksi_jual,
    "Jenis": "Prediksi"
    
})

data["Jenis"] = "Asli"
data_total = pd.concat([data,data_prediksi],ignore_index= True)

data_total["Tanggal"] = pd.to_datetime(data_total["Tanggal"],errors = "coerce")

plt.figure(figsize=(10,6))


for jenis, warna in zip(["Asli","Prediksi"],["blue","red"]):
    subset = data_total[data_total["Jenis"] == jenis]
    plt.bar(subset["Tanggal"],subset["Total Penjualan"],label = jenis,color = warna)

plt.xlabel("Tanggal")
plt.ylabel("Total Penjualan")
plt.title("Nilai Prediksi Baru")
plt.xticks(rotation = 45)
plt.legend()
plt.grid(axis= 'y',linestyle = '--',alpha = 0.5)

plt.tight_layout()
plt.show()

