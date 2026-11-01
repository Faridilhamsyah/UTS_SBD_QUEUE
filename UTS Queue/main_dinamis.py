from queue_dinamis import QueueDinamis

q = QueueDinamis()

print("=== SISTEM ANTREAN TAKJIL - QUEUE DINAMIS ===")

# Menambahkan mahasiswa
data_mahasiswa = [
    "Andi",
    "Budi",
    "Citra",
    "Dewi",
    "Eka",
    "Fajar",
    "Gita"
]

for nama in data_mahasiswa:
    q.enqueue(nama)

print("\nAntrean saat ini:")
print(q.tampil())

# Melihat mahasiswa paling depan
print("\nMahasiswa paling depan:", q.peek())

# Melayani dua mahasiswa
print("\nDilayani:", q.dequeue())
print("Dilayani:", q.dequeue())

print("\nAntrean sekarang:")
print(q.tampil())

# Menambah mahasiswa lagi
q.enqueue("Hadi")
q.enqueue("Indah")

print("\nAntrean setelah penambahan:")
print(q.tampil())

# Melayani semua
print("\n=== MELAYANI SEMUA ANTREAN ===")

while not q.is_empty():
    print("Dilayani:", q.dequeue())

# Underflow
q.dequeue()