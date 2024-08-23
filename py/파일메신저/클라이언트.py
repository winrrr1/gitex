import socket  # 소켓 통신을 위한 모듈 임포트
import os  # 운영체제 관련 기능을 위한 모듈 임포트
import tkinter as tk  # GUI 생성을 위한 Tkinter 모듈 임포트
from tkinter import filedialog, messagebox  # 파일 대화상자와 메시지 박스 모듈 임포트

def send_file():
    filepath = filedialog.askopenfilename()  # 파일 선택 대화상자 열기
    if not filepath:
        return  # 선택한 파일이 없으면 함수 종료
    
    filesize = os.path.getsize(filepath)  # 파일 크기 가져오기
    filename = os.path.basename(filepath)  # 파일 이름 가져오기
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 클라이언트 소켓 생성 (IPv4, TCP)
    client_socket.connect(("192.168.0.109", 1004))  # 서버에 연결 (서버의 IP 주소와 포트로 변경)
    
    client_socket.send(f"{filename}:{filesize}".encode())  # 파일 이름과 파일 크기 전송
    
    with open(filepath, 'rb') as f:  # 파일을 읽기 모드로 열기
        bytes_sent = 0  # 전송한 바이트 수 초기화
        while bytes_sent < filesize:
            data = f.read(1024)  # 파일 데이터 읽기
            if not data:
                break  # 데이터가 없으면 루프 종료
            client_socket.sendall(data)  # 데이터 전송
            bytes_sent += len(data)  # 전송한 바이트 수 업데이트
    
    response = client_socket.recv(1024).decode()  # 서버로부터 응답 수신
    messagebox.showinfo("Info", response)  # 응답 메시지를 메시지 박스로 표시
    
    client_socket.close()  # 클라이언트 소켓 닫기

def client_gui():
    window = tk.Tk()  # Tkinter 윈도우 생성
    window.title("File Transfer Client")  # 윈도우 제목 설정
    
    send_button = tk.Button(window, text="Send File", command=send_file)  # 파일 전송 버튼 생성
    send_button.pack(pady=20)  # 버튼 배치 및 여백 설정
    
    window.mainloop()  # Tkinter 이벤트 루프 시작

if __name__ == "__main__":
    client_gui()  # 클라이언트 GUI 실행
