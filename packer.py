import os, subprocess, time

PACKER_PATH = 'C:\\Users\\jack\\Desktop\\upx394w\\upx.exe'
MAL_PATH = 'D:\\패킹관련\\패킹\\20171029'
OUT_PATH = 'D:\\패킹관련\\패킹\\패킹완료'

malfile_list=os.listdir(MAL_PATH)
for x in malfile_list:
    mal_path = os.path.join(MAL_PATH, x)
    print(mal_path)
    command = '{packer} {file} -d -o {unpackfile}'.format(packer = PACKER_PATH, file = mal_path , unpackfile =os.path.join(OUT_PATH,x))
    subprocess.run(command)
