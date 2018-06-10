import os

# IDA 경로
IDA_PATH = os.path.normpath('C:/Program Files/IDA 7.0/idat64.exe')

# malware 경로
MALWARE_PATH = os.path.normpath(os.path.abspath('./malware'))  #'D:\\패킹관련\패킹\\패킹4가지아웃풋\\mpress' #os.path.normpath(os.path.abspath('./malware'))

# ZIP FILE PATH
ZIP_FILE_PATH = os.path.normpath(os.path.abspath('./zipfile'))

# idb(i64) 저장 경로
IDB_PATH = os.path.normpath(os.path.abspath('./idb'))#'C:\\Users\\jack\\Desktop\\ida-master\\idb' # os.path.normpath(os.path.abspath('./idb'))

# ops 저장 경로
BOPS_PATH = os.path.normpath(os.path.abspath('./bops'))

# fops 저장 경로
FOPS_PATH = os.path.normpath(os.path.abspath('./fops'))

# ida python script 저장 경로
IDA_PYTHON_SCRIPT_PATH = os.path.normpath(os.path.abspath('./ida_script'))

# CPU COUNT
CPU_COUNT = 4