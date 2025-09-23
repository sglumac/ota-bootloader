import socket


def tcp_client(host: str, port: int):
    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        full_file = b""
        print(f"Connecting to {host}:{port}...")
        s.connect((host, port))
        print("Connected! Type messages and press Enter. Type 'quit' to exit.\n")
        # arr = b"\x00\xAA\xBB\xCC\xDD\x00"
        try:
            while True:
                num = int(input("> "))
                message = b""
                if num == 0:
                    message = b"\x00\x48\x65\x6C\x6C\x6F"
                if num == 1:
                    with open("binaries/WIFI_OTA_2.bin", "rb") as f:  # ?????
                        while True:
                            chunk = f.read(512)
                            if not chunk:
                                break
                            if len(chunk) < 512:
                                chunk += b"\x00" * (512 - len(chunk))
                            message = b"\x01" + chunk
                            full_file += chunk
                            s.sendall(message)
                            data = s.recv(4096)
                            if not data:
                                print("Server closed the connection.")
                                break
                            print(f"Received: {data.decode(errors='replace')}")
                        continue

                if num == 2:
                    import binascii

                    checksum = binascii.crc32(full_file) & 0xFFFFFFFF
                    checksum_bytes = checksum.to_bytes(4, byteorder="little")
                    message = b"\x02" + checksum_bytes

                    full_file = b""
                    print(f"crc32 = {checksum:08x}")
                if num == 3:
                    import binascii

                    checksum = binascii.crc32(full_file) & 0xFFFFFFFF
                    checksum_bytes = checksum.to_bytes(4, byteorder="little")
                    checksum_bytes = b"\xFF" * 4 + checksum_bytes[4:]
                    message = b"\x02" + checksum_bytes

                    full_file = b""
                    print(f"crc32 = {checksum:08x}")

                if num == 4:
                    for i in range(12):
                        message = b"\x01" + b"\xAA" * 512
                        s.sendall(message)
                        data = s.recv(4096)
                        if not data:
                            print("Server closed the connection.")
                            break
                        print(f"Received: {data.decode(errors='replace')}")
                    continue
                if num == 5:
                    message = b"\xAA" * 5
                    s.sendall(message)

                    break

                # Send message
                s.sendall(message)

                # Receive response (up to 4 KB)
                data = s.recv(4096)

                if not data:
                    print("Server closed the connection.")
                    break
                print(f"Received: {data.decode(errors='replace')}")
                rec = data.decode(errors="replace")

        except KeyboardInterrupt:
            print("\nInterrupted by user, closing connection.")


if __name__ == "__main__":
    # Example: change to the IP/port of your server
    SERVER_IP = "192.168.214.184"
    SERVER_PORT = 8002
    tcp_client(SERVER_IP, SERVER_PORT)
