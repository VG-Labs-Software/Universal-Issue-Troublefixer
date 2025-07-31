'''
Universal Issue Troublefixer
         by Nyther
'''
import random as rd
from time import sleep

print("Welcome to Nyther's Universal Issue Troublefixer")
sleep(0.5)
print()
print("Let's start troublefixing your issue...")
sleep(0.5)
print("Searching for issue...")
sleep(rd.uniform(0.8, 3))
print("Issue found!")
print("Looking up fixes...")
sleep(rd.uniform(0.8, 3))
print("Fix found! Initiating troubleshoot:")
sleep(0.5)
print()
inp = None
while inp is None or inp.lower() not in ("y", "n", "yes", "no"):
    inp = input("Have you already rebooted your PC? (Y/N)\n")
    print()
    if inp.lower() in ("y", "yes"):
        print("Issue cannot be resolved. Please throw away PC and aquire a new unit.")
    elif inp.lower() in ("n", "no"):
        print("Please restart your PC.")
    input()
    break
