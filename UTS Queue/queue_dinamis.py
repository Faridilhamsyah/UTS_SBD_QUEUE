class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueDinamis:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, isi):
        node_baru = Node(isi)

        # Jika antrean kosong
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru

        else:
            # Node baru disambungkan ke belakang
            self.rear.next = node_baru
            self.rear = node_baru

        print(f"[+] {isi} masuk ke antrean")
        return True

    def dequeue(self):
        if self.is_empty():
            print("[!] Antrian Kosong (Underflow)")
            return None

        keluar = self.front.data

        # Front berpindah ke node berikutnya
        self.front = self.front.next

        # Jika antrean menjadi kosong
        if self.front is None:
            self.rear = None

        return keluar

    def peek(self):
        if self.is_empty():
            return None

        return self.front.data

    def tampil(self):
        if self.is_empty():
            return "[]"

        hasil = []
        sekarang = self.front

        # Menelusuri semua node
        while sekarang is not None:
            hasil.append(sekarang.data)
            sekarang = sekarang.next

        return hasil