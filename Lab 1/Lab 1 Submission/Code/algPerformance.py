import sys
import os

iv = "fedcba9876543210"
key = "40fedf386da13d57"

fileArray = ["TestFile/test16.txt", "TestFile/test64.txt", "TestFile/test512.txt", "TestFile/test4096.txt",
             "TestFile/test32768.txt", "TestFile/test262144.txt", "TestFile/test2047152.txt"]

fileArrayRSA = ["TestFile/testRSA2.txt", "TestFile/testRSA4.txt", "TestFile/testRSA8.txt", "TestFile/testRSA16.txt",
                "TestFile/testRSA32.txt", "TestFile/testRSA64.txt"]


# Run code to test
# DES Algorithm
for i in fileArray:
    os.system("python tempdes.py " + iv + " " + key + " " + i + " output.des")

# RSA Algorithm
for i in fileArray:
    os.system("python tempaes.py " + i)

# AES Algorithm
for i in fileArrayRSA:
    os.system("python temprsa.py " + i)

# SHA1 Algorithm
for i in fileArray:
    os.system("python tempsha1.py " + i)

# HMAC Algorithm
for i in fileArray:
    os.system("python tempHMAC.py " + i)





