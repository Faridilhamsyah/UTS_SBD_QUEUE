class QueueStatis:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1 and self.tail == -1

    def is_full(self):
        return self.tail == self.kapasitas - 1

    def enqueue(self, isi):
        if self.is_full():
            print(f"[!] Antrian Penuh, {isi} tidak dapat masuk")
            return False

        # Jika queue masih kosong
        if self.is_empty():
            self.head = 0

        self.tail += 1
        self.data[self.tail] = isi

        print(f"[+] {isi} masuk ke antrean")
        return True

    def dequeue(self):
        if self.is_empty():
            print("[!] Antrian Kosong (Underflow)")
            return None

        keluar = self.data[self.head]

        # Menggeser semua elemen ke depan
        for i in range(self.tail):
            self.data[i] = self.data[i + 1]

        self.data[self.tail] = None
        self.tail -= 1

        # Jika semua data sudah keluar
        if self.tail == -1:
            self.head = -1

        return keluar

    def peek(self):
        if self.is_empty():
            return None

        return self.data[self.head]

    def tampil(self):
        if self.is_empty():
            return "[]"

        hasil = []

        for i in range(self.head, self.tail + 1):
            hasil.append(self.data[i])

        return hasil