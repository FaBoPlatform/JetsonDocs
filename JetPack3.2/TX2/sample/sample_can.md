# CAN サンプルコード
Jetson TX2 Docs>JetPack3.2>CANサンプルコード
<hr>

# Point
* 配線を正しく行う

# 接続確認
[CAN 有効化](../setup/can.md)を見てCANデバイスを正しく接続する

# 実行
can-utils(apt-get install can-utils)のcansendとcandumpを実行します。

受信ソースコード：[sample_candump.py](sample_candump.py)
```
python sample_candump.py
```

送信ソースコード：[sample_cansend.py](sample_cansend.py)
```
python sample_cansend.py
```

CANはマルチキャストなので、CANデバイスが1つしかない場合でも受信出来ます。<br>
その場合は送信と受信のCANデバイス番号を同じにしてください。<br>
>     cmd = "cansend can0 123#abcdabcd"  
>     cmd = "candump can0"  


# 出力
受信側に出力されます。
```
b'  can1  123   [4]  AB CD AB CD\n'
```




Powered by [FaBo](http://www.fabo.io)