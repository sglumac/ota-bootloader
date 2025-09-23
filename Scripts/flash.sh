# Have stm_prog to STM32_Programmer_CLI executable and the board connected to SWD

stm_prog -c port=SWD -e all
stm_prog -c port=SWD -d binaries/WIFI_Client_Server.bin 0x08080000 -rst
stm_prog -c port=SWD -d binaries/addresses.bin 0x08070000 -rst
stm_prog -c port=SWD -d binaries/Bootloader_test.bin 0x08000000 -rst


