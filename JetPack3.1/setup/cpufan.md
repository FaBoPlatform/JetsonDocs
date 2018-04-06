# CPUファン起動
Jetson TX2 Docs>JetPack3.1>CPUファン起動
<hr>


# Point
* 再起動するたびに必要になります

# CPUファンを起動する
```
sudo sh -c 'echo 255 > /sys/kernel/debug/tegra_fan/target_pwm'
```


Powered by [FaBo](http://www.fabo.io)