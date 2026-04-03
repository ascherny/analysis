# Пример кода для проверки магического числа версии Python
import importlib.util
import binascii

# Магическое число для текущей версии Python
magic = importlib.util.MAGIC_NUMBER
print(binascii.hexlify(magic).decode('ascii'))