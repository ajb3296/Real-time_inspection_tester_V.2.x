import os
import urllib.request
from bs4 import BeautifulSoup
import zipfile
import requests
import shutil

file = open("system/version", 'r')
version=file.read()
file.close()

url = "https://newpremium.github.io/version/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
rtit = soup.find("rtit")
rtit = rtit.get_text()
rtitdownload = soup.find("rtitdownload")
url = rtitdownload.get_text()

# 업데이트 할지 안할지 결정
if not rtit==version:
    print("프로그램을 새 버전으로 업데이트 해야 합니다. 자동으로 업데이트가 진행됩니다.\nYou need to update the program to a new version. The update will proceed automatically.")
    # 폴더 비우기
    try:
        shutil.rmtree('update')
    except FileNotFoundError:
        os.mkdir("update")

    # 최신버전 다운로드
    urllib.request.urlretrieve(url, "master.zip")

    # 압축풀기
    zip_ref = zipfile.ZipFile("master.zip", 'r')
    zip_ref.extractall("/")
    zip_ref.close()

    # 불러오기
    os.system("cls")
    os.system("call Real-time_inspection_tester_V.%s-master\Real-time_inspection_tester.py" %rtit)
    exit()
