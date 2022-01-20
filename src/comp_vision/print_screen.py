# -*- coding: utf-8 -*-
import numpy as np
import mss


class PrintScreen:
    def __init__(self, targetMonitor=0):
        self.targetMonitor = targetMonitor

    def take(self):
        with mss.mss() as sct:
            monitor = sct.monitors[self.targetMonitor]
            sct_img = np.array(sct.grab(monitor))
            # The screen part to capture
            # monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

            # Grab the data
            return sct_img[:, :, :3]
