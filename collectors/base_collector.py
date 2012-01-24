class Collector(object):
    def collect(self):
        raise NotImplementedError

    def __call__(self):
        return self.collect()

