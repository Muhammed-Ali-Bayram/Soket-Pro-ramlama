import socket  # Socket modülünü içe aktarıyoruz.
import threading  # Threading modülünü içe aktarıyoruz.
import time  # Zaman modülünü içe aktarıyoruz.

# Kullanıcı isimlerini tutmak için bir liste oluşturuyoruz.
chat_isimleri = []
# Thread-safe işlemler için bir kilit oluşturuyoruz.
lock = threading.Lock()

# İstemci işlemlerini yönetecek fonksiyonu tanımlıyoruz.
def client_handler(client_socket, client_address):
    global chat_isimleri
    # İstemciye bağlantının kurulduğunu belirten bir mesaj gönderiyoruz.
    client_socket.send("Bağlantı kuruldu.\n".encode())

    while True:
        # İstemciden chat için bir isim seçmesini istiyoruz.
        client_socket.send("Chat için bir isim seçiniz: ".encode())
        try:
            # Timeout ayarı yaparak aktif olmayan bağlantıları kesmeyi sağlıyoruz.
            client_socket.settimeout(60)
            # İstemciden gelen ismi alıyoruz.
            chat_ismi = client_socket.recv(1024).decode().strip()
        except socket.timeout:
            # Eğer istemci 1 dakika boyunca bir işlem yapmazsa bağlantıyı kesiyoruz.
            client_socket.send("Bağlantı sonlandırıldı (1 dakikadan uzun süre işlem yapılmadı).\n".encode())
            client_socket.close()
            return

        with lock:
            # Eğer chat ismi boş değilse ve daha önce kullanılmamışsa
            if chat_ismi and chat_ismi not in chat_isimleri:
                # İsmi listeye ekliyoruz.
                chat_isimleri.append(chat_ismi)
                # İstemciye ismin başarıyla tahsis edildiğini bildiriyoruz.
                client_socket.send(f"{chat_ismi} ismi başarıyla tahsis edildi.\n".encode())
                break
            else:
                # Eğer isim zaten kullanılıyorsa istemciden başka bir isim seçmesini istiyoruz.
                client_socket.send("Bu isim zaten kullanılıyor. Başka bir isim seçiniz.\n".encode())

    while True:
        # İstemciden bir komut girmesini istiyoruz.
        client_socket.send("Komut giriniz (list veya quit): ".encode())
        try:
            # Timeout ayarı yapıyoruz.
            client_socket.settimeout(60)
            # İstemciden gelen komutu alıyoruz.
            komut = client_socket.recv(1024).decode().strip()
        except socket.timeout:
            # Eğer istemci 1 dakika boyunca bir işlem yapmazsa bağlantıyı kesiyoruz.
            client_socket.send("Bağlantı sonlandırıldı (1 dakikadan uzun süre işlem yapılmadı).\n".encode())
            break
        
        if komut == "quit":
            # Eğer komut "quit" ise döngüden çıkıyoruz ve bağlantıyı sonlandırıyoruz.
            break
        elif komut == "list":
            # Eğer komut "list" ise mevcut chat isimlerini istemciye gönderiyoruz.
            with lock:
                isimler = "\n".join(chat_isimleri)
            client_socket.send(f"Mevcut chat isimleri:\n{isimler}\n".encode())
        else:
            # Geçersiz komut girilirse istemciye geçersiz komut mesajı gönderiyoruz.
            client_socket.send("Geçersiz komut. 'list' veya 'quit' giriniz.\n".encode())

    with lock:
        # Bağlantı sonlandırıldığında chat ismini listeden kaldırıyoruz.
        chat_isimleri.remove(chat_ismi)
    # Bağlantıyı kapatıyoruz.
    client_socket.close()
    # Bağlantının sonlandırıldığını sunucu ekranına yazdırıyoruz.
    print(f"{client_address} adresindeki kullanıcı bağlantısı sonlandırıldı.")

# Sunucuyu başlatan fonksiyonu tanımlıyoruz.
def sunucu_baslat(host='localhost', port=12345):
    # Bir TCP soketi oluşturuyoruz.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Sunucuyu belirtilen host ve port üzerinde bağlama işlemi yapıyoruz.
    server_socket.bind((host, port))
    # Sunucunun 10 bağlantıya kadar dinlemesini sağlıyoruz.
    server_socket.listen(10)
    # Sunucunun dinlemeye başladığını belirten bir mesaj yazdırıyoruz.
    print(f"Sunucu {host}:{port} üzerinde dinliyor")

    while True:
        # Yeni bir istemci bağlantısını kabul ediyoruz.
        client_socket, client_address = server_socket.accept()
        # Bağlantının kabul edildiğini sunucu ekranına yazdırıyoruz.
        print(f"{client_address} adresinden bağlantı alındı")
        # Her yeni bağlantı için bir thread oluşturuyoruz ve client_handler fonksiyonunu çalıştırıyoruz.
        client_thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
        client_thread.start()

# Programın ana kısmı, sunucuyu başlatıyoruz.
if __name__ == "__main__":
    sunucu_baslat()
