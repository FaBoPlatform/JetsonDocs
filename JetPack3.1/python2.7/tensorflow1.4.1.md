# Tensorflow 1.4.1 インストール
Jetson TX2 Docs>JetPack3.1>Python2.7>tensorflow1.4.1インストール
<hr>

# Tensorflow 1.4.1 インストール
```
wget https://raw.githubusercontent.com/peterlee0127/tensorflow-nvJetson/master/tensorflow-1.4.1-cp27-cp27mu-linux_aarch64.whl
sudo pip install --upgrade tensorflow-1.4.1-cp27-cp27mu-linux_aarch64.whl
```

# バージョン確認
```
python -c 'import tensorflow as tf; print(tf.__version__)'
```


Powered by [FaBo](http://www.fabo.io)