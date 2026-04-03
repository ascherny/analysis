import re
import os

path = "0_protection.exe"
data = "0_protection_extracted.pck"

def extract_gdpc(path):
    with open(path, "rb") as f:
        data = f.read()
    
    magic = b"GDPC"
    start = data.find(magic)
    
    if start != -1:
        with open("0_protection_extracted.pck", "wb") as out:
            out.write(data[start:])
        print(".pck file successfully extracted!")
    else:
        print("GDPC signature not found in the .exe")
   
        
def read_gdpc(data):       
    with open(data, "rb") as f:
        data = f.read()
    os.makedirs("extracted", exist_ok=True)
    blocks = re.split(r'(\[gd_resource.+?\]|\[node.+?\]|\[ext_resource.+?\])', data.decode("utf-8", errors="ignore"))
    for i in range(0, len(blocks)-1, 2):
        with open(f"extracted/scene_{i}.txt", "w", encoding="utf-8") as out:
            out.write(blocks[i] + blocks[i+1])

read_gdpc(data)