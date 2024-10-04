#ifndef _TREZOR_T_H
#define _TREZOR_T_H

#define HSE_8MHZ

#define USE_SD_CARD 1
#define USE_I2C 1
#define USE_TOUCH 1
#define USE_SBU 1
#define USE_RGB_COLORS 1
#define USE_BACKLIGHT 1
#define USE_DISP_I8080_8BIT_DW 1
#define USE_PVD 1

#define DISPLAY_RESX 240
#define DISPLAY_RESY 240
#define DISPLAY_COLOR_MODE DMA2D_OUTPUT_RGB565
#define DISPLAY_LEGACY_HEADER "displays/st7789v.h"

#define DISPLAY_IDENTIFY 1
#define DISPLAY_TE_PORT GPIOD
#define DISPLAY_TE_PIN GPIO_PIN_12

#define BACKLIGHT_PWM_FREQ 10000
#define BACKLIGHT_PWM_TIM TIM1
#define BACKLIGHT_PWM_TIM_CLK_EN __HAL_RCC_TIM1_CLK_ENABLE
#define BACKLIGHT_PWM_TIM_AF GPIO_AF1_TIM1
#define BACKLIGHT_PWM_TIM_OCMODE TIM_OCMODE_PWM2
#define BACKLIGHT_PWM_TIM_CHANNEL TIM_CHANNEL_1
#define BACKLIGHT_PWM_TIM_CCR CCR1
#define BACKLIGHT_PWM_PIN GPIO_PIN_7
#define BACKLIGHT_PWM_PORT GPIOA
#define BACKLIGHT_PWM_PORT_CLK_EN __HAL_RCC_GPIOA_CLK_ENABLE

#define I2C_COUNT 1
#define I2C_INSTANCE_0 I2C1
#define I2C_INSTANCE_0_CLK_EN __HAL_RCC_I2C1_CLK_ENABLE
#define I2C_INSTANCE_0_CLK_DIS __HAL_RCC_I2C1_CLK_DISABLE
#define I2C_INSTANCE_0_PIN_AF GPIO_AF4_I2C1
#define I2C_INSTANCE_0_SDA_PORT GPIOB
#define I2C_INSTANCE_0_SDA_PIN GPIO_PIN_7
#define I2C_INSTANCE_0_SDA_CLK_EN __HAL_RCC_GPIOB_CLK_ENABLE
#define I2C_INSTANCE_0_SCL_PORT GPIOB
#define I2C_INSTANCE_0_SCL_PIN GPIO_PIN_6
#define I2C_INSTANCE_0_SCL_CLK_EN __HAL_RCC_GPIOB_CLK_ENABLE
#define I2C_INSTANCE_0_RESET_REG &RCC->APB1RSTR
#define I2C_INSTANCE_0_RESET_BIT RCC_APB1RSTR_I2C1RST
#define I2C_INSTANCE_0_EV_IRQHandler I2C1_EV_IRQHandler
#define I2C_INSTANCE_0_ER_IRQHandler I2C1_ER_IRQHandler
#define I2C_INSTANCE_0_EV_IRQn I2C1_EV_IRQn
#define I2C_INSTANCE_0_ER_IRQn I2C1_ER_IRQn
#define I2C_INSTANCE_0_GUARD_TIME 0

#define TOUCH_SENSITIVITY 0x06
#define TOUCH_I2C_INSTANCE 0
#define TOUCH_RST_PORT GPIOC
#define TOUCH_RST_PIN GPIO_PIN_5
#define TOUCH_INT_PORT GPIOC
#define TOUCH_INT_PIN GPIO_PIN_4
#define TOUCH_ON_PORT GPIOB
#define TOUCH_ON_PIN GPIO_PIN_10

#define SD_DETECT_PORT GPIOC
#define SD_DETECT_PIN GPIO_PIN_13
#define SD_ENABLE_PORT GPIOC
#define SD_ENABLE_PIN GPIO_PIN_0

// Ensure compatible hardware settings before jumping to
// the different booting stage. This function is used to
// ensure backward compatibility with older versions of
// released bootloaders and firmware.
#define ENSURE_COMPATIBLE_SETTINGS
extern void ensure_compatible_settings(void);

#endif  //_TREZOR_T_H
