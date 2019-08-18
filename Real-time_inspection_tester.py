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
    
    # 압축 상태 확인
    if not os.path.exists("system/Real-time_inspection_test"):
        print("Please unzip the file properly and execute it.\n\nPress the ENTER key to exit the program.")
        os.system("pause")
        exit()

    # 기본설정
    os.system("title Real-time_inspection_tester V.2.0")
    os.system("mode.com con cols=120 lines=40")

    # 버전 설정
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

    language="language"
    while True:
        # For Portable
        # 설정파일 존재확인
        if not os.path.exists("setting.xml"):
            print("""언어를 선택하세요
Please select a language
1. 한글 - Korean
2. English - 영어
""")

            language = input("<1/2> : ")

            if language == '1' or language == 'ko' or language == '한글' or language == 'korean':
                language="ko"
                break
            elif language == '2' or language == 'en' or language == '영어' or language == "english":
                language="en"
                break
            else:
                pass
        else:
            break

    # 설정파일 만들기
    if language == "ko" or language == "en":
        file = open("setting.xml", "w", encoding='UTF-8')
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write("<!-- Language (언어) -->\n")
        file.write("<language>%s</language>\n\n" %language)
        file.write("<!-- File name (미끼파일 이름) -->\n")
        file.write("<filename>EICAR.TXT</filename>\n\n")
        file.write("<!-- File internal code (미끼파일 내부 코드) -->\n")
        file.write("<!-- default value  (기본값) : X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H* -->\n")
        file.write("<fileinside>X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*</fileinside>\n")
        file.close()
        
    # 설정파일이 존재할 경우 읽어오기
    if os.path.exists("setting.xml"):
        file = open("setting.xml", "r", encoding='UTF-8')
        html=file.read()
        file.close()
        soup = BeautifulSoup(html, 'html.parser')
        language = soup.find("language")
        language = language.get_text()
        filename = soup.find("filename")
        filename = filename.get_text()
        fileinside = soup.find("fileinside")
        fileinside = fileinside.get_text()

    # 프로그램이 사용 가능한 언어인지 확인
    if language == "ko" or language == "en":
        pass
        
    # 지원하지 않는 언어일 경우
    else:
        print("Language error\n언어오류\n\nModify the language settings of the setting.xml file(en/ko)\nsetting.xml 파일의 언어설정을 수정하세요(en/ko)")
        os.system("pause")
        exit()
        
    os.system("cls")

    # 메인 페이지
    sec=3
    while True:
        if language=="ko":
            loadmsg="[ %s ] 초 후 백신 테스트를 시작합니다." %sec
        else:
            loadmsg="Start the vaccine test in [ %s ] seconds." %sec
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
    %s
""" %(version, loadmsg))
        time.sleep(1)
        sec=sec-1
        os.system("cls")
        if sec==0:
            break
        else:
            pass
    if language=="ko":
        chackmsg="체크중. . .\n    백신 테스트 실행. . ."
    else:
        chackmsg="Checking. . .\n    Run a vaccine test. . ."
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
    num=0
    # 미끼파일 작성
    file = open(filename, 'w')
    file.write(fileinside)
    file.close()
    while True:
        try:
            file = open(filename, 'r')

        # 백신이 미끼파일의 권한을 바꿀 경우
        except PermissionError:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break
        
        # 미끼파일이 존재하지 않을 경우
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

        # 백신이 미끼파일 내부 글자를 수정했을 경우
        eicar=file.read()
        if not eicar==fileinside:
            if language=="ko":
                print("\n\n백신이 미끼파일을 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
            else:
                print("\n\nTime taken for the vaccine to detect and treat the decoy file : about [ %s ] seconds.\n" %num)
            break

        # Time Out (10초)
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

    # 미끼파일 삭제
    try:
        os.remove(filename)
    except PermissionError:
        pass
    except FileNotFoundError:
        pass
    except OSError:
        pass

    # 프로그램 종료
    if language=="ko":
        print("\n프로그램을 종료하시려면 아무키나 누르세요.")
    else:
        print("\nPress any key to exit the program.")
    os.system("pause>nul")
exit()
