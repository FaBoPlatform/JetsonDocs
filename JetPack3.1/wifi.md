# WiFi 設定
Jetson TX2 Docs>JetPack3.1>WiFi設定
<hr>


# WiFi IP固定設定
WiFiルーターへの接続方法が<br>
SSID:MySSID<br>
PASS:MyPassword<br>
の時、wpa_pasphraseコマンドを実行します。
```
wpa_passphrase 'MySSID' 'MyPassword'
```
出力
```
network={
	ssid="MySSID"
	#psk="MyPassword"
	psk=a66e97b9a1008a97285c78c2b95082bed3541d3dd01165b0128f7f3c18563797
}
```
pskの値を用いて以下のファイルを作成します。<br>
IPアドレスを192.168.0.200に固定する例：<br>
```
sudo vi /etc/network/interfaces.d/wlan0_static
sudo chmod 600 /etc/network/interfaces.d/wlan0_static
```
wlan0_staticの中身
```
auto wlan0
iface wlan0 inet static
    address 192.168.0.200
    netmask 255.255.255.0
    broadcast 192.168.0.255
    gateway 192.168.0.100
    dns-nameservers 8.8.8.8
    wpa-ssid "MySSID"
    wpa-psk a66e97b9a1008a97285c78c2b95082bed3541d3dd01165b0128f7f3c18563797
```
もう一つファイルを書き換えます。
```
sudo vi /etc/network/interfaces
```
interfacesの中身
```
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

# This line is a custom edit.
source interfaces.d/wlan0_static
```
ネットワークを再起動
```
/etc/init.d/networking restart
```
再起動をかけたらLANケーブルを抜いて指定したIPアドレスにSSHでログインします。


Powered by [FaBo](http://www.fabo.io)