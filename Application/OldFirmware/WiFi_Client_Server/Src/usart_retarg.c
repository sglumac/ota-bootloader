#include "stm32l4xx_hal.h"
#include <stdint.h>

extern UART_HandleTypeDef hDiscoUart;

int _write(int fd, const char *ptr, int len) {
  (void)fd;
  HAL_UART_Transmit(&hDiscoUart, (uint8_t*)ptr, (uint16_t)len, HAL_MAX_DELAY);
  return len;
}