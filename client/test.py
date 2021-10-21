from client import Client
import time

c1 = Client("Mantas")
c2 = Client("Tomas")

c1.send_message("hello")
time.sleep(1)
c2.send_message("hey")
time.sleep(1)
c1.send_message("how are you?")
time.sleep(1)
c2.send_message("not so bad, you?")
time.sleep(3)
c1.send_message("boring...")