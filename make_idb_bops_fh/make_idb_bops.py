import os, subprocess

import multiprocessing as mp
import sys

from settings import *

SCRIPT_PATH = os.path.join(IDA_PYTHON_SCRIPT_PATH, 'bopcode.py')

def create_file_list ( root ) :
    ret_list = []
    for path, dirs, files in os.walk(root) :
        for file in files :
            full_file_path = os.path.join(path, file)
            ret_list.append(full_file_path)
    return ret_list

def make_idb_bops( file_path ) :
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    sub_file_path = file_path.replace(MALWARE_PATH, '').replace(os.path.basename(file_path), '')

    idb_save_path = IDB_PATH + sub_file_path
    bops_save_path = BOPS_PATH + sub_file_path

    if not os.path.exists(idb_save_path):
        os.makedirs(idb_save_path)

    if not os.path.exists(bops_save_path):
        os.makedirs(bops_save_path)

    dst_path = os.path.join(idb_save_path, file_name)
    bops_dst_path = os.path.join(bops_save_path, file_name) + '.bops'

    if os.path.exists(dst_path + '.i64') or os.path.exists(dst_path + '.idb') or os.path.exists(bops_dst_path):
        return

    command = '"{ida_path}" -c -o"{idb_path}" -A -S"{script_path} {bops_path}" -P+ "{malware_path}"'.format(ida_path=IDA_PATH, idb_path=dst_path, script_path=SCRIPT_PATH, bops_path=bops_dst_path, malware_path=file_path)
    try:
        subprocess.run(command)
        if os.path.exists(dst_path + '.i64') or os.path.exists(dst_path + '.idb'):
            print("{}을 성공적으로 분석하였습니다.".format(file_name))
            os.remove(file_path)
        else:
            print("{}을 분석하는데 실패하였습니다.".format(file_name))
    except:
        print("{}을 분석하는데 실패하였습니다.".format(file_name))

if __name__ == '__main__' :
    mp.freeze_support()
    file_list = create_file_list(MALWARE_PATH)
    print("Total Malware Count : {}".format(len(file_list)))
    p = mp.Pool(CPU_COUNT)
    p.map(make_idb_bops, file_list)

