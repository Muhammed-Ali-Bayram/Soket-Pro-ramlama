# Soket-Pro-ramlama
Bu projede bir chat programının, kullanıcılara isim tahsisini gerçekleştirir

1. Server dosyası: Localde server olarak çalışacak bir TCP soketi oluşturmalıdır. Sürekli olarak 
kullanıcıları dinler, gerektiğinde birden fazla kullanıcının işlemini aynı anda yapabilir ve eş zamanlı 
olarak 10 kullanıcıya bağlantı sunabilir. Kullanıcı bağlantısı gerçekleştirildiğinde, kullanıcıya 
bağlantı kurulduğunu teyit eden bir mesaj yollar. Chat programı için kullanmak istediği chat ismini 
bildirmesini ister. Bildirilen chat ismi daha önce kullanılmadıysa bu ismi kullanıcıya tahsis eder ve 
bunu kullanıcıya teyit eder. Eğer chat ismi başka bir kullanıcı tarafından kullanılıyorsa, isim 
tahsisini gerçekleştirmez ve başka bir chat ismi seçmesi gerektiğini kullanıcıya bildirir. Geçerli bir 
chat ismi tahsis edilene kadar bu işlemi tekrarlar. Kullanıcılara tahsis edilen chat isimlerinin bir 
listesini tutar. Bir kullanıcı bir dakikadan uzun bir süre herhangi bir işlem yapmaz ise bağlantısını 
keser. Yeni bir bağlantı gerçekleştirdiği zaman bağlantı kuran kullanıcının adresini de belirtecek 
şekilde bunu server ekranına yazdırır. Aşağıda belirtilen, kullanıcıdan gelen taleplere karşılık verir.

2. Client dosyası: Bir TCP soketi oluşturur ve chat serverına bağlanma talebi gönderir. Bağlantı 
gerçekleştirildiğinde bunu client ekranında duyurur. Kullanıcıdan bir chat ismi seçmesini ister. 
Seçilen ismi servera gönderir. Seçilen chat ismi tahsis edilirse bunu client ekranında ilan eder. Eğer 
tahsis işlemi gerçekleşmez ise bu ismin kullanılamayacağını client ekranında yazar ve kullanıcıdan 
yeni bir chat ismi seçmesini ister. Yeni seçilen chat ismini servera gönderir. Geçerli bir isim tahsis 
edilene kadar bu işlem tekrarlanır

