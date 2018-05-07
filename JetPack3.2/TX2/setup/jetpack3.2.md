# JetPack3.2 インストール
Jetson TX2 Docs>JetPack3.2インストール
<hr>

Jetson TX2にOSをインストールするには、Ubuntu 16.04をインストールしたPCが必要となります。これをHostと呼びます。<br>

# 準備するもの
* ネットワーク、LANケーブル
* Jetson TX2 DevKit
* Ubuntu PC(WindowsはVMware Playerでも可)
* JetPack3.2 インストーラ(NVIDIAにユーザ登録が必要。[ダウンロード](https://developer.nvidia.com/embedded/jetpack))

# インストール方法
[公式のインストール方法](https://docs.nvidia.com/jetpack-l4t/index.html#developertools/mobile/jetpack/l4t/3.2/install.htm%3FTocPath%3D_____3)に沿ってインストールする。<br>

### 主なポイント
#### 5. Authenticate
ここでパスワードはUbuntu PCのrootユーザのパスワードになる。
#### 6. The Component Manager
Host-UbuntuのActionはno actionを選択すること。
#### 7. Accept the license
すべてにチェックを付けること。Accept Allにチェックを付ければ全てにチェックが付く。
#### 9. Device Information - Jetson TX2
ここは説明にある通り、わざわざFlash OSを選択肢から外していなければ表示されない。<br>
#### 11. Network Interface Selection
ここはVMware Playerの場合、仮想ネットワークデバイスもリストに出てくるが、eth0を選択すること。<br>
#### 13. Post Installation
リカバリーモードでJetson TX2を起動し、接続を確認する。<br>
説明にある通りに実行する。
1. TX2の電源を落とす。コンデンサの電力を消すためにACアダプタも抜く。
2. PCとTX2をUSBケーブルで繋ぐ。
3. ACアダプタを繋ぐ。
4. REC(リカバリー)ボタンを押しながらPWR(パワー)ボタンを押し、2秒くらいしたらRECボタンを離す。
5. TX2はリカバリーモードで起動しているので、lsusbで"NVidia Corp"があることを確認する。
6. エンターキーを押してインストールを開始する。

説明では4.は通常起動してからRECボタンを押しながらRST(リセット)ボタンを押すとあるが、RECボタンを押しながらPWRボタンを押してもよい。

エンターキーを押すとJetPack3.2のインストール(Jetson TX2へのUbuntuインストール、およびCUDA等のパッケージインストール)が始まる。30分位。

インストールが終わると、ターミナルを終了してくださいと表示されるが、ターミナルを閉じる前にTX2のIPアドレスを控えておきたい。<br>
IPアドレスが分からないとsshでログイン出来なくなるため、fing(Android/iOS/Windowsアプリ)でIPアドレスを調べるか、HDMIモニタを繋いでTX2にログインすることになる。


#### その他
SPIを有効化する場合はkernel-dtbをflashするために、ダウンロードしたJetPack 3.2が必要になるのでPCにデータを残しておく。


Powered by [FaBo](http://www.fabo.io)