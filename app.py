# Install library yang dibutuhkan
!pip install streamlit pyngrok -q

# Tambahkan authtoken ngrok (ganti dengan token punyamu sendiri)
!ngrok config add-authtoken '338dbqzOuOvRMHfU5QyQ1nuMLoE_2RrFAnMk9C6oXgACUqGBG'

# Buat file app.py berisi aplikasi Streamlit dengan 3 fitur
with open("app.py", "w") as f:
    f.write("""
import streamlit as st

st.title("Aplikasi Serbaguna")

# Menu utama
menu = st.sidebar.radio("Pilih Fitur", ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

# ----------------- Fitur 1: Kalkulator -----------------
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")

    num1 = st.number_input("Masukkan angka pertama", value=0.0)
    num2 = st.number_input("Masukkan angka kedua", value=0.0)

    operator = st.selectbox("Pilih operator", ["+", "-", "*", "/"])

    if st.button("Hitung"):
        if operator == "+":
            hasil = num1 + num2
        elif operator == "-":
            hasil = num1 - num2
        elif operator == "*":
            hasil = num1 * num2
        elif operator == "/":
            if num2 != 0:
                hasil = num1 / num2
            else:
                hasil = "Error: Pembagian dengan nol!"
        st.success(f"Hasil: {hasil}")

# ----------------- Fitur 2: Konversi Suhu -----------------
elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")

    nilai = st.number_input("Masukkan nilai suhu", value=0.0)
    satuan_asal = st.selectbox("Pilih satuan asal", ["Celcius", "Reamur", "Fahrenheit"])
    satuan_tujuan = st.selectbox("Konversi ke", ["Celcius", "Reamur", "Fahrenheit"])

    if st.button("Konversi"):
        hasil = None
        if satuan_asal == "Celcius":
            if satuan_tujuan == "Celcius":
                hasil = nilai
            elif satuan_tujuan == "Reamur":
                hasil = (4/5) * nilai
            elif satuan_tujuan == "Fahrenheit":
                hasil = (9/5) * nilai + 32
        elif satuan_asal == "Reamur":
            if satuan_tujuan == "Celcius":
                hasil = (5/4) * nilai
            elif satuan_tujuan == "Reamur":
                hasil = nilai
            elif satuan_tujuan == "Fahrenheit":
                hasil = (9/4) * nilai + 32
        elif satuan_asal == "Fahrenheit":
            if satuan_tujuan == "Celcius":
                hasil = (5/9) * (nilai - 32)
            elif satuan_tujuan == "Reamur":
                hasil = (4/9) * (nilai - 32)
            elif satuan_tujuan == "Fahrenheit":
                hasil = nilai

        st.success(f"Hasil konversi: {hasil} {satuan_tujuan}")

# ----------------- Fitur 3: Deret Fibonacci -----------------
elif menu == "Deret Fibonacci":
    st.header("Deret Fibonacci")

    n = st.number_input("Masukkan jumlah bilangan (n)", min_value=1, value=5, step=1)

    def fibonacci(n):
        deret = []
        a, b = 0, 1
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b
        return deret

    if st.button("Tampilkan Deret"):
        hasil = fibonacci(n)
        st.success(f"Deret Fibonacci {n} bilangan: {hasil}")
""")

# Hentikan streamlit lama kalau ada
!pkill streamlit

# Jalankan aplikasi dengan streamlit dan buat link publik via ngrok
from pyngrok import ngrok
public_url = ngrok.connect(8501)
print("Aplikasi bisa dibuka di:", public_url)
!streamlit run app.py --server.port 8501
