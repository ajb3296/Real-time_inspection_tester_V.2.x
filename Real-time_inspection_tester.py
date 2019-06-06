#-*- coding: utf-8 -*-

# 모듈 임포트
import os
import time
from bs4 import BeautifulSoup
import requests
import urllib.request
import zipfile
import shutil

if __name__=="__main__":
    '''
    # 압축 상태 확인
    if not os.path.exists("system/Real-time_inspection_test"):
        print("Please unzip the file properly and execute it.\n\nPress the ENTER key to exit the program.")
        os.system("pause")
        exit()
'''
    # 기본설정
    os.system("title Real-time_inspection_tester V.2.0")
    os.system("mode.com con cols=120 lines=40")
    version="2.0"
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
    Version : V.%s
    Loading. . .
    """ %version)
    
    os.system("call updater.py")
    

    # 버전 확인

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
            elif language==2 or language=="한국어" or language=="한글" or language=="korean" or language=="korea":
                language="ko"
            else:
                pass
        else:
            file = open("setting.xml", "r")
            html=file.read()
            file.close()
            soup = BeautifulSoup(html, 'html.parser')
            language = soup.find("language")
            language = language.get_text()
            filename = soup.find("filename")
            filename = filename.get_text()
            fileinside = soup.find("fileinside")
            fileinside = fileinside.get_text()
        if language == "ko" or language == "en":
            break
        else:
            print("Language error\n언어오류\n\nModify the language settings of the setting.xml file(en/ko)\nsetting.xml 파일의 언어설정을 수정하세요(en/ko)")
            os.system("pause")
            exit()
        

    num=0

    os.system("cls")

    # 메인 페이지
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
    Version : V.%s
    [ %s ] 초 후 백신 테스트를 시작합니다.
""" %(version, sec))
        time.sleep(1)
        sec=sec-1
        os.system("cls")
        if sec==0:
            break
        else:
            pass
    if language=="ko":
        chackmsg="체크중. . .\n    핵심 알고리즘 실행. . ."
    else:
        chackmsg="Checking. . .\n    execution of core algorithm. . ."
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
    %s
""" %chackmsg)

    # Core algorithm
    file = open(filename, 'w')
    file.write(fileinside)
    file.close()
    while True:
        try:
            file = open(filename, 'r')
        except PermissionError:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break
        except FileNotFoundError:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break
        except OSError:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break
        eicar=file.read()
        if not eicar==fileinside:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break
        if num==10:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료/제거하는데 걸리는 시간이 [ 10 ] 초가 넘었습니다.\n백신의 상태를 다시 한번 확인해 주세요.")
            else:
                print("It took more than [ 10 ] seconds for the vaccine to detect and clean/remove the decoy file.\nPlease check the status of the vaccine again.")
            break
        num=num+1
        file.close()
        time.sleep(1)
    file.close()
    try:
        os.remove(filename)
    except PermissionError:
        pass
    except FileNotFoundError:
        pass
    except OSError:
        pass
    if language=="ko":
        print("\n프로그램을 종료하시려면 아무키나 누르세요.")
    else:
        print("\nPress any key to exit the program.")
    os.system("pause>nul")
exit()
