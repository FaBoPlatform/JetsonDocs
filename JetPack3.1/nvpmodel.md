# NVPMODEL
Jetson TX2 Docs>JetPack3.1>NVPMODEL
<hr>

# Point
* ビルド時はアーキテクチャ最適化がかかるのでデフォルトの状態にする

# NVPMODEL
| Mode | Mode Name | Denver 2 | Frequency | ARM A57 | Frequency | GPU Frequency |
|:--|:--|:--|:--|:--|:--|:--|
| 0 | Max-N | 2 | 2.0 GHz | 4 | 2.0 GHz | 1.30 GHz |
| 1 | Max-Q | 0 | | 4 | 1.2 GHz | 0.85 GHz |
| 2 | Max-P Core-All | 2 | 1.4 GHz | 4 | 1.4 GHz | 1.12 GHz |
| 3 | Max-P ARM | 0 | | 4 | 2.0 GHz | 1.12 GHz |
| 4 | Max-P Denver | 2 | 2.0 GHz | 0 | | 1.12 GHz |

Max-N
```
sudo nvpmodel -m 0
sudo ./jetson_clocks.sh
```

Max-P ARM(Default)
```
sudo nvpmodel -m 3
sudo ./jetson_clocks.sh
```

Show current mode
```
sudo nvpmodel -q --verbose
```



Powered by [FaBo](http://www.fabo.io)