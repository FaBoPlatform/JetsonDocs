# I2C Fabo Shinobiモーター
Jetson TX2 Docs>JetPack3.1>I2C Fabo Shinobiモーター
<hr>

# Point
* rootユーザで実行する。

# 接続確認
Fabo Shinobiモーターを使う  
![](img/shinobi.jpg)  

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
60: -- -- -- 63 64 -- -- -- -- -- -- -- -- -- -- -- 
70: 70 -- -- -- -- -- -- --                         
```
Fabo Shinobiモーターには2つのモーターを制御するためのチップとしてDRV8830を2個搭載している。このチップのI2Cアドレスは0x63と0x64になる。<br>
アドレスが異なる場合はJetson TX2を一度シャットダウンしてJetson TX2とFaboシールドの電源ケーブルを抜く。<br>


# 実行
ソースコード：[sample_motor.py](sample_motor.py)
```
sudo python sample_motor.py
```

# 結果
モーターが動作する

Powered by [FaBo](http://www.fabo.io)