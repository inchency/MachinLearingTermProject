import os, subprocess, sys

import multiprocessing as mp

from settings import *

SCRIPT_PATH = os.path.join(IDA_PYTHON_SCRIPT_PATH, 'fopcode.py')

def create_idb_list ( root ) :
    ret_list = []
    for path, dirs, files in os.walk(root) :
        for file in files :
            ext = os.path.splitext(file)[-1]
            if ext == '.i64' or ext == '.idb' :
                ret_list.append(os.path.join(path, file))
    return ret_list

def make_fops( file_path ) :
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    sub_file_path = file_path.replace(IDB_PATH,'').replace(os.path.basename(file_path), '')

    fops_save_path = FOPS_PATH + sub_file_path

    if not os.path.exists(fops_save_path):
        try :
            os.makedirs(fops_save_path)
        except :
            pass

    fops_dst_path = os.path.join(fops_save_path, file_name) + '.fops'

    if os.path.exists(fops_dst_path) :
        return

    command = '"{ida_path}" -A -S"{script_path} {fops_path}" "{idb_path}"'.format(ida_path=IDA_PATH, script_path = SCRIPT_PATH, fops_path = fops_dst_path, idb_path=file_path)
    print("fcommand : ", command)
    subprocess.run(command)

if __name__ == '__main__' :
    mp.freeze_support()
    #file_list = create_idb_list(MALWARE_PATH)
    file_list = create_idb_list(IDB_PATH)
    print("Total IDB Count : {}".format(len(file_list)))
    p = mp.Pool(CPU_COUNT)
    p.map(make_fops, file_list)