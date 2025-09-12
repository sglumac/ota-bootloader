import socket


def tcp_client(host: str, port: int):
    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with open("blinky_linked.bin", "rb") as f:
            print(f"Connecting to {host}:{port}...")
            s.connect((host, port))
            print("Connected! Type messages and press Enter. Type 'quit' to exit.\n")
            arr = b"\x00\xAA\xBB\xCC\xDD\x00"
            try:
                while True:
                    num = int(input("> "))
                    message = b""
                    if num == 0:
                        message = b"\x00\x48\x65\x6C\x6C\x6F"
                    if num == 1:
                        while True:
                            chunk = f.read(512)
                            if not chunk:
                                break
                            message = b"\x01" + chunk
                            s.sendall(message)
                            data = s.recv(4096)
                            if not data:
                                print("Server closed the connection.")
                                break
                            print(f"Received: {data.decode(errors='replace')}")
                        continue

                    if num == 2:
                        message = b"\x02\x42\x79\x65\x2E"

                    # Send message
                    s.sendall(message)

                    # Receive response (up to 4 KB)
                    data = s.recv(4096)

                    if not data:
                        print("Server closed the connection.")
                        break
                    print(f"Received: {data.decode(errors='replace')}")
                    rec = data.decode(errors="replace")
                    if "Finished." in rec:
                        print("Finished transfer")
                        break
                    elif "Confirm." not in rec:
                        print(f"BAD RECEPTION")
                        break

            except KeyboardInterrupt:
                print("\nInterrupted by user, closing connection.")


if __name__ == "__main__":
    # Example: change to the IP/port of your server
    SERVER_IP = "192.168.99.184"
    SERVER_PORT = 8002
    tcp_client(SERVER_IP, SERVER_PORT)
