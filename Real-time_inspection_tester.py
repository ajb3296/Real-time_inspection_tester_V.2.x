import os
import time
from bs4 import BeautifulSoup

if not os.path.exists("system/Real-time_inspection_test"):
    print("Please unzip the file properly and execute it.\n\nPress the ENTER key to exit the program.")
    os.system("pause")
    exit()

while True:
    if not os.path.exists("setting.xml"):
        print("""Please select language:
언어를 선택하세요:
1. English - 영어
2. 한글 - Korean
""")
        language = input("언어를 선택하세요 (1/2) : ")
        if language==1 or language=="english" or language=="영어":
            language="en"
            break
        elif language==2 or language=="한국어" or language=="한글" or language=="korean" or language=="korea":
            language="ko"
            break
        else:
            pass
    else:
        file = open("setting.xml", "r")
        html=file.read()
        file.close()
        soup = BeautifulSoup(html, 'html.parser')
        language = soup.find("language")
        filename = soup.find("filename")
        fileinside = soup.find("fileinside")
    if language.get_text()=="ko" or language.get_text()=="en":
        print(language.get_text())
    os.system("pause")
    break
    
os.system("title Real-time_inspection_test V.2.0")
os.system("mode.com con cols=120 lines=40")
num=0

os.system("cls")

sec=3
while True:
    print("""
                                                   QESASDDS
                                                    .BgK.
                                                   :BBEE.
                                               JBQYBBBsPAW
                                                 EBBPi
                                               .BBPP.
                                              vBBgS
                                             bBBgi
                                            BBM2:
                                          iBBPS
                                         SBQQr
                                        BBBq.
                                      :J::L.
                                     ru7i.
                                    :usJ:
                                   .BU..       ..
                                  :BE       iKBBBBB
                                  ;'     .dBBBBBBRBK
                                 /    :vPEbSBBDSjv12
                       .iv.     / .7IZDZU7. .SYssJv.
                      :iUQM7   / ::7PUr....  71r.
                     .....:uE/.  .........
                      ....../EbL    ...
                       ..  iPBBBB
                         .v2uqRBBB:
                          sj77IgBBBX
                           rJvvIEBBBq
                            .jY77rrLq
                             .JULJjj.
                                :i:.
    Version : V.2.0
    [ %s ] 초 후 백신 테스트를 시작합니다.
""" %sec)
    time.sleep(1)
    sec=sec-1
    os.system("cls")
    if sec==0:
        break
    else:
        pass
print("""
                                                   QESASDDS
                                                    .BgK.
                                                   :BBEE.
                                               JBQYBBBsPAW
                                                 EBBPi
                                               .BBPP.
                                              vBBgS
                                             bBBgi
                                            BBM2:
                                          iBBPS
                                         SBQQr
                                        BBBq.
                                      :J::L.
                                     ru7i.
                                    :usJ:
                                   .BU..       ..
                                  :BE       iKBBBBB
                                  ;'     .dBBBBBBRBK
                                 /    :vPEbSBBDSjv12
                       .iv.     / .7IZDZU7. .SYssJv.
                      :iUQM7   / ::7PUr....  71r.
                     .....:uE/.  .........
                      ....../EbL    ...
                       ..  iPBBBB
                         .v2uqRBBB:
                          sj77IgBBBX
                           rJvvIEBBBq
                            .jY77rrLq
                             .JULJjj.
                                :i:.
    체크중. . .
    핵심 알고리즘 실행. . .
""")

# Core algorithm
file = open("EICAR.TXT", 'w')
file.write("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
file.close()
while True:
    try:
        file = open("EICAR.TXT", 'r')
    except PermissionError:
        if language.get_text()=="ko":
            print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
        else:
            print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
        os.system("pause")
        break
    except OSError:
        if language.get_text()=="ko":
            print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
        else:
            print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
        os.system("pause")
        break
    except FileNotFoundError:
        if language.get_text()=="ko":
            print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
        else:
            print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
        os.system("pause")
        break
    eicar=file.read()
    if not eicar=="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*":
        print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
        os.remove("EICAR.TXT")
        os.system("pause")
        break
    if num==10:
        os.remove("EICAR.TXT")
        print("\n\n백신이 미끼파일을 탐지하고 치료/제거하는데 걸리는 시간이 [ 10 ] 초가 넘었습니다.\n백신의 상태를 다시 한번 확인해 주세요.")
        os.system("pause")
        break
    num=num+1
    time.sleep(1)
file.close()
exit()
