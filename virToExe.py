import os, shutil

VIR_PATH = "E:\\vmshare\\s2"
EXE_PATH ="E:\\vmshare\\s2"

vir_list = os.listdir(VIR_PATH)
for x in vir_list:  
    vir_full_path = os.path.join(VIR_PATH,x)
    if(os.path.splitext(vir_full_path)[1] == '.exe'):
        temp = x.replace('.exe','.vir')
        exe_full_path = os.path.join(EXE_PATH,temp)
        shutil.move(vir_full_path, exe_full_path)
        #print(vir_full_path, "에서", exe_full_path,"로 파일을 복사하였습니다.")
