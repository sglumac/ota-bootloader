cmake_minimum_required(VERSION 3.16)


set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
set(CMAKE_C_COMPILER arm-none-eabi-gcc)
set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)



project(Bootloader_test C ASM)

set(MCU_FLAGS "-mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard")
set(CMAKE_C_FLAGS  "${MCU_FLAGS} -Wall -O2 -ffunction-sections -fdata-sections")
set(CMAKE_ASM_FLAGS "${MCU_FLAGS} -Wall -O2 -ffunction-sections -fdata-sections")
set(CMAKE_EXE_LINKER_FLAGS "${MCU_FLAGS} -T${CMAKE_SOURCE_DIR}/STM32L475VGTX_FLASH.ld -Wl,--gc-sections -specs=nosys.specs -specs=nano.specs")

set(CMAKE_C_STANDARD 11)

# set(CMAKE_C_COMPILER arm-none-eabi-gcc)# koji c compiler
# set(CMAKE_ASM_COMPILER arm-none-eabi-gcc)# koji asm compiler


add_compile_definitions(USE_HAL_DRIVER
                        STM32L475xx)       


include_directories(${CMAKE_SOURCE_DIR}/Core/Inc
                    ${CMAKE_SOURCE_DIR}/Drivers/CMSIS/Device/ST/STM32L4xx/Include
                    ${CMAKE_SOURCE_DIR}/Drivers/CMSIS/Include
                    ${CMAKE_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Inc
) 

file(GLOB CORE_SRC ${CMAKE_SOURCE_DIR}/Core/Src/*.c)
file(GLOB PROJECT_STARTUP ${CMAKE_SOURCE_DIR}/Core/Startup/startup_stm32l475vgtx.s)
file(GLOB HAL_SOURCES ${CMAKE_SOURCE_DIR}/Drivers/STM32L4xx_HAL_Driver/Src/*.c)


list(FILTER HAL_SOURCES EXCLUDE REGEX ".*_template\\.c$")

add_executable(Bootloader_test      ${CORE_SRC} #tu je main.c
                                    ${PROJECT_STARTUP}
                                    ${HAL_SOURCES}
                                    )

set_target_properties(Bootloader_test PROPERTIES SUFFIX ".elf")


find_program(ARM_OBJCOPY arm-none-eabi-objcopy REQUIRED)
add_custom_command(TARGET Bootloader_test POST_BUILD
  COMMAND ${ARM_OBJCOPY} -O binary
          $<TARGET_FILE:Bootloader_test>
          $<TARGET_FILE_DIR:Bootloader_test>/Bootloader_test.bin
  COMMENT "Generating Bootloader_test.bin"
)

# ./STM32_Programmer_CLI -c port=SWD -d  /home/student/Desktop/final_files1/tmp/STM32CubeIDe/Bootloader_test/Bootloader_Build/Bootloader_test.bin 0x08000000 -rst





