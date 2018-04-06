# coding: utf-8
import Fabo_PCA9685
import smbus2 as smbus
import time


INITIAL_VALUE = 300
SERVO_HZ = 50 # PWM周期。60だと壊れるサーボがあるので50にしておく
CHANNEL = 0 # PCA9685 サーボ接続チャネル
BUSNUM = 1 # I2C bus番号

bus = smbus.SMBus(BUSNUM)

pca9685 = Fabo_PCA9685.PCA9685(bus, INITIAL_VALUE)
pca9685.set_hz(SERVO_HZ)

# サーボを動作させる
value=200
pca9685.set_channel_value(CHANNEL, value)
time.sleep(1)

value=400
pca9685.set_channel_value(CHANNEL, value)
time.sleep(1)

