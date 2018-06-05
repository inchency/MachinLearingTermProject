import os, shutil

VIR_PATH = "Z:\\패킹관련\\패킹\\패킹완료"
EXE_PATH ="C:\\Users\\jack\\Desktop\\노패킹exe"

vir_list = os.listdir(VIR_PATH)
for x in vir_list:  
    vir_full_path = os.path.join(VIR_PATH,x)
    if(os.path.splitext(vir_full_path)[1] == '.vir'):
        temp = x.replace('.vir', '.exe')
        exe_full_path = os.path.join(EXE_PATH,temp)
        shutil.copy2(vir_full_path, exe_full_path)
        #print(vir_full_path, "에서", exe_full_path,"로 파일을 복사하였습니다.")
