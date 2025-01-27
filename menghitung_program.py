import os

def hitung_file(folder_path):
    jumlah_file = 0
    # Melooping melalui semua item dalam folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        # Cek dulu apakah item adalah file
        if os.path.isfile(item_path):
            jumlah_file += 1
        # Jika item adalah folder, maka hitung file di dalamnya
        elif os.path.isdir(item_path):
            jumlah_file += hitung_file(item_path)
    return jumlah_file

def main():
    os.system("cls")
    print("="*40)
    print("PROGRAM MENGHITUNG JUMLAH FILE DI FOLDER")
    print("="*40)
    folder_path = input("Masukan nama folder = ")
    jumlah = hitung_file(folder_path)
    print(f'Jumlah file dalam folder {folder_path} adalah: {jumlah}')

    # Tanya apakah ingin menghitung lagi
    lagi = input("Ingin menghitung lagi? (y/n) = ")
    if lagi.lower() == 'y':
        main()
    else:
        print("Terima kasih!")

if __name__ == "__main__":
    main()