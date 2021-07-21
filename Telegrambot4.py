import pyautogui
import time
import webbrowser
url = 'https://twitter.com/Elevate_CV'
n = 0
def post():
    time.sleep(1)
    pyautogui.write("/mint stake")
    pyautogui.press("enter")
    time.sleep(1)



def wait():
    print("Kółko numer:", n, "zrobione.")
    time.sleep(53)
    print("Uwaga za 5 sekund następne kólko")
    time.sleep(6)
    
print("Ile Stakehousów? ")
a = int(input())
print("Ile razy? ")
ile_razy_chcecie = int(input())

                       
# 1. trzeba zainstalować python3: https://www.python.org/downloads/
# 2. zainstalować
# 3. otworzyc powershell albo cmd:
# znak windows -> wpisac "powershell"
# 4. zainstalować bibliotekę "pyautogui" wpisując w powershell
# pip3 install pyautogui

#WAZNE KANAŁY STAKEHOUSE MUSZĄ BYĆ PRZYPIĘTE ABY NIE MIESZYAŁY
#SIĘ POZYCJE(BOT KLIKA PO KOLEI W KANAŁY OD 1 DO 4)


# trzeba miec telegram na wierzchu
#Uruchom wpisz ilość powtórzeń i ilość aktywnych Stakehousów

if (a == 1):
    for i in range(1, ile_razy_chcecie):
        pyautogui.click(253, 114)
        post()
        n+=1
        wait()
elif (a == 2):
    for i in range(1, ile_razy_chcecie):
        pyautogui.click(253, 114)
        post()
        pyautogui.click(334, 180)
        post()
        n+=1
        wait()

elif (a == 3):
    for i in range(1, ile_razy_chcecie):
        pyautogui.click(253, 114)
        post()
        pyautogui.click(334, 180)
        post()
        pyautogui.click(356, 227)
        post()
        n+=1
        wait()
    
elif (a == 4):
    for i in range(1, ile_razy_chcecie):
        pyautogui.click(253, 114)
        post()
        pyautogui.click(334, 180)
        post()
        pyautogui.click(356, 227)
        post()
        pyautogui.click(338, 277)
        post()
        n+=1
        wait()
else:
    print("Zła ilość Stakehousów")

webbrowser.register('chrome',
    None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(url)
