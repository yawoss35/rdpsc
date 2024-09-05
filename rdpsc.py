import os
import subprocess

host = input("host: ")
user = input("user: ")
password = input("password: ")  

os.system(f"cmdkey /add:{host} /user:{user} /pass:{password}")
subprocess.run(f"mstsc /v:{host}", shell=True)
os.system(f"cmdkey /delete:{host}")
#bu kod windowsta çalışır