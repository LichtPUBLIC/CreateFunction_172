def konversisuhu(temperature, value):
    # Mengecek apakah unit suhu yang diberikan adalah Celsius
    if value == 'C':
        # Jika ya, konversi dari Fahrenheit ke Celsius
        temperaturesuhu = (temperature - 32) * 5/9  # Rumus konversi
        return temperaturesuhu, 'C'  # Mengembalikan suhu yang telah dikonversi dan unitnya

    else:
        # Jika tidak, asumsikan unit adalah Celsius dan konversi ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32  # Rumus konversi
        return temperaturesuhu, 'F'  # Mengembalikan suhu yang telah dikonversi dan unitnya

# Contoh penggunaan pertama:
celsius_temperature = 30  # Menetapkan suhu dalam Celsius
# Memanggil fungsi untuk mengonversi Celsius ke Fahrenheit
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F') 
# Mencetak hasil konversi dengan format yang ditentukan
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu:.2f}°{target_value}")

# Contoh penggunaan kedua:
fahrenheit_temperature = 86  # Menetapkan suhu dalam Fahrenheit
# Memanggil fungsi untuk mengonversi Fahrenheit ke Celsius
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C') 
# Mencetak hasil konversi dengan format yang ditentukan
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu:.2f}°{target_value}")
