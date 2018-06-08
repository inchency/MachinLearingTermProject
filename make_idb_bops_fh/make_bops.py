
import os, subprocess, sys

import multiprocessing as mp

from settings import *

SCRIPT_PATH = os.path.join(IDA_PYTHON_SCRIPT_PATH, 'bopcode.py')

def create_idb_list ( root ) :
    ret_list = []
    for path, dirs, files in os.walk(root) :
        for file in files :
            ext = os.path.splitext(file)[-1]
            if ext == '.i64' or ext == '.idb' :
                ret_list.append(os.path.join(path, file))
    return ret_list

def make_bops( file_path ) :
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    sub_file_path = file_path.replace(IDB_PATH,'').replace(os.path.basename(file_path), '')

    bops_save_path = BOPS_PATH + sub_file_path

    if not os.path.exists(bops_save_path):
        try :
            os.makedirs(bops_save_path)
        except :
            pass

    bops_dst_path = os.path.join(bops_save_path, file_name) + '.bops'

    if os.path.exists(bops_dst_path) :
        return

    command = '"{ida_path}" -A -S"{script_path} {bops_path}" "{idb_path}"'.format(ida_path=IDA_PATH, script_path = SCRIPT_PATH, bops_path = bops_dst_path, idb_path=file_path)
    print("bcommand : ", command)
    subprocess.run(command)

if __name__ == '__main__' :
    mp.freeze_support()
    file_list = create_idb_list(IDB_PATH)
    print("Total IDB Count : {}".format(len(file_list)))
    p = mp.Pool(CPU_COUNT)
    p.map(make_bops, file_list)