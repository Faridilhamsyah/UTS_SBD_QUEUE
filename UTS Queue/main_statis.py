from queue_statis import QueueStatis

# Membuat antrean dengan kapasitas 5
q = QueueStatis(5)

print("=== SISTEM ANTREAN TAKJIL - QUEUE STATIS ===")

# Cek apakah kosong
print("\nApakah antrean kosong?", q.is_empty())

# Menambahkan 5 mahasiswa
data_mahasiswa = ["Andi", "Budi", "Citra", "Dewi", "Eka"]

for nama in data_mahasiswa:
    q.enqueue(nama)

print("\nAntrean saat ini:", q.tampil())

# Mencoba menambahkan saat penuh
q.enqueue("Fajar")

print("Apakah antrean penuh?", q.is_full())

# Melayani 2 mahasiswa
print("\nDilayani:", q.dequeue())
print("Antrean:", q.tampil())

print("Dilayani:", q.dequeue())
print("Antrean:", q.tampil())

# Sekarang ada ruang untuk mahasiswa baru
q.enqueue("Fajar")
q.enqueue("Gita")

print("\nAntrean setelah Fajar dan Gita masuk:")
print(q.tampil())

# Melayani semua mahasiswa
print("\n=== MELAYANI SEMUA ANTREAN ===")

while not q.is_empty():
    print("Dilayani:", q.dequeue())

# Mencoba dequeue saat kosong
print("\nMencoba melayani antrean kosong:")
q.dequeue()