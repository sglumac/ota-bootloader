cmake_minimum_required(VERSION 3.16)


set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)

set(CMAKE_C_STANDARD 11) #definirat koji c koristimo
set(CMAKE_C_COMPILER arm-none-eabi-gcc)# koji c compiler
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)# koji asm compiler


project(WIFI_OTA_2 C ASM)

set(MCU_FLAGS "-mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard")
set(CMAKE_C_FLAGS  "${MCU_FLAGS} -Wall -O2 -ffunction-sections -fdata-sections")
set(CMAKE_ASM_FLAGS "${MCU_FLAGS} -Wall -O2 -ffunction-sections -fdata-sections")
set(CMAKE_EXE_LINKER_FLAGS "${MCU_FLAGS} -T${CMAKE_SOURCE_DIR}/STM32CubeIDE/STM32L475VGTX_FLASH.ld -Wl,--gc-sections -specs=nosys.specs")




add_compile_definitions(USE_HAL_DRIVER
                        STM32L475xx)       

include_directories(${CMAKE_SOURCE_DIR}/Inc
                    ${CMAKE_SOURCE_DIR}/Common/Inc
                    ${CMAKE_SOURCE_DIR}/Drivers/BSP/B-L475E-IOT01
                    ${CMAKE_SOURCE_DIR}/Drivers/BSP/Components/Common
                    ${CMAKE_SOURCE_DIR}/Drivers/CMSIS/Device/ST/STM32L4xx/Include
                    ${CMAKE_SOURCE_DIR}/Drivers/CMSIS/Include
                    ${CMAKE_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Inc
                    )    

file(GLOB HAL_SOURCES ${CMAKE_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Src/*.c)
file(GLOB SRC ${CMAKE_SOURCE_DIR}/Src/*.c)
file(GLOB APPLICATION_STARTUP ${CMAKE_SOURCE_DIR}/STM32CubeIDE/Application/Startup/startup_stm32l475vgtx.s)
file(GLOB COMMON_SOURCES ${CMAKE_SOURCE_DIR}/Common/Src/*.c)

set(BSP_SOURCES ${CMAKE_SOURCE_DIR}/Drivers/BSP/B-L475E-IOT01/stm32l475e_iot01.c)


list(FILTER HAL_SOURCES EXCLUDE REGEX ".*_template\\.c$")


add_executable(WIFI_OTA_2   ${SRC} #tu je main.c
                                    ${HAL_SOURCES}
                                    ${APPLICATION_STARTUP}
                                    ${COMMON_SOURCES}
                                    ${BSP_SOURCES}
                                    # ${UTIL_SOURCES}
                                    )
                                    
# target_sources(WIFI_Client_Server PRIVATE ${CMAKE_SOURCE_DIR}/Src/usart_retarg.c)



set_target_properties(WIFI_OTA_2 PROPERTIES SUFFIX ".elf")


find_program(ARM_OBJCOPY arm-none-eabi-objcopy REQUIRED)
add_custom_command(TARGET WIFI_OTA_2 POST_BUILD
  COMMAND ${ARM_OBJCOPY} -O binary
          $<TARGET_FILE:WIFI_OTA_2>
          $<TARGET_FILE_DIR:WIFI_OTA_2>/WIFI_OTA_2.bin
  COMMENT "Generating WIFI_OTA_2.bin"
)
