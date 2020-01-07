import psutil
# ------------------------------------------------------------------------------------------------cpu
# cpu_count(logical=True)	获取CPU数量
# cpu_times(percpu=False)	获取不同状态下CPU运行时间
# cpu_percent(interval=None, percpu=False)	获取CPU使用率
# cpu_times_percent(interval=None, percpu=False)	获取CPU各状态占百分比

print(psutil.cpu_count(logical=True))   # 获取CPU数量
print(psutil.cpu_percent(interval=1,percpu=True))   # 获取CPU使用率 ，interval=1  一秒内
print(psutil.cpu_times_percent(percpu=True))    # 获取CPU各状态占百分比  ,percpu=True各个cpu数据
#CPU使用率：不加参数为上一次调用到现在使用率
print('1秒内CPU使用率：',psutil.cpu_percent(interval=0.1))
#3秒内每个CPU使用率
print('每个逻辑CPU使用率：',psutil.cpu_percent( percpu = True))
#CPU各个状态使用情况（百分比）
print('CPU 各个状态使用情况：',psutil.cpu_times_percent())   # 无参数则表示显示第一个cpu的情况


# -----------------------------------------------------------------------------------------------------内存
# psutil.virtual_memory	获取内存使用情况，不同系统返回值不同
# psutil.swap_memory()	获取swap内存使用情况
mem = psutil.virtual_memory()
print('系统内存：', mem)
print('总  内存：', mem.total)
print('空闲内存：', mem.available)
print('使用内存：', mem.used)
print('未使用内存：', mem.free)
print('内存使用率：', mem.percent)
print('swap 内存：', psutil.swap_memory())


# --------------------------------------------------------------------------------------------------------硬盘空间
# disk_partitions(all=False)	获取硬盘分区信息，返回分区列表
# disk_usage(path)	获取硬盘使用情况，path为路径
# disk_io_counters(perdisk=False, nowrap=True)	硬盘IO读取信息


#获取硬盘分区
devs = psutil.disk_partitions()
#显示硬盘信息：
print(devs)
#硬盘名称与挂载点，文件类型：
for dev in devs:
    print('硬盘名：%s, 挂载点：%s, 文件类型：%s'%(dev.device, dev.mountpoint, dev.fstype))

#根据前面打印信息G盘使用'G:\'表示
print(psutil.disk_usage('C:\\'))

import psutil
diskrw = psutil.disk_io_counters()
#diskrw为硬盘总的读写信息
print(diskrw)
diskrws = psutil.disk_io_counters(perdisk=True)
#diskrws为字典类型，表示每个分区读写信息，观察diskrw与diskrws值的关系
print(diskrws)


# ---------------------------------------------------------------------------------------------获取进程信息
# psutil.pids()	获取进程ID（每个进程都有唯一ID）
# psutil.Process(pid)	根据进程ID获取进程Process对象
#获取当前所有进程
pids = psutil.pids()
print(pids)
#获取ID为pids[0]的进程,
process = psutil.Process(pids[0])
print(process)
p = psutil.Process(0)
print('进程名称:', p.name())          #进程名称
print('运行状态:', p.status())        #当前状态
print('创建时间:', p.create_time())   #创建时间
print('CPU信息:',  p.cpu_times())     #进程的cpu时间信息,主要：user,system运行时间
print('内存信息:', p.memory_percent())#进程内存利用率
print('内存使用:', p.memory_info())   #进程内存使用详情
print('IO信息：', p.io_counters() )   #进程的IO信息,包括读写IO数字及参数
print('线程数：', p.num_threads() )   #进程开启的线程数
