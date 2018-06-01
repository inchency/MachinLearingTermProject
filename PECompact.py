import os, subprocess

PACKER_PATH = "C:\\Users\\jack\\Desktop\\autopackingscript\\tools\\PECompact\\"
MAL_PATH = "C:\\Users\\jack\\Desktop\\노패킹exe"
OUT_PATH = "C:\\Users\\jack\\Desktop\\패킹아웃풋\\PECompact"

malfile_list = os.listdir(MAL_PATH)
cnt = 1
for x in malfile_list:
    mal_path = os.path.join(MAL_PATH, x)
    to_mal_path = os.path.join(OUT_PATH, x)
    # copy
    command = 'copy {from_mal} {to_mal}'.format(from_mal = mal_path, to_mal = to_mal_path)
    subprocess.run(command, shell=True)
    # packing
    command = '{pec2_path}pec2.exe {file}'.format(pec2_path = PACKER_PATH, file = to_mal_path)
    subprocess.run(command, shell=True)
    # 생성되는 pec2bac 삭제하기
    command = 'del {bac_path}.pec2bac'.format(bac_path = to_mal_path)
    subprocess.run(command, shell=True)
    print(cnt,"번째 파일 패킹 완료")
    cnt += 1
