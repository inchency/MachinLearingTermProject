import hashlib, pickle, os

bops_path = "D:\\패킹관련\\패킹\\pack_bops_everything"
fh_path = "D:\\패킹관련\\패킹\\pack_fh_everthing"
fh_size = 512
fh_index_max_size = 256
file_list = os.listdir(bops_path)

for x in file_list:
    full_path = os.path.join(bops_path, x)
    with open(full_path, 'rb') as f:
        data = pickle.load(f)
    fh = [0 for z in range(0, fh_size)]
    for func in data:
        for basicBlock in func:
            ops = ''
            for contents in basicBlock:
                ops += contents
            ops = ops.encode('utf-8') # string -> bytes
            md5Hash = hashlib.md5()
            md5Hash.update(ops)
            sha256Hash = hashlib.sha256()
            sha256Hash.update(ops)
            sha512Hash = hashlib.sha512()
            sha512Hash.update(ops)
            # hash의 Index 구하기
            hashIndex = md5Hash.hexdigest()
            hashIndex = int(hashIndex, base=16)
            hashIndex %= fh_size
            min = fh[hashIndex]
            plusIndex = hashIndex
            hashIndex = sha256Hash.hexdigest()
            hashIndex = int(hashIndex, base=16)
            hashIndex %= fh_size
            if(fh[hashIndex] < min):
                min = fh[hashIndex]
                plusIndex = hashIndex
            hashIndex = sha512Hash.hexdigest()
            hashIndex = int(hashIndex, base=16)
            hashIndex %= fh_size
            if (fh[hashIndex] < min):
                min = fh[hashIndex]
                plusIndex = hashIndex
            if(fh[plusIndex] < fh_index_max_size):
                fh[plusIndex] += 1
    fh = [z / fh_index_max_size for z in fh]
    # make .fh
    file_name = x.replace('bops', 'fh')
    with open(os.path.join(fh_path, file_name), 'wb') as f:
        pickle.dump(fh, f)
        print(file_name,"의 fh를 완료하였습니다.")
