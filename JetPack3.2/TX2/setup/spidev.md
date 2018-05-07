# SPIdev 有効化
Jetson TX2 Docs>JetPack3.2>SPIdev有効化

###### メモ
* [PC] PCにダウンロードしたJetPack 3.2のDTBを編集する
* [PC] リカバリーモードでkernel-dtbをflashする
* [TX2] TX2でkernelソースコードをダウンロードする
* [TX2] TX2でspiドライバをコンパイルする
* [TX2] TX2でspiドライバをインストールする
* [TX2] reboot
* dd if=を使って取得したイメージは"FATAL ERROR: Blob has incorrect magic number"となりデコンパイル出来なくなっている
* kernel-dtb_bが追加されている

check cmmands
```
lsmod
ls /proc/device-tree/ | grep spi
cat /proc/modules
ls /dev/spi*
gdisk -l /dev/mmcblk0
```

## [PC] PCにダウンロードしたJetPack 3.2のDTBを編集する
* DTBバックアップ
* DTBデコンパイル
* DTB編集
* DTBコンパイル

#### DTBバックアップ
```
cd 64_TX2/Linux_for_Tegra/kernel/dtb/
# backup
cp tegra186-quill-p3310-1000-c03-00-base.dtb tegra186-quill-p3310-1000-c03-00-base.dtb.org
```

#### DTBデコンパイル
```
# decompile
../dtc -I dtb -O dts -o tegra186-quill-p3310-1000-c03-00-base.dts tegra186-quill-p3310-1000-c03-00-base.dtb
```
#### DTB編集
```
vi tegra186-quill-p3310-1000-c03-00-base.dts
```
spi@3240000 に「spidev@0」と「spidev@1」を書き加える
```
	spi@3240000 {
		compatible = "nvidia,tegra186-spi";
		reg = <0x0 0x3240000 0x0 0x10000>;
		interrupts = <0x0 0x27 0x4>;
		nvidia,dma-request-selector = <0x19 0x12>;
		#address-cells = <0x1>;
		#size-cells = <0x0>;
		#stream-id-cells = <0x1>;
		dmas = <0x19 0x12 0x19 0x12>;
		dma-names = "rx", "tx";
		nvidia,clk-parents = "pll_p", "clk_m";
		clocks = <0xd 0x4a 0xd 0x10d 0xd 0x261>;
		clock-names = "spi", "pll_p", "clk_m";
		resets = <0xd 0x2b>;
		reset-names = "spi";
		status = "okay";
		linux,phandle = <0x7d>;
		phandle = <0x7d>;
		spidev@0 {
			compatible = "spidev";
			reg = <0x0>;
			spi-max-frequency = <0x17d7840>;
		};

		spidev@1 {
			compatible = "spidev";
			reg = <0x1>;
			spi-max-frequency = <0x17d7840>;
		};
	};
```

#### DTBコンパイル
```
# compile
dtc -I dts -O dtb -o tegra186-quill-p3310-1000-c03-00-base.dtb tegra186-quill-p3310-1000-c03-00-base.dts
```


## [PC] リカバリーモードでkernel-dtbをflashする
Jetson TX2をリカバリモードで起動後、PCでflash.shを実行する。
```
cd 64_TX2/Linux_for_Tegra/
sudo ./flash.sh -r -k kernel-dtb jetson-tx2 mmcblk0p1
```

## [TX2] TX2でkernelソースコードをダウンロードする
```
sudo su
mkdir /compile
cd /compile
wget --no-check-certificate https://developer.nvidia.com/embedded/dlc/l4t-tx2-sources-28-2-ga -O l4t-tx2-sources-28-2-ga.tbz2
```

## [TX2] TX2でspiドライバをコンパイルする
```
cd /compile
tar -xvf l4t-tx2-sources-28-2-ga.tbz2
cd public_release

tar -xvf kernel_src.tbz2
cd kernel/kernel-4.4

zcat /proc/config.gz > .config
# less .configで内容を確認してから実行すること
sed -i 's/CONFIG_LOCALVERSION=""/CONFIG_LOCALVERSION="-tegra"/' .config
sed -i 's/# CONFIG_SPI_SPIDEV is not set/CONFIG_SPI_SPIDEV=m/' .config

make prepare
make modules_prepare
make M=drivers/spi/
```

## [TX2] TX2でspiドライバをインストールする
```
cp drivers/spi/spidev.ko /lib/modules/$(uname -r)/kernel/drivers
depmod
```

## [TX2] reboot
```
reboot
```

## check spidev
```
lsmod
```
>Module                  Size  Used by
>fuse                   82192  2
>mttcan                 48918  0
>bcmdhd               7441739  0
>can_dev                11882  1 mttcan
>spidev                  9920  0 ←これが出現した  
>pci_tegra              60038  0
>bluedroid_pm           11195  0
```
ls /dev/spi*
```
>/dev/spidev3.0  /dev/spidev3.1  

