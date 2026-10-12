#14
#12.10.2026
#Animace kulicky ze strany na stranu
import math
import time
p = int(input("zadej pocet"))
print("Animace kuličky")
for i in range(p):
    print(" " * i + "O")
    time.sleep(0.1)
for i in range(p - 2, -1, -1):
        print(" " * i + "O")
        time.sleep(0.1)
for i in range(p):
      print("i", i * i, math.sqrt(i))