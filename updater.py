#-*- coding: utf-8 -*-

# 모듈 임포트
import os
import urllib.request
from bs4 import BeautifulSoup
import zipfile
import requests
import shutil

# 최신버전/최신버전 다운로드 링크 확인
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

    # 업데이트 패키지 제거
    os.remove("master.zip")

    # 옮기기
    filename = 'README.md'
    src = 'Real-time_inspection_tester_V.%s-master/'%rtit
    dir = '/'
    shutil.move(src + filename, dir + filename)
    filename = 'system'
    src = 'Real-time_inspection_tester_V.%s-master/'%rtit
    dir = '/'
    shutil.move(src + filename, dir + filename)
    filename = 'Real-time_inspection_tester.py'
    src = 'Real-time_inspection_tester_V.%s-master/'%rtit
    dir = '/'
    shutil.move(src + filename, dir + filename)
    filename = 'LICENSE'
    src = 'Real-time_inspection_tester_V.%s-master/'%rtit
    dir = '/'
    shutil.move(src + filename, dir + filename)
    filename = 'system'
    src = 'Real-time_inspection_tester_V.%s-master/'%rtit
    dir = '/'
    shutil.move(src + filename, dir + filename)
    os.system("start Real-time_inspection_tester.py")

else:
    pass
