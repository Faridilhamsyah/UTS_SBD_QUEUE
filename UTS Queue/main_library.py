from queue import Queue

# Membuat Queue menggunakan library bawaan Python
q = Queue(maxsize=5)

print("=== SISTEM ANTREAN TAKJIL - LIBRARY PYTHON ===")

# Enqueue
data_mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eka"]

for nama in data_mahasiswa:
    q.put(nama)
    print(f"[+] {nama} masuk ke antrean")

print("\nJumlah antrean:", q.qsize())

# Mengecek penuh
print("Apakah antrean penuh?", q.full())

# Tidak memasukkan Fajar karena sudah penuh
if q.full():
    print("[!] Antrian Penuh, Fajar tidak dapat masuk")

# Dequeue dua mahasiswa
print("\nDilayani:", q.get())
print("Dilayani:", q.get())

# Menambahkan data baru
q.put("Fajar")
q.put("Gita")

print("\nJumlah antrean sekarang:", q.qsize())

# Melayani semua
print("\n=== MELAYANI SEMUA ANTREAN ===")

while not q.empty():
    print("Dilayani:", q.get())

# Mengecek kondisi kosong
if q.empty():
    print("\n[!] Antrian Kosong")