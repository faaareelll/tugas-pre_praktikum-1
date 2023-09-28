import random

# Fungsi untuk membuat data acak
def create_data():
    random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
    return random_list

# Fungsi untuk memproses data sesuai tipe
def process_data(data):
    # Mengumpulkan float ke dalam tuple
    float_tuple = tuple(item for item in data if isinstance(item, float))

    # Mengumpulkan string ke dalam list
    string_list = [item for item in data if isinstance(item, str)]

    # Mengelompokkan angka integer berdasarkan satuan, puluhan, dan ratusan
    int_dict = {"satuan": [], "puluhan": [], "ratusan": []}
    for item in data:
        if isinstance(item, int):
            satuan = item % 10
            puluhan = (item % 100) // 10
            ratusan = item // 100

            # Menambahkan ke dictionary sesuai kelompok
            int_dict["satuan"].append(satuan)
            int_dict["puluhan"].append(puluhan)
            int_dict["ratusan"].append(ratusan)

    return float_tuple, string_list, int_dict

# Fungsi untuk menampilkan hasil
def display_data(float_tuple, string_list, int_dict):
    print("Data float dalam bentuk tuple:", float_tuple)
    print("Data string dalam list:", string_list)
    print("Data int dalam dictionary:")
    print("Satuan:", int_dict["satuan"])
    print("Puluhan:", int_dict["puluhan"])
    print("Ratusan:", int_dict["ratusan"])

# Fungsi utama
def main():
    # Membuat data acak
    random_list = create_data()

    # Memproses data
    float_tuple, string_list, int_dict = process_data(random_list)

    # Menampilkan hasil
    display_data(float_tuple, string_list, int_dict)

if __name__ == "__main__":
    main()