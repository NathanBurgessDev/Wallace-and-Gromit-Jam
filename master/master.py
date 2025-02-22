import serial
import struct


ser = serial.Serial('COM4', 9600)

# ser.open()
ser.write(struct.pack('>I',128))
data = ser.read(4)
print(data)
print(struct.unpack('>I',data)[0])
print("Hello World")