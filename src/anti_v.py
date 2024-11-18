import os
import hashlib

db = ['69a329523ce1ec88bf63061863d9cb14'
	'5d41402abc4b2a76b9719d911017c592']

def check (signature, efile):
    print(f"{signature}")
    if signature in db:
        print(f'Malicious {exe_file}')

file_list = os.listdir(".")
for exe_file in file_list:
    if ".exe" in exe_file:
        result = hashlib.md5(exe_file.encode())
        SIGNATURE = result.hexdigest()
        check(SIGNATURE, exe_file)