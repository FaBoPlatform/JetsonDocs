# coding: utf-8
import smbus2 as smbus
import time

class Motor():
    '''
    通電し続けている限り、DRV8830に書き込んだ値のパルスを送信し続けるため、
    値を一度書き込んだら値に変更があるまで放置でよい（無限ループで書き込み続ける必要はない）
    '''
    ## DRV8830 Default I2C address
    MOTOR_ADDR_L = 0x64
    MOTOR_ADDR_R = 0x63

    # DRV8830 Register Addresses
    COMMAND0 = 0x00

    ## Value motor.
    FORWARD = 0x01
    BACK = 0x02
    STOP = 0x00
    BRAKE = 0x03

    def __init__(self, busnum=1, motor_address=None):
        if motor_address is None:
            motor_address = self.MOTOR_ADDR_L
        self.bus = smbus.SMBus(busnum)
        self.MOTOR_ADDRESS = motor_address

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def forward(self, speed):
        '''
        前進する値は2bitで
        xxxx xx01 となる。(FORWARD = 0x01)
        後進する値は2bitで
        xxxx xx10 となる。(BACK = 0x02)
        停止する値は2bitで
        xxxx xx00 となる。(STOP = 0x00)
        ブレーキする値は2bitで
        xxxx xx11 となる。(BRAKE = 0x03)
        
        速度として使える値は1111 11 == 0011 1111 == 63まで。
        speed : 0-100
        '''
        if speed <= 0:
            print("value is under 0,  must define 1-100 as speed.")
            return
        elif speed > 100:
            print("value is over 100,  must define 1-100 as speed.")
            return
        direction = self.FORWARD
        s = self.map(speed, 1, 100, 1, 63)
        value = (s<<2) + direction # スピード値を2ビット左シフトして下位2bitに前進ビットを設定した1Byteの送信データを作成
        print("forward:{} {}".format(speed,value))
        self.bus.write_byte_data(self.MOTOR_ADDRESS,self.COMMAND0,value) #生成したデータを送信

    def stop(self):
        self.bus.write_byte_data(self.MOTOR_ADDRESS,self.COMMAND0,self.STOP) #モータへの電力の供給を停止

    def back(self, speed):
        if speed <= 0:
            print("value is under 0,  must define 1-100 as speed.")
            return
        elif speed > 100:
            print("value is over 100,  must define 1-100 as speed.")
            return
        direction = self.BACK
        s = self.map(speed, 1, 100, 1, 63)
        value = (s<<2) + direction # スピード値を2ビット左シフトして下位2bitに後進ビットを設定した1Byteの送信データを作成
        print("forward:{} {}".format(speed,value))
        self.bus.write_byte_data(self.MOTOR_ADDRESS,self.COMMAND0,value) #生成したデータを送信

    def brake(self):
        self.bus.write_byte_data(self.MOTOR_ADDRESS,self.COMMAND0,0x03) #モータをブレーキさせる


motor = Motor()
motor.foward(100)
time.sleep(2)
motor.stop()
time.sleep(2)
motor.back(100)
time.sleep(2)
motor.stop()
