import socket  # Socket modülünü içe aktarıyoruz.

# İstemci işlemlerini başlatan fonksiyonu tanımlıyoruz.
def istemci_baslat(host='localhost', port=12345):
    # Bir TCP soketi oluşturuyoruz.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Sunucuya bağlanma işlemini gerçekleştiriyoruz.
    client_socket.connect((host, port))

    # Sunucudan gelen bağlantı mesajını alıyoruz ve ekrana yazdırıyoruz.
    print(client_socket.recv(1024).decode())

    while True:
        # Kullanıcıdan chat için bir isim seçmesini istiyoruz.
        chat_ismi = input("Chat için bir isim seçiniz: ")
        # Seçilen ismi sunucuya gönderiyoruz.
        client_socket.sendall(chat_ismi.encode())
        
        # Sunucudan gelen yanıtı alıyoruz ve ekrana yazdırıyoruz.
        yanit = client_socket.recv(1024).decode()
        print(yanit)
        # Eğer isim başarıyla tahsis edildiyse döngüden çıkıyoruz.
        if "başarıyla tahsis edildi" in yanit:
            break

    while True:
        # Kullanıcıdan bir komut girmesini istiyoruz.
        komut = input("Komut giriniz (list veya quit): ")
        # Girilen komutu sunucuya gönderiyoruz.
        client_socket.sendall(komut.encode())
        
        # Sunucudan gelen yanıtı alıyoruz ve ekrana yazdırıyoruz.
        yanit = client_socket.recv(1024).decode()
        print(yanit)
        
        if komut == "quit":
            # Eğer komut "quit" ise döngüden çıkıyoruz ve bağlantıyı sonlandırıyoruz.
            break

    # Bağlantıyı kapatıyoruz.
    client_socket.close()

# Programın ana kısmı, istemciyi başlatıyoruz.
if __name__ == "__main__":
    istemci_baslat()
