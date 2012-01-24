from apscheduler.scheduler import Scheduler
import yaml
import sys
import inspect
import signal

def load_class_from_name(fqcn):
    # Break apart fqcn to get module and classname
    paths = fqcn.split('.')
    modulename = '.'.join(paths[:-1])
    classname = paths[-1]
    # Import the module
    mod = __import__(modulename, globals(), locals(), ['*'])
    # Get the class
    cls = getattr(sys.modules[modulename], classname)
    # Check cls
    if not inspect.isclass(cls):
        raise TypeError, "%s is not a class" % (fqcn)
    # Return class
    return cls

sched = Scheduler(daemonic=True)
sched.start()

config_file = open('etc/default.yaml', 'r')
cfg = yaml.load(config_file)
jobs = cfg['Jobs']
print jobs

for job, params in jobs.items():
    cls = load_class_from_name(job)
    inst = cls()
    sched.add_interval_job(inst, seconds=params['interval'])



signal.pause()   
