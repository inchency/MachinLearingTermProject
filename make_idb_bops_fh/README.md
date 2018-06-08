# IDA

## 사용법
1. IDA Pro 를 설치한다
2. IDA Pro 를 방화벽 규칙에 추가 한다. ( 외부로 가는 것 차단 )
3. [settings.py](./settings.py) 에 있는 `IDA_PATH` 를 수정 한다.
4. [settings.py](./settings.py) 에 있는 `CPU_COUNT` 를 수정 한다.
5. [나스](http://203.246.112.134:5000/)에서 악성코드를 받아서 [zipfile](./zipfile)에 넣는다.
6. [preprocessing.py](./preprocessing.py)를 실행 시킨다.
7. [main.py](./main.py)를 실행 시킨다.

## 주의 사항
1. 처음 실행하기 전에 make_filename.py를 실행시켜주세요.

## 개발 사항

Version 1.0
* [settings.py](./settings.py) 에서 경로 수정 할 수 있도록 추가
* opcode 추출 하는 ida python 코드([opcode.py](./ida_script/opcode.py)) 추가

Version 1.1
* [settings.py](./settings.py) 에 사용할 CPU 코어 개수(`CPU_COUNT`) 설정 가능하도록 수정
* opcode 최근 수정일 기준으로 저장 되도록 수정
* 이미 idb(i64)파일이 존재 할 경우 새로 안만들 도록 수정

Version 1.2
* make_i64 파일명 make_idb로 수정
* opcode 최근 수정일 기준으로 저장 되는 기능 제거ㅊ
* idb(i64)파일 최근 수정일 기준으로 저장 되도록 수정
* opcode를 idb(i64)가 저장된 경로를 기준으로 분류 되도록 수정

Version 1.3
* 분석끝난 악성코드 파일 제거 하도록 수정
* malware 폴더에 있는 파일들 이름형식 수정하는 파일 추가 [make_filename.py](./make_filename.py)
* opcode 생성 안되던 오류 수정 ( join 함수 수정 )

Version 2.0
* 연구실에 맞게 수정

Version 2.1
* Feature Hashing 하는 기능 추가
* idb(i64)파일이 생성 안될 경우 에러 출력 하는 기능 추가

Version 2.2
* 예외 처리 추가

Version 2.3
* idb(i64)를 만드는 동시에 ops 파일 만들도록 수정 ( helped by [netju071](https://github.com/netju071) )
* 필요 없는 코드 정리 ( make_idb.py, make_ops.py )

Version 2.4
* 폴더 생성 되는 로직 변경

Version 3.0
* ida 실행 코드중 잘못된 부분 수정
* [make_idb_ops.py](./make_idb_ops.py) 와 [make_fh.py](./make_fh.py) 독립적으로 실행 가능 하게 수정
