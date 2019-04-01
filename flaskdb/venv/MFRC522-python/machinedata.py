import RPi.GPIO as GPIO
import MFRC522
import signal
import Read
import dht11

ID = Read.machinedata()
atm = dht11.i()

print(ID, atm)