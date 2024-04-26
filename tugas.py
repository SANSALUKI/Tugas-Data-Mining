
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load dataset
df = pd.read_csv('heart.csv')


# Menampilkan deskripsi dataset
print("Dataset : Heart Attack Analysis & Prediction Dataset")
print("Tujuan : ingin memprediksi apakah seseorang kemungkinan terkena serangan jantung.")
print("Dataset terdiri dari 303 record dengan 13 atribut independen dan 1 target.")
print("Atribut:")
print("• Usia : Usia pasien")
print("• Jenis Kelamin : Jenis kelamin pasien (1=laki2, 0=perempuan)")
print("• exang: angina akibat olahraga (1 = ya; 0 = tidak)")
print("• caa: jumlah pembuluh arteri (0-3)")
print("• cp : Tipe nyeri dada")
print("  - Nilai 1 : angina tipikal")
print("  - Nilai 2: angina atipikal")
print("  - Nilai 3: nyeri non-angina")
print("  - Nilai 4: tanpa gejala")
print("• trtbps : tekanan darah istirahat (dalam mm Hg)")
print("• chol : kolestoral dalam mg/dl diambil melalui sensor BMI")
print("• fbs : (gula darah puasa >120 mg/dl)")
print("  (1 = benar; 0 = salah)")
print("• rest_ecg : hasil elektrokardiografi istirahat")
print("  - Nilai 0: biasa")
print("  - Nilai 1 : mengalami kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi ST > 0,05 mV)")
print("  - Nilai 2: menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri menurut kriteria Estes")
print("• thalach : tercapai denyut jantung maksimal")
print("Output (Target)")
print("0= lebih kecil kemungkinan terkena serangan jantung")
print("1= lebih besar kemungkinan terkena serangan jantung")

# Menampilkan dataset secara lengkap
print("Dataset:")
print(df)

# Cek missing value
print("\nTidak ada missing value")
print(df.describe())
print("\n", df.isnull().sum())

# Informasi tentang dataframe
print(df.info())

# Splitting the dataset
# Definisikan terlebih dahulu variabel bebasnya yaitu variabel ‘X’,
# dan variabel terikatnya yaitu variabel ‘Y’.
# Dengan menggunakan fungsi ‘StandardScaler' di scikit-learn, kita
# akan menormalkan variabel independen atau variabel 'X'.
X = df.drop(['output'], axis=1)
Y = df['output']
print(X.shape, Y.shape)

# Normalizing independent variables
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns.values)

# Menampilkan data setelah normalisasi
print(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Create logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.coef_)

# Predict target on test set
y_pred = pd.Series(model.predict(X_test))
y_test = y_test.reset_index(drop=True)
z = pd.concat([y_test, y_pred], axis=1)
z.columns = ['True', 'Prediction']
print(z.head())

# Evaluate model performance
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
labels = [0, 1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(labels))
plt.xticks(tick_marks, labels)
plt.yticks(tick_marks, labels)

# Create heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu", fmt='g')
ax.xaxis.set_label_position("top")
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Predicted')
plt.xlabel('True')
plt.show()
