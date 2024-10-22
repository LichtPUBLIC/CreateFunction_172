import math  # Mengimpor library math untuk menggunakan konstanta dan fungsi matematika, seperti pi

# Membuat lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r  # Fungsi ini menerima satu parameter 'r' (jari-jari) dan mengembalikan luas lingkaran

# Contoh penggunaan fungsi
jari_jari = 7  # Menetapkan nilai jari-jari lingkaran (misalnya, 7)
area = luas_lingkaran(jari_jari)  # Memanggil fungsi luas_lingkaran dengan jari-jari yang telah ditentukan dan menyimpan hasilnya dalam variabel 'area'

# Mencetak hasil luas lingkaran
print(f"Luas lingkaran dengan jari jari {jari_jari} adalah {area:.2f}")  # Menggunakan f-string untuk mencetak hasil dengan format 2 desimal
