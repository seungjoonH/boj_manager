# BoJ Problem Manager

> 백준 문제 풀이를 디렉토리별로 체계적으로 관리하고, VS Code로 바로 열거나 실행할 수 있는 간편 CLI 유틸리티 프로젝트

## 사용 언어

- Python
  - 문제 풀이 언어로 Python 3 사용
  - 모든 풀이 파일은 `.py` 확장자로 저장됨


## 📁 폴더 구조

문제 번호를 기준으로 다음과 같은 디렉토리 구조를 따릅니다:

``` 
./[만의 자리]/[천의 자리 2자리]/[문제 번호]/[풀이 번호].py 
```

**예시:**

``` 
./1/00/10000/1.py 
./0/01/1000/1.py 
```


## ⚙️ alias 설정

다음 두 alias를 `~/.zshrc` 또는 `~/.bashrc`에 추가하세요:

``` 
alias baek="bash /Users/seungjoonh/Documents/code/blog/baekjoon/boj.sh" 
alias stats="python3 /Users/seungjoonh/Documents/code/blog/baekjoon/stats.py" 
```

```sh
$ source ~/.zshrc
```


## 🚀 사용법

### 1. 문제 풀이 파일 생성

``` 
$ baek -c [문제번호] 
```

- 해당 문제 번호 디렉토리를 자동 생성
- 가장 마지막 풀이 번호 다음 번호의 파일(`n.py`)을 생성
- VS Code로 자동 오픈

**예시:**

``` 
$ baek -c 10000 
```
→ `./1/00/10000/1.py` 생성 및 열기


### 2. 기존 풀이 열기

``` 
$ baek -o [문제번호] [-n 풀이번호] 
```

- `-n`이 생략되면 가장 최신 풀이 자동 감지
- 원하는 풀이 번호를 직접 지정 가능

**예시:**

``` 
$ baek -o 10000         # 최신 풀이 자동 열기 
$ baek -o 10000 -n 2    # 2번 풀이 열기 
```


### 3. 풀이 실행 및 성능 측정

``` 
$ stats [문제번호]/[풀이번호] [-i 입력파일명] [-o 출력파일명] [-d 딜레이(ms)] [-t 제한시간(ms)] 
```

**기능 요약:**
- 파이썬 풀이 실행 + 실행 시간 + 메모리 사용량 측정
- 출력 중 `@`, stderr 중 `#` 발견 시 딜레이(`-d`) 적용
- 제한 시간(`-t`) 초과 시 자동 종료
- 실행 중 `q` 키 입력 시 수동 종료 가능

**예시:**

``` 
$ stats 10000/1                     # 표준 입력으로 실행 
$ stats 10000/1 -i sample           # input/sample.txt 로 실행 
$ stats 10000/1 -o result           # output/result.txt 로 저장 
$ stats 10000/1 -d 150              # @, # 출력 시 150ms 지연 
$ stats 10000/1 -t 3000             # 3초 제한시간 설정 
```


## 📤 stats 명령어 출력 예시

``` 
$ stats 10101/1 
```

``` 
==============================
INPUT (Ctrl+D to end):
< INPUT >
^D
==============================
OUTPUT:
< OUTPUT >
==============================
RUNTIME: 0.123456 s
PEAK MEMORY USAGE: 5.27 MB (5396.00 KB)
```

- `RUNTIME`: 전체 실행 시간 (초 단위)
- `PEAK MEMORY USAGE`: 최대 메모리 사용량 (MB/KB 동시 표시)
- 실행 중 `q` 키 입력 시 다음 메시지 출력:

``` 
[!] TERMINATED BY USER (q key)
```


## 📌 유의사항

- `code` 명령어가 작동하려면:
  - VS Code → `Cmd + Shift + P` →
  - `Shell Command: Install 'code' command in PATH` 실행 필요
- `Ctrl+D`: 표준 입력 종료
- `q` 키 입력 시 실행 즉시 종료됨
- `-o` 옵션 없이 실행하면 출력은 콘솔에 표시됨
- `-o` 옵션 사용 시 출력은 파일에만 저장됨


## 🏁 명령어 요약

``` 
$ baek -c 10000             # 새 풀이 생성
$ baek -o 10000             # 가장 최근 풀이 열기
$ baek -o 10000 -n 2        # 특정 풀이 열기
$ stats 10000/1             # 풀이 실행
$ stats 10000/1 -t 3000     # 3초 제한 시간 설정
$ stats 10000/1 -i test     # 입력 파일로 실행
$ stats 10000/1 -o out      # 출력 파일 저장
```