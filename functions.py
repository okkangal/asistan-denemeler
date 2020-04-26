import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
from gtts import gTTS 
import os 
from pyvirtualdisplay import Display  #tarayıcıyı arka planda çalıştırır 

display = Display(visible = 0, size =(800, 600 ))
display.start()

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located


def dinle():
    #Bu kısımda Recognizer'ımızı r diye çağırıyoruz.
    r = sr.Recognizer()

    #Burada ise cihaza bağlı olan mikrofondan veri almaya başlıyor,
    #daha doğrusu mikrofonu dinlemeye başlıyor.
    with sr.Microphone() as source:
        print("Birşeyler Söyle!")
        
        audio = r.listen(source)

    #Bir ses sinyali geldiği anda onu google recognizer'ı ile tanımaya çalışıyor.
    #Burada birçok seçeneğimiz var, Bing, Yandex vs. ama google en iyi çalışanı diyebilirim.

    #Tanıdıktan sonra eğer dediğiniz şey boş bir ses değilse, yani tıkırtı vs. Dediğiniz geri döndürecek.
    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
    #data          ​= data.lower()
        return str(data)
    except sr.UnknownValueError:
        print("Ne dediğini anlamadım")
        
def konus(metin):
    #Burada kullanacağımız 2 parametre bulunuyor, Dil ve Text
    tts = gTTS(text=str(metin), lang='tr')
    #Burada oluşturduğumuz ses dosyasını konuma merhaba.mp3 diye kaydediyoruz
    tts.save("merhaba.mp3")

    #şimdi ise bu dosyayı açalım.
    os.system("xdg-open merhaba.mp3")  # xdg-open  bir dosyayı öntanımlı programla açmak için 



def music_cal(parca): 

    browser.get("https://www.youtube.com/results?search_query=" + str(parca))
    wait.until(visible((By.ID, "video-title")))
    time.sleep(3)   
    browser.find_element_by_id("video-title").click()



    
#sarki = dinle()
#music_cal(sarki)



#browser.quit()
#display.stop()


# arkaplanda Chromu terminalden durdurmak için gereken komut : killall -q -15 chrome 