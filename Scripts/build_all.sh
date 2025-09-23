# Final binaries destination
mkdir binaries
# Temporary build files
mkidr build_tmp


#Make the bootloader
cmake -S Bootloader/Bootloader_test -B Bootloader/Bootloader_test/build
cmake --build Bootloader/Bootloader_test/build
mv Bootloader/Bootloader_test/build/Bootloader_test.bin binaries/
rm -rf Bootloader/Bootloader_test/build/

cmake -S Application/OldFirmware/WiFi_Client_Server -B Application/OldFirmware/WiFi_Client_Server/build
cmake --build Application/OldFirmware/WiFi_Client_Server/build
mv Application/OldFirmware/WiFi_Client_Server/build/WIFI_Client_Server.bin binaries/
rm -rf Application/OldFirmware/WiFi_Client_Server/build/

cmake -S Application/NewFirmware/WIFI_OTA_2 -B Application/NewFirmware/WIFI_OTA_2/build
cmake --build Application/NewFirmware/WIFI_OTA_2/build
mv Application/NewFirmware/WIFI_OTA_2/build/WIFI_OTA_2.bin binaries/
rm -rf Application/NewFirmware/WIFI_OTA_2/build/

cp Application/addresses.bin binaries/addresses.bin






 
