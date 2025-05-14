import os
import ctypes
import lib.f81866 as f81866

F81866_CFG_GPIO = 0x06

def get_gpio_input(index):
    index &= 7
    f81866.set_logic_device(F81866_CFG_GPIO)
    val = f81866.read(0x8A)
    return 1 if val & (1 << index) else 0

def set_gpio_output(index, value):
    index &= 7
    value = 1 if value else 0
    f81866.set_logic_device(F81866_CFG_GPIO)
    val = f81866.read(0x8A)
    val &= ~(1 << index)
    val |= (value << index)
    f81866.write(0x89, val)

def set_gpio_direction(index, mode):  # mode: 0=input, 1=output
    index &= 7
    mode = 1 if mode else 0
    f81866.set_logic_device(F81866_CFG_GPIO)
    val = f81866.read(0x88)
    val &= ~(1 << index)
    val |= (mode << index)
    f81866.write(0x88, val)

def init_gpio():
    f81866.set_logic_device(F81866_CFG_GPIO)
    val = f81866.read(0x30)
    f81866.write(0x30, val | 1)
    # 設定 GPIO4~7 為輸出
    for i in range(4, 8):
        set_gpio_direction(i, 1)
