def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

# Fungsi untuk memilih jenis konversi
def main():
    print("Pilih jenis konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Fahrenheit ke Celsius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celsius")
    print("6. Kelvin ke Fahrenheit")

    choice = int(input("Masukkan nomor pilihan: "))

    if choice == 1:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius = {result} Fahrenheit")
    elif choice == 2:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        result = celsius_to_kelvin(celsius)
        print(f"{celsius} Celsius = {result} Kelvin")
    elif choice == 3:
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit = {result} Celsius")
    elif choice == 4:
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        result = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} Fahrenheit = {result} Kelvin")
    elif choice == 5:
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        result = kelvin_to_celsius(kelvin)
        print(f"{kelvin} Kelvin = {result} Celsius")
    elif choice == 6:
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        result = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin = {result} Fahrenheit")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
