# Import pustaka yang dibutuhkan
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

# 1. Masukkan data set (training)
data = {
    'Temperatur': [10, 25, 15, 20, 18, 17, 22, 24],
    'Kecepatan_Angin': [0, 0, 5, 0, 3, 7, 5, 6],
    'Klasifikasi': ['Dingin', 'Panas', 'Dingin', 'Panas', 'Dingin', 'Dingin', 'Panas', 'Panas']
}

# Konversi data ke DataFrame
df = pd.DataFrame(data)

# Pisahkan fitur (X) dan label (y)
X = df[['Temperatur', 'Kecepatan_Angin']]
y = df['Klasifikasi']

# 2. Menentukan nilai k yang optimal menggunakan cross-validation
k_range = range(1, 8)  # K dari 1 sampai 7
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=4, scoring='accuracy')
    k_scores.append(scores.mean())

# Cari k dengan skor terbaik
optimal_k = k_range[np.argmax(k_scores)]
print(f"Nilai k yang optimal adalah: {optimal_k}")

# 3. Mengklasifikasikan data test
# Data uji: Temperatur = 16, Kecepatan Angin = 3
X_test = [[16, 3]]

# Inisialisasi model KNN dengan k optimal
knn = KNeighborsClassifier(n_neighbors=optimal_k)
knn.fit(X, y)

# Prediksi
prediction = knn.predict(X_test)
print(f"Persepsi Marry saat temperatur 16°C dan kecepatan angin 3 km/jam adalah: {prediction[0]}")
