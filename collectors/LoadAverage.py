import os
from .base_collector import Collector

class LoadAverage(Collector):
    def collect(self):
        loadavg = os.getloadavg()
        print loadavg
