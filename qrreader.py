#!/usr/bin/python3
import sys, os, pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

#Simple encoder/decoder for qrcode 

print("[+] Encode (1)")
print("[+] Decode (2)")
cic = input("\nChoose 1 or 2: ")

os.system("cls" if os.name == "nt" else "clear")

#Encode
if cic=="1":
	inp = input("Type message for the QRCode: ")
	qr = pyqrcode.create(inp)
	ott = input("Output name: ")
	qr.png(ott + ".png", scale=8)
	print("\nSuccesfully created!")

#Decode also barcode qrcode etc.. (I will probably do a new update for gif file.)
elif cic=="2":
	dcd = input("Select the file to decode: ")
	d = decode(Image.open(dcd))
	print(d)



#error
elif cic !="":
	print("Type something")
	exit()
