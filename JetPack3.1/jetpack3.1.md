# JetPack3.1 インストール
Jetson TX2 Docs>JetPack3.1インストール
<hr>

Jetson TX2にOSをインストールするには、Ubuntu 14.04をインストールしたPCが必要となります。これをHostと呼びます。<br>
[TX1のフォーラム](https://devtalk.nvidia.com/default/topic/1021031/jetson-tx1/host-ubuntu-16-04-or-14-04-jetpack-3-1-install/)ではJetPack3.1のインストールはUbuntu 14.04がいいようですが、TX2は16.04でもインストール出来ました。

# 準備するもの
* ネットワーク、LANケーブル
* Jetson TX2 DevKit
* Ubuntu PC(WindowsはVMware Playerでも可)
* JetPack3.1 インストーラ(NVIDIAにユーザ登録が必要。[ダウンロード](https://developer.nvidia.com/embedded/jetpack-3_1))

# インストール方法
[公式のインストール方法](http://docs.nvidia.com/jetpack-l4t/index.html#developertools/mobile/jetpack/l4t/3.1/jetpack_l4t_install.htm)に沿ってインストールする。<br>

### 主なポイント
#### 5. Authenticate
ここでパスワードはUbuntu PCのrootユーザのパスワードになる。
#### 6. The Component Manager
Host-UbuntuのActionはno actionを選択すること。
#### 7. Accept the license
すべてにチェックを付けること。Accept Allにチェックを付ければ全てにチェックが付く。
#### 8. Device Information - Jetson TX2
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

エンターキーを押すとJetPack3.1のインストール(Jetson TX2へのUbuntuインストール、およびCUDA等のパッケージインストール)が始まる。30分位。

インストールが終わると、ターミナルを終了してくださいと表示されるが、ターミナルを閉じる前にTX2のIPアドレスを控えておきたい。<br>
IPアドレスが分からないとsshでログイン出来なくなるため、fing(Android/iOS/Windowsアプリ)でIPアドレスを調べるか、HDMIモニタを繋いでTX2にログインすることになる。

Powered by [FaBo](http://www.fabo.io)