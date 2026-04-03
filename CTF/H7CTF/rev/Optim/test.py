"""
Формула шифрования c = (b + factorial(i)) % 137

b от 0 до 256
factorial - факториал позиции

с = сумма по модулю 137 -> не больше 136


Для дешифра мы вычитаем из b % 136 f % 136

f % 136 может оказаться больше b % 

если f > c то надо прибавить к c 136

EXAMPLE:
Пусть b = 50
factorial(6) = 720

 c = (50 + 720) % 137 = 770 % 137
137 * 5 = 685
770 - 685 = 85

с = 85

f_mod = 720 % 137 = 35
b_recovered = (c - f_mod + 137) % 137 = (85 - 35 + 137) % 137 = 187 % 137 = 50


c = (120 + 130) % 137
c = 250 % 137
250 - 137 = 113

b_candidate = c - f_mod = 113 - 130 = -17
b_recovered = b_candidate + mod = -17 + 137 = 120

"""



with open('flag.enc', "rb") as f:
    encrypted_data = bytearray(f.read())

mod = 0x89

"""Задаем массив факториалов по модулю (как и было в enc) размером с файл"""
factorials = [1] * len(encrypted_data)
for i in range(1, len(encrypted_data)):
    factorials[i] = (factorials[i-1] * i) % mod


"""Вычитаем факториал обращая шифрование"""
decrypted_data = bytearray()
for i in range(len(encrypted_data)):
    result = encrypted_data[i] - factorials[i] #
    if result < 0:
        result += mod
    decrypted_data.append(result % 256)  

with open('flag.zip', "wb") as f:
    f.write(decrypted_data)


#H7CTF{451ab9e0c8548140b84b5d703e285efc}
H7CTF{nBqvn7LpG+iRRABKO/uHcZ/mFuCTCGQQXoozH+34uWm6yspl6ZaTEcnwHMC4p+/Q}