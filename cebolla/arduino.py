import datetime
from dataclasses import dataclass

import serial

from cebolla.settings import DATA_LOG


@dataclass
class Packet:
    timestamp: str
    moisture1: float
    moisture2: float
    moisture3: float
    humidity: float
    temperature: float


def read_packet(ser: serial.Serial, port: str):

    eos, sos = False, False  # start of sequence, end of sequence
    message = []
    while not sos:
        newline = ser.readline()  # read a byte string
        string_n = newline.decode()  # decode byte string into unicode
        string = string_n.rstrip()  # remove \n and \r
        if string == "sos":
            sos = True
            now = str(datetime.datetime.now())
            message.append(now)

    while not eos:
        newline = ser.read_until(b"\n")  # read a byte string
        string_n = newline.decode()  # decode byte string into unicode
        string = string_n.rstrip()  # remove \n and \r
        if string == "eos":
            eos = True
        else:
            value = string.split(",")[-1]
            if value:
                message.append(float(value))

    packet = Packet(*message)
    return packet


def read_from_serial(port: str):
    with open(DATA_LOG, "a+") as f:
        ser = serial.Serial(port, 9600, timeout=0.5)
        i = 0
        while True:
            try:
                packet = read_packet(ser, port)
                print(
                    packet.timestamp,
                    packet.moisture1,
                    packet.moisture2,
                    packet.moisture3,
                    packet.humidity,
                    packet.temperature,
                    sep=",",
                    file=f,
                )
                print(
                    packet.timestamp,
                    packet.moisture1,
                    packet.moisture2,
                    packet.moisture3,
                    packet.humidity,
                    packet.temperature,
                    sep=",",
                )

            except Exception as e:
                i += 1
                print(f"Corrupted {i}: {e}")
        ser.close()


if __name__ == "__main__":
    packet = read_from_serial(port="/dev/ttyACM0")
