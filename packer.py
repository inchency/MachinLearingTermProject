import os, subprocess, time

PACKER_PATH = 'E:\\data\\packing\\upx394w\\upx.exe'
MAL_PATH = 'E:\\data\\packing\\benign\\exe64'
OUT_PATH = 'E:\\data\\packing\\un_exe64'

malfile_list=os.listdir(MAL_PATH)
for x in malfile_list:
    mal_path = os.path.join(MAL_PATH, x)
    print(mal_path)
    command = '{packer} {file} -d -o {unpackfile}'.format(packer = PACKER_PATH, file = mal_path , unpackfile =os.path.join(OUT_PATH,x))
    subprocess.run(command)
