import shutil
import ctypes
# shutil.rmtree('non_exist_dir')

try:
    shutil.rmtree('non_exist_dir')
except WindowsError as e:
    print(e.errno)
    print(ctypes.FormatError(e.errno))
