import os, shutil

VIR_PATH = "D:\\패킹관련\\패킹\\PECompact_idb\\bops"
EXE_PATH ="D:\\패킹관련\\패킹\\PECompact_idb\\bops"

vir_list = os.listdir(VIR_PATH)
for x in vir_list:  
    vir_full_path = os.path.join(VIR_PATH,x)
    change = os.path.splitext(vir_full_path)[0]+'_PECompact.bops'
    exe_full_path = os.path.join(EXE_PATH,change)
    shutil.move(vir_full_path, exe_full_path)
