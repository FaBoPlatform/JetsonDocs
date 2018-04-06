# CPUファン自動起動
Jetson TX2 Docs>JetPack3.1>CPUファン自動起動
<hr>


# Point
* daemonで用意することでOS起動時にCPUファンを起動します

# CPUファン自動起動
```
sudo cat <<EOF> /etc/init.d/cpufan
#!/bin/sh
### BEGIN INIT INFO
# Provides:         cpufan
# Required-Start:   $remote_fs $syslog
# Required-Stop:    $remote_fs $syslog
# Default-Start:    2 3 4 5
# Default-Stop:	    0 1 6
# Short-Description: CPU Fan launcher
### END INIT INFO

# Launch CPU Fan
sh -c 'echo 255 > /sys/kernel/debug/tegra_fan/target_pwm'
EOF

sudo chmod 755 /etc/init.d/cpufan
sudo update-rc.d cpufan defaults
```


Powered by [FaBo](http://www.fabo.io)