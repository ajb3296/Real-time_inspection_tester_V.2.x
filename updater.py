# 버전 확인
    url = "https://newpremium.github.io/version/"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    rtit = soup.find("rtit")
    rtit = rtit.get_text()
    rtitdownload = soup.find("rtitdownload")
    url = rtitdownload.get_text()

    if not rtit=="2.0":
        print("프로그램을 새 버전으로 업데이트 해야 합니다. 자동으로 업데이트가 진행됩니다.\nYou need to update the program to a new version. The update will proceed automatically.")
        try:
            shutil.rmtree('update')
            except OSError as e:
        if e.errno == 2:
            pass

    else:
        raise
        urllib.request.urlretrieve(url, "update/master.zip")        
        zip_ref = zipfile.ZipFile("update/master.zip", 'r')
        zip_ref.extractall("update")
        zip_ref.close()
        os.system("call update\Real-time_inspection_tester_V.%s-master\Real-time_inspection_tester.py")
        exit()
