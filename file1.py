#Buatlah GUI dengan Tkinter yang berisi:
#–1 label judul Aplikasi prediksi Prodi Pilihan
#–10 input nilai mata pelajaran
#–1 button bertuliskan Hasil Prediksi
#–1 label luaran hasil prediksi
#•Atur posisi GUI sebaik mungkin
#•Fungsi Hasil Prediksi menuliskan prodi TeknologiInformasi apapun input yang diberikan ().


import tkinter as tk
from tkinter import font

def tampilkan_prediksi():
    "Fungsi ini dipanggil saat tombol ditekan. Ia akan mengatur teks pada label hasil (hasil_prediksi_var)."
    hasil_prediksi_var.set("Hasil Prediksi: Teknologi Informasi")

# --- Setup Jendela Utama ---
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi")
root.geometry("450x650") 

# Mengatur font default
default_font = font.Font(family="Arial", size=10)
root.option_add("*Font", default_font)

# -Variabel String untuk Hasil-
# Kita menggunakan StringVar agar label bisa di-update secara dinamis
hasil_prediksi_var = tk.StringVar()
hasil_prediksi_var.set("Hasil Prediksi: -")

# --- Membuat Widget ---

# 1. Label Judul
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
# Menempatkan judul di baris 0, melintasi 2 kolom, dengan padding
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))


# 2. 10 Input Nilai Mata Pelajaran
# Kita akan menggunakan loop untuk membuatnya agar lebih efisien
mapel_entries = [] # List untuk menyimpan widget Entry (jika diperlukan nanti)
mapel_labels_text = ["Matematika:", "Bhs. Indonesia:", "Bhs. Inggris:", "Fisika:", "Kimia:", "Biologi:", "Sejarah:", "Geografi:", 
                     "Sosiologi:", "Ekonomi:"]

for i in range(10):
    # Membuat Label Mata Pelajaran
    label = tk.Label(root, text=mapel_labels_text[i])
    # 'sticky="e"' membuat teks label rata kanan
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="e") 
    
    # Membuat Entry (Input)
    entry = tk.Entry(root, width=30)
    entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
    mapel_entries.append(entry)

# 3. Button Hasil Prediksi
prediksi_button = tk.Button(
    root, 
    text="Hasil Prediksi", 
    command=tampilkan_prediksi, 
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white"      
)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)


# 4. Label Hasil Prediksi
# Menggunakan 'textvariable' agar terhubung dengan 'hasil_prediksi_var'
# Saya asumsikan "Iuran hasil produksi" adalah typo dan maksudnya adalah "Keluaran/Hasil Prediksi"
# Label ini akan menampilkan hasil dari fungsi
hasil_label = tk.Label(
    root, 
    textvariable=hasil_prediksi_var, 
    font=("Arial", 14, "italic"),
    fg="#00008B" # Warna biru gelap
)
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()