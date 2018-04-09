# coding: utf-8 
import VL53L0X
import time

''' definition
class Vl53l0xAccuracyMode:
    GOOD = 0        # 33 ms timing budget 1.2m range
    BETTER = 1      # 66 ms timing budget 1.2m range
    BEST = 2        # 200 ms 1.2m range
    LONG_RANGE = 3  # 33 ms timing budget 2m range
    HIGH_SPEED = 4  # 20 ms timing budget 1.2m range
'''

mode = VL53L0X.Vl53l0xAccuracyMode.BEST
busnum = 1 # I2C Bus番号。DevKitの場合は1。Faboカスタムボードの場合は0

sensor1 = VL53L0X.VL53L0X(i2c_bus=busnum,i2c_address=0x29)
sensor1.open()
sensor1.start_ranging(mode)
timing = sensor1.get_timing()

if timing < 20000:
    timing = 20000

print("Timing %d ms" % (timing/1000))
    
for i in range(100):
    distance1 = sensor1.get_distance()

    if distance1 > 0:
        print("distance1 cm: {}".format(int(distance1/10)))
    time.sleep(timing/1000000.00)

sensor1.stop_ranging()
sensor1.close()
