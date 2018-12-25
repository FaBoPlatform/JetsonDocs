UART

## Jetson Xavier

UARTのフォルダ

```
/dev/ttyTHS0
/dev/ttyTHS1
/dev/ttyTHS4
``` 
 
 J21端子8ピン(TX),10ピン(RX)が/dev/TTS0。
 J17 UART端子が/dev/TTYHS2。

## Sample

```
import serial
  
ser = serial.Serial('/dev/ttyTHS0', 115200)
ser.write("TEST".encode())
ser.close()
```