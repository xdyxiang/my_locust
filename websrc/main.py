
from flask import Blueprint,render_template
import psutil


main=Blueprint('main',__name__,template_folder='templates1',static_folder='static1')
rootpath = main.root_path
@main.route('/')
def showinfo():
    infodict = {}
    cpu_count = psutil.cpu_count(logical=True)
    cpu_use = psutil.cpu_times_percent(percpu=True)
    mem = psutil.virtual_memory()
    memtotal = mem.total
    memavailable = mem.available
    memused = mem.used
    devs = psutil.disk_partitions()
    infodict["cpu_count"] = cpu_count
    infodict["cpu_use"] = cpu_use
    infodict["memtotal"] = memtotal
    infodict["memavailable"] = memavailable
    infodict["memused"] = memused
    infodict["devs"] = devs
    infodict["rootpath"] = rootpath
    return render_template('sourceinfo.html',infodict = infodict)
    # return 'main.hello'



