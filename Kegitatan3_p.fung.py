# Fungsi untuk menghitung nilai akhir mahasiswa
def menghitung_nilai_akhir(student_data):
    final_scores = {}  # Inisialisasi dictionary untuk menyimpan nilai akhir
    for name, scores in student_data.items():
        # Hitung nilai akhir sebagai rata-rata dari nilai UTS dan UAS
        final_score = (scores['nilai_uts'] + scores['nilai_uas']) / 2
        final_scores[name] = final_score  # Simpan nilai akhir dalam dictionary
    return final_scores


# Fungsi untuk menampilkan nilai akhir mahasiswa
def menampilkan_nilai_akhir(final_scores):
    print("Hasil Nilai Akhir Mahasiswa:")
    for name, final_score in final_scores.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(name, final_score))


# Fungsi utama
def main():
    # Data mahasiswa beserta nilai UTS dan UAS
    student_data = {
        'SIA': {'nilai_uts': 88, 'nilai_uas': 85},
        'SIB': {'nilai_uts': 78, 'nilai_uas': 86},
        'SIC': {'nilai_uts': 82, 'nilai_uas': 94},
    }

    # Hitung nilai akhir
    final_scores = menghitung_nilai_akhir(student_data)

    # Tampilkan nilai akhir
    menampilkan_nilai_akhir(final_scores)


# Pengecekan jika script dijalankan langsung
if __name__ == "__main__":
    main()