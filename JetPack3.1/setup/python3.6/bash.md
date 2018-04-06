# bash 設定
Jetson TX2 Docs>JetPack3.1>Python3.6>bash設定
<hr>

# Point
* CUDAライブラリパスを設定
* LANG設定

# ubuntuユーザ
```
sudo localedef -i en_US -f UTF-8 en_US.UTF-8

cat <<EOF>> /home/ubuntu/.bashrc

export PATH=/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/lib:
export __GL_PERFMON_MODE=1
export LANG="en_US.UTF-8"
export LC_ALL=$LANG
EOF
```

# rootユーザ
```
sudo cat <<EOF>> /root/.bashrc

export PATH=/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:/usr/local/lib:
export __GL_PERFMON_MODE=1
export LANG="en_US.UTF-8"
export LC_ALL=$LANG
EOF
```

設定したら再ログインもしくはsource ~/.bashrcで再読み込み



Powered by [FaBo](http://www.fabo.io)