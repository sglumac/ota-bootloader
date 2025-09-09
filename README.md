# STM32 B-L475E OTA Bootloader

This repository contains an **Over-The-Air (OTA) bootloader** for the  
[ST B-L475E-IOT01A](https://www.st.com/en/evaluation-tools/b-l475e-iot01a.html) IoT discovery board.

The bootloader allows the board to:

- Start a **TCP server** over the onboard Wi-Fi module  
- Receive a **binary firmware file** from a host (via Python client)  
- Store the binary in internal Flash memory  
- Jump to and run the newly received application  

This project demonstrates a minimal OTA update mechanism for IoT devices.

---

## Features

- TCP/IP server for binary transfer  
- Python client for sending firmware updates  
- Bootloader with application jump logic  
- Example application: **LED blink** in a custom pattern  
- Extensible design for future security and reliability improvements  

---

## Project Structure

```
.
├── Bootloader/       # Bootloader source code
├── Application/      # Example app (LED blink)
├── PythonClient/     # Python script for firmware upload
└── README.md
```

---

## Hardware Requirements

- **Board:** B-L475E-IOT01A  
- **Programmer:** ST-LINK/V2-1 (integrated on the board)  
- **Interface:** Onboard Wi-Fi (SPWF04SA module)  

---

## Usage

### 1. Flash the Bootloader
- Build the bootloader and flash it to the board at address `0x08000000`.  
- After reset, the bootloader initializes Wi-Fi and waits for a TCP connection on the configured port.  

### 2. Prepare an Application
- Build the application (e.g., LED blink).  
- Convert it to `.bin` format.  
- Place the binary file in the `Application/build/` folder.  

### 3. Send Firmware via Python Client
Run the client to push the binary to the board:

```bash
python3 PythonClient/send_binary.py --ip <board_ip> --port <port> --file Application/build/led_blink.bin
```

- The bootloader writes the binary to the application region (default `0x08020000`).  
- Once transfer completes, the bootloader jumps to the new application.  

---

## Configuration

- **Application start address:** `0x08020000`  
- **TCP port:** defined in `Bootloader/config.h`  
- **Wi-Fi SSID/password:** defined in `Bootloader/config.h`  

---

## Roadmap

- [ ] Add CRC32 integrity check  
- [ ] Implement dual-bank fail-safe update  
- [ ] Secure OTA with signatures and encryption  
- [ ] Add versioning and rollback support  

---

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.  

---

## Acknowledgments

- [STMicroelectronics STM32CubeL4](https://github.com/STMicroelectronics/STM32CubeL4)  
- STM32 community examples and application notes  
