import socket  # 소켓 통신을 위한 모듈 임포트
import threading  # 멀티쓰레딩을 위한 모듈 임포트
import tkinter as tk  # GUI 생성을 위한 Tkinter 모듈 임포트
from tkinter import filedialog, messagebox  # 파일 대화상자와 메시지 박스 모듈 임포트

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 서버 소켓 생성 (IPv4, TCP)
    server_socket.bind(("0.0.0.0", 1004))  # 모든 인터페이스에서 5000 포트로 바인딩
    server_socket.listen(5)  # 최대 5개의 연결 대기
    
    print("Server started, waiting for connections...")  # 서버 시작 메시지 출력

    while True:
        client_socket, addr = server_socket.accept()  # 클라이언트 연결 수락
        print(f"Connection from {addr} has been established.")  # 연결된 클라이언트 주소 출력
        threading.Thread(target=handle_client, args=(client_socket,)).start()  # 클라이언트 처리용 쓰레드 시작

def handle_client(client_socket):
    while True:
        file_info = client_socket.recv(1024).decode()  # 클라이언트로부터 파일 정보 수신
        if not file_info:
            break  # 파일 정보가 없으면 루프 종료
        
        filename, filesize = file_info.split(':')  # 파일 이름과 파일 크기 분리
        filesize = int(filesize)  # 파일 크기를 정수로 변환
        
        with open(filename, 'wb') as f:  # 수신한 파일을 저장할 파일 열기 (쓰기 모드)
            bytes_received = 0  # 수신한 바이트 수 초기화
            while bytes_received < filesize:
                data = client_socket.recv(1024)  # 파일 데이터 수신
                if not data:
                    break  # 데이터가 없으면 루프 종료
                f.write(data)  # 수신한 데이터를 파일에 쓰기
                bytes_received += len(data)  # 수신한 바이트 수 업데이트
        
        print(f"File {filename} received successfully.")  # 파일 수신 성공 메시지 출력
        client_socket.send("File received successfully.".encode())  # 클라이언트에 성공 메시지 전송
    
    client_socket.close()  # 클라이언트 소켓 닫기

def start_server_thread():
    server_thread = threading.Thread(target=start_server)  # 서버 시작용 쓰레드 생성
    server_thread.daemon = True  # 데몬 쓰레드로 설정
    server_thread.start()  # 서버 쓰레드 시작

def server_gui():
    window = tk.Tk()  # Tkinter 윈도우 생성
    window.title("File Transfer Server")  # 윈도우 제목 설정
    
    start_button = tk.Button(window, text="Start Server", command=start_server_thread)  # 서버 시작 버튼 생성
    start_button.pack(pady=20)  # 버튼 배치 및 여백 설정
    
    window.mainloop()  # Tkinter 이벤트 루프 시작

if __name__ == "__main__":
    server_gui()  # 서버 GUI 실행
