import os
import time

if not os.path.exists("system/Real-time_inspection_test"):
    print("Please unzip the file properly and execute it.\n\nPress the ENTER key to exit the program.")
    os.system("pause")
    exit()

while True:
  if not os.path.exist("setting.xml"):
    print("""Please select language:
언어를 선택하세요:

1. English - 영어
2. 한글 - Korean

Please enter number (1/2)""")

os.system("title Real-time_inspection_test V.2.0")
os.system("mode.com con cols=120 lines=40")
num=0
os.system("cls")
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
    Version : V.1.0
    [ 3 ] 초 후 백신 테스트를 시작합니다.
""")
time.sleep(1)
os.system("cls")
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
    Version : V.1.0
    [ 2 ] 초 후 백신 테스트를 시작합니다.
""")
time.sleep(1)
os.system("cls")
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
    Version : V.1.0
    [ 1 ] 초 후 백신 테스트를 시작합니다.
""")
time.sleep(1)
os.system("cls")
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

#Core algorithm
file = open("EICAR.TXT", 'w')
file.write("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
file.close()
while True:
    if os.path.exists("EICAR.TXT"):
            try:
                file = open("EICAR.TXT", 'r')
            except PermissionError:
                print("\n\n백신이 가짜 바이러스를 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
                os.system("pause")
                exit()
            eicar=file.read()
            if not eicar=="X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*":
                print("\n\n백신이 가짜 바이러스를 탐지하고 치료하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
                file.close()
                os.remove("EICAR.TXT")
                os.system("pause")
                exit()
    else:
        print("\n\n백신이 가짜 바이러스를 탐지하고 제거하는데 걸린 시간 : 약 [ %s ] 초\n" %num)
        file.close()
        os.system("pause")
        exit()
    if num==10:
        file.close()
        os.remove("EICAR.TXT")
        print("\n\n백신이 가짜 바이러스를 탐지하고 치료/제거하는데 걸리는 시간이 [ 10 ] 초가 넘었습니다.\n백신의 상태를 다시 한번 확인해 주세요.")
        os.system("pause")
        exit()
    num=num+1
    file.close()
    time.sleep(1)
