from dataclasses import dataclass

import serial

import move_pb2


@dataclass
class SerialConnection:
    connection: serial.Serial

    def __init__(self, address: str):
        self.connection = serial.Serial(address, 115200)

    def send_message(self, message: move_pb2.MoveTo):
        serialised = message.SerializeToString()
        self.connection.write(serialised)


if __name__ == "__main__":
    message = move_pb2.MoveTo()
    message.azimuth = 100
    message.altitude = 200
    message.accelRate = 300
    message.speedRate = 400

    SerialConnection("/dev/tty.usbmodem123456781").send_message(message)
