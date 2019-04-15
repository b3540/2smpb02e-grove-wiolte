# 2smpb02e-grove-wiolte
オムロン製センサ 2SMPB-02E を MicroPythonで評価するためのモジュールとサンプルプログラム。

## 動作確認
* MicroPython on Wio LTE

## 使い方

* MicroPythonが動いているボードに `grove_2smpb_02e.py` をコピーします。
* `import grove_2smpb_02e`としてモジュールをインポートします。
* 2SMPB-02Eを接続したGroveのI2Cに対応する `machine.I2C` のインスタンスを作成します。
    * Wio-LTEの場合は `machine.I2C(1)`
* `bus`引数にI2Cのインスタンスを指定して `Grove2smpd02e`のインスタンスを作成します。
* `Grove2smpd02e.readData()`を呼び出すとセンサのデータが返ってきます。
    * `(temperature, humidity)`のtupleが返ってきます。

```Python
import grove_2smpb_02e
import machine

i2c = machine.I2C(1)
addr = i2c.scan()
sensor = grove_2smpb_02e.Grove2smpd02e(bus=i2c, address=addr[0])
print(sensor.readData())
```

## ライセンス
* 元はOMRONのRaspberry Pi用Pythonモジュール(MITライセンス)なので、変更後のコードもMITライセンスに従います。

### 元のコードのライセンス表記
Copyright (c) OMRON Corporation. All rights reserved.

このリポジトリはMITライセンスの下でライセンスされています。

