import os, subprocess

PACKER_PATH = "E:\\vmshare\\packer\\sePACK_0.01a\\sePACK.exe"
MAL_PATH = "E:\\vmshare\\s2"
OUT_PATH = "E:\\vmshare\\sepack"

malfile_list = os.listdir(MAL_PATH)
for x in malfile_list:
    mal_path = os.path.join(MAL_PATH, x)
    to_mal_path = os.path.join(OUT_PATH, x)
    command = '{packer_path} {from_mal} {to_mal}'.format(packer_path = PACKER_PATH , from_mal = mal_path, to_mal = to_mal_path)
    subprocess.run(command, shell=True)