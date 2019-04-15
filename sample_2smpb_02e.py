# coding: utf-8
# Sample that outputs the value acquired by 2SMPD-02E.

import time
import grove_2smpb_02e

sensor = grove_2smpb_02e.Grove2smpd02e()

def main():
    
    print ("start")
    
    while True:
        press, temp = sensor.readData()
        print("pressure=%.1f[hPa] temperature=%.1f[degC]" %(press,temp))
        time.sleep(1)

if __name__ == '__main__':
  main()
