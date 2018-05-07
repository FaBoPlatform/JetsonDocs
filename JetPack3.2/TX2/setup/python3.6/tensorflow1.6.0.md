# Tensorflow 1.6.0 インストール
Jetson TX2 Docs>JetPack3.2>Python3.6>tensorflow1.6.0インストール
<hr>

# Tensorflow 1.6.0 インストール
```
wget https://raw.githubusercontent.com/naisy/JetsonTX2/JetPack3.2_python3.6/JetPack3.2/python3.6/binary/tensorflow-1.6.0-cp36-cp36m-linux_aarch64.whl
sudo pip3 install --upgrade tensorflow-1.6.0-cp36-cp36m-linux_aarch64.whl
```

# バージョン確認
```
python -c 'import tensorflow as tf; print(tf.__version__)'
```


Powered by [FaBo](http://www.fabo.io)