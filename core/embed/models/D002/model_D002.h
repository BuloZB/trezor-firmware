#ifndef MODELS_MODEL_DISC2_H_
#define MODELS_MODEL_DISC2_H_

#include "bootloaders/bootloader_hashes.h"
#include "sizedefs.h"

#define MODEL_NAME "D002"
#define MODEL_FULL_NAME "Trezor DIY 2"
#define MODEL_INTERNAL_NAME "D002"
#define MODEL_INTERNAL_NAME_TOKEN D002
#define MODEL_NAME_QSTR MP_QSTR_D002
#define MODEL_INTERNAL_NAME_QSTR MP_QSTR_D001
#define MODEL_USB_MANUFACTURER "Trezor DIY"
#define MODEL_USB_PRODUCT MODEL_FULL_NAME

/*** Discovery uses DEV keys in any build variant ***/
#define MODEL_BOARDLOADER_KEYS \
  (const uint8_t *)"\xdb\x99\x5f\xe2\x51\x69\xd1\x41\xca\xb9\xbb\xba\x92\xba\xa0\x1f\x9f\x2e\x1e\xce\x7d\xf4\xcb\x2a\xc0\x51\x90\xf3\x7f\xcc\x1f\x9d", \
  (const uint8_t *)"\x21\x52\xf8\xd1\x9b\x79\x1d\x24\x45\x32\x42\xe1\x5f\x2e\xab\x6c\xb7\xcf\xfa\x7b\x6a\x5e\xd3\x00\x97\x96\x0e\x06\x98\x81\xdb\x12", \
  (const uint8_t *)"\x22\xfc\x29\x77\x92\xf0\xb6\xff\xc0\xbf\xcf\xdb\x7e\xdb\x0c\x0a\xa1\x4e\x02\x5a\x36\x5e\xc0\xe3\x42\xe8\x6e\x38\x29\xcb\x74\xb6",

#define MODEL_BOOTLOADER_KEYS \
  (const uint8_t *)"\xd7\x59\x79\x3b\xbc\x13\xa2\x81\x9a\x82\x7c\x76\xad\xb6\xfb\xa8\xa4\x9a\xee\x00\x7f\x49\xf2\xd0\x99\x2d\x99\xb8\x25\xad\x2c\x48", \
  (const uint8_t *)"\x63\x55\x69\x1c\x17\x8a\x8f\xf9\x10\x07\xa7\x47\x8a\xfb\x95\x5e\xf7\x35\x2c\x63\xe7\xb2\x57\x03\x98\x4c\xf7\x8b\x26\xe2\x1a\x56", \
  (const uint8_t *)"\xee\x93\xa4\xf6\x6f\x8d\x16\xb8\x19\xbb\x9b\xeb\x9f\xfc\xcd\xfc\xdc\x14\x12\xe8\x7f\xee\x6a\x32\x4c\x2a\x99\xa1\xe0\xe6\x71\x48",

#define IMAGE_CHUNK_SIZE SIZE_256K
#define IMAGE_HASH_SHA256

#define DISPLAY_JUMP_BEHAVIOR DISPLAY_RESET_CONTENT
#define DISPLAY_RESX 240
#define DISPLAY_RESY 240

// SHARED WITH MAKEFILE, LINKER SCRIPT etc.
// misc
#define FLASH_START 0x0C004000
#define NORCOW_SECTOR_SIZE (8 * 8 * 1024)  // 64 kB

// FLASH layout
#define SECRET_START 0x0C000000
#define SECRET_MAXSIZE (2 * 8 * 1024)  // 8 kB
#define SECRET_SECTOR_START 0x0
#define SECRET_SECTOR_END 0x1

// overlaps with secret
#define BHK_START 0x0C002000
#define BHK_MAXSIZE (1 * 8 * 1024)  // 8 kB
#define BHK_SECTOR_START 0x1
#define BHK_SECTOR_END 0x1

#define BOARDLOADER_START 0x0C004000
#define BOARDLOADER_MAXSIZE (6 * 8 * 1024)  // 48 kB
#define BOARDLOADER_SECTOR_START 0x2
#define BOARDLOADER_SECTOR_END 0x7

#define BOARDCAPS_START 0x0C00FF00
#define BOARDCAPS_MAXSIZE 0x100

#define BOOTLOADER_START 0x0C010000
#define BOOTLOADER_MAXSIZE (16 * 8 * 1024)  // 128 kB
#define BOOTLOADER_SECTOR_START 0x8
#define BOOTLOADER_SECTOR_END 0x17

#define STORAGE_1_START 0x0C030000
#define STORAGE_1_MAXSIZE (8 * 8 * 1024)  // 64 kB
#define STORAGE_1_SECTOR_START 0x18
#define STORAGE_1_SECTOR_END 0x1F

#define STORAGE_2_START 0x0C040000
#define STORAGE_2_MAXSIZE (8 * 8 * 1024)  // 64 kB
#define STORAGE_2_SECTOR_START 0x20
#define STORAGE_2_SECTOR_END 0x27

#define FIRMWARE_START 0x0C050000
#define FIRMWARE_MAXSIZE (464 * 8 * 1024)  // 3712 kB
#define FIRMWARE_SECTOR_START 0x28
#define FIRMWARE_SECTOR_END 0x1F7
#define KERNEL_START 0x0C050000
#define KERNEL_MAXSIZE (512 * 1024)  // 512 kB
#define KERNEL_U_FLASH_SIZE 512

#define ASSETS_START 0x0C3F0000
#define ASSETS_MAXSIZE (8 * 8 * 1024)  // 64 kB
#define ASSETS_SECTOR_START 0x1F8
#define ASSETS_SECTOR_END 0x1FF

// RAM layout
#define KERNEL_U_RAM_SIZE 512
#define KERNEL_SRAM1_SIZE (16 * 1024)
#define KERNEL_SRAM2_SIZE (9 * 1024)
#define KERNEL_SRAM3_SIZE (750 * 1024)

#define BOOTARGS_SIZE 0x100
#define CODE_ALIGNMENT 0x400
#define COREAPP_ALIGNMENT 0x2000

#endif
