from Phidget22.Phidget import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.ErrorCode import *
import time


class phidget_relay_class:
    def __init__(self, serial_num):
        self.ch = [DigitalOutput() for i in range(0, 8)]
        print(f'Assign relay board:{serial_num}')

        for i in range(0, 8):
            # Address, then open the channels
            self.ch[i].setChannel(i)
            self.ch[i].setDeviceSerialNumber(serial_num)
            self.ch[i].openWaitForAttachment(5000)
            # print(self.ch[i])

    def close(self):
        for i in range(0, 8):
            self.ch[i].close()

    def relay_switch(self, ch_num, state=0):
        n = 0
        retry_max = 3
        if state == 0:
            while (self.ch[ch_num].getState() != False) and (n < retry_max):
                self.ch[ch_num].setState(False)
                # time.sleep(0.1)
                n = n + 1
                # print(f'n:{n}')
        else:
            while (self.ch[ch_num].getState() != True) and (n < retry_max):
                self.ch[ch_num].setState(True)
                # time.sleep(0.1)
                n = n + 1
                # print(f'n:{n}')
        return self.ch[ch_num].getState()

    def relay_reset_all(self):
        for i in range(0, 8):
            self.relay_switch(i)

    def relay_set_all(self):
        for i in range(0, 8):
            self.relay_switch(i,1)

    def relay_self_test(self, delay=5, n_times=4):
        for j in range(0, n_times):
            self.relay_set_all()
            time.sleep(delay)
            self.relay_reset_all()
            time.sleep(delay)
