import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f : 
    read_lines = f.readlines()  #리스트의 형태로 넘겨줌
    
    for line in read_lines:
        line = line.strip()  #줄 마지막에 줄 바꿈 문자를 삭제합니다.
        print(line)