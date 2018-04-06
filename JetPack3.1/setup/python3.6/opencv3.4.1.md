# OpenCV 3.4.1 インストール
Jetson TX2 Docs>JetPack3.1>Python3.6>OpenCV3.4.1インストール
<hr>

# パッケージインストール
```
sudo apt-get install -y build-essential cmake libeigen3-dev libatlas-base-dev gfortran git wget libavformat-dev libavcodec-dev libswscale-dev libavresample-dev ffmpeg pkg-config unzip qtbase5-dev libgtk-3-dev libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev v4l-utils liblapacke-dev libopenblas-dev checkinstall libgdal-dev libgphoto2-dev
```

# OpenCV 3.4.1 インストール
```
wget https://raw.githubusercontent.com/naisy/JetsonTX2/JetPack3.1_python3.6/JetPack3.1/python3.6/binary/opencv-3.4.1.deb
sudo dpkg -i opencv-3.4.1.deb
sudo ldconfig
```

# バージョン確認
```
python -c 'import cv2; print(cv2.__version__)'
```


Powered by [FaBo](http://www.fabo.io)