# I2C Fabo #509 PWMサーボ
Jetson TX2 Docs>JetPack3.2>I2C Fabo #509 PWMサーボ
<hr>

# Point
* rootユーザで実行する。
* PWM周波数は50Hzにする。
* サーボのケーブルは色が濃い方がGND(黒)。
* Fabo #509のPWM0がCHANNEL=0。
* Fabo #509のI2C Bus番号は1。これは#509のI2Cコネクタの配線がTX2のI2C Bus番号1に接続しているため固定値となる。

# 接続確認
Faboの#509 PWMサーボで確認する。  
![](img/servo.jpg)

# I2Cアドレスを確認する
```
sudo i2cdetect -y -r 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                         
```
Fabo #509にはPWMサーボを制御するためチップとしてPCA9685を搭載している。このチップのI2Cアドレスは0x40になる。<br>

アドレスが異なる場合はJetson TX2を一度シャットダウンしてJetson TX2とFaboシールドの電源ケーブルを抜く。<br>


# 実行
ソースコード：[sample_servo.py](sample_servo.py)
```
sudo python sample_servo.py
```

# 結果
サーボが左右に回転する。


Powered by [FaBo](http://www.fabo.io)