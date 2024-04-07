import subprocess


data = "GOD "


data2send = ''.join(hex(ord(c))[2:] for c in data)
ping_count = 10


for _ in range(ping_count):
   out = subprocess.run(["ping", "-p", data2send, "-c", "1", "127.0.0.1"], capture_output=True, text=True)
   print(out.stdout)
