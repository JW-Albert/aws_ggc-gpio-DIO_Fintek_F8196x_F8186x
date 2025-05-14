import os
import time
import ctypes
import lib.f81866 as f81866
import lib.f81866_gpio as gpio

# 初始狀態
val_lastTime = [1, 1, 1, 1]

def main():
    global val_lastTime

    os.setuid(0)
    if ctypes.CDLL("libc.so.6").iopl(3) != 0:
        print("錯誤：無法設定 I/O 權限（請確認使用 sudo）")
        return

    if f81866.init() != 0:
        print("錯誤：找不到 F81866 晶片")
        return

    gpio.init_gpio()

    print("讀取 GPIO 0~3 狀態：")
    for i in range(4):
        val = gpio.get_gpio_input(i)
        print(f"GPIO{i}: {val}")

    while True:
        val = [gpio.get_gpio_input(i) for i in range(4)]

        for i in range(4):
            if val[i] != val_lastTime[i]:
                print("State changed!")
                print("GPIO%d: %d -> %d" % (i, val_lastTime[i], val[i]))

                # 更新狀態
                val_lastTime = val

                break  # 只要有一個變化就離開 for-loop

        time.sleep(0.1)

if __name__ == "__main__":
    main()
