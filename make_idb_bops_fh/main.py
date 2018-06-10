# 국민대학교 정보보호 연구실을 위해 존재하는 피알
import time, subprocess

from settings import *

if __name__ == '__main__' :
    start = time.time()
    subprocess.run("python make_idb.py {}".format(MALWARE_PATH))
    print("{}".format(time.time() - start))
    #subprocess.run("python make_ops.py {}".format(IDB_PATH))
    #print("{}".format(time.time() - start))
    #subprocess.run("python make_fops.py {}".format(IDB_PATH))
    #print("{}".format(time.time() - start))
    subprocess.run("python make_bops.py {}".format(IDB_PATH))
    print("{}".format(time.time() - start))
    #subprocess.run("python make_fh.py {}".format(OPS_PATH))
    #print("{}".format(time.time() - start))
    #subprocess.run("python make_ffh.py {}".format(FOPS_PATH))
    #print("{}".format(time.time() - start))