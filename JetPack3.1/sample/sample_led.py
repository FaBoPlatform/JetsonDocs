# coding: utf-8 
import FaBoGPIO_PCAL6408
import time

pcal6408 = FaBoGPIO_PCAL6408.PCAL6408()

# 指定したLED番号を点灯する
TARGET=0
pcal6408.setDigital(1<<TARGET, 1)

time.sleep(1)

# 指定したLED番号を消灯する
pcal6408.setDigital(1<<TARGET, 0)

