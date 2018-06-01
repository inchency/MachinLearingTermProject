import os, subprocess

PACKER_PATH = "C:\\Users\\jack\\Desktop\\autopackingscript\\tools\\mpress.219\\"
MAL_PATH = "C:\\Users\\jack\\Desktop\\노패킹exe"
OUT_PATH = "C:\\Users\\jack\\Desktop\\mpress"

malfile_list = os.listdir(MAL_PATH)
cnt = 1
for x in malfile_list:
    mal_path = os.path.join(MAL_PATH, x)
    to_mal_path = os.path.join(OUT_PATH, x)
    command = 'copy {from_mal} {to_mal}'.format(from_mal = mal_path, to_mal = to_mal_path)
    subprocess.run(command, shell=True)
    command = '{mpress_path}mpress.exe {file}'.format(mpress_path = PACKER_PATH, file = to_mal_path)
    subprocess.run(command, shell=True)
    print(cnt, "번째 파일 패킹 완료")
    cnt += 1