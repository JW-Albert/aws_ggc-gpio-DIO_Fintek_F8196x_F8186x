import ctypes
from ctypes import c_ubyte
from pathlib import Path

# 載入 C 實作的共享函式庫
dll_path = Path(__file__).parent / "libf81866.so"
lib = ctypes.CDLL(dll_path)

# 綁定函式簽名
lib.f81866_unlock.argtypes = []
lib.f81866_unlock.restype = None

lib.f81866_lock.argtypes = []
lib.f81866_lock.restype = None

lib.f81866_read.argtypes = [c_ubyte]
lib.f81866_read.restype = c_ubyte

lib.f81866_write.argtypes = [c_ubyte, c_ubyte]
lib.f81866_write.restype = None

lib.f81866_set_logicdevice.argtypes = [c_ubyte]
lib.f81866_set_logicdevice.restype = None

lib.f81866_init.argtypes = []
lib.f81866_init.restype = ctypes.c_int

# Python 封裝函式
def unlock(): lib.f81866_unlock()
def lock(): lib.f81866_lock()
def read(reg): return lib.f81866_read(c_ubyte(reg))
def write(reg, val): lib.f81866_write(c_ubyte(reg), c_ubyte(val))
def set_logic_device(dev): lib.f81866_set_logicdevice(c_ubyte(dev))
def init(): return lib.f81866_init()
