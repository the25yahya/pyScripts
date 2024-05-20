import psutil
import platform
from datetime import datetime

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["","K","M","G","","T","P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        
            
 #system info
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"system : {uname.system}")
print(f"node name : {uname.node}")
print(f"release : {uname.release}")
print(f"version :  {uname.version}")
print(f"machine : {uname.machine}")
print(f"Processor: {uname.processor}")
 
 #boot time
print("="*40, "Boot time", "="*40)
 
boot_time_timestamp = psutil.boot_time()
print(boot_time_timestamp)
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"boot time: {bt.year}/{bt.month}/{bt.day}/{bt.hour}/{bt.minute}/{bt.second}")

#cpu info
print("="*40, "CPU INFO", "="*40)
#numbers of core
print("Physical cores : ", psutil.cpu_count(logical=False))
print("Total cores: ", psutil.cpu_count(logical=True))

#cpu frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency : {cpufreq.max: .2f}Mhz")
print(f"Min Frequency : {cpufreq.min: .2f}Mhz")
print(f"Current Frequency {cpufreq.current: .2f}Mhz")

#cpu usage 
print("CPU Usage Per Core:")

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU usage: {psutil.cpu_percent()}%")


#memory info
print("="*40, "Memory Information", "="*40)
#get the memory details
svmen = psutil.virtual_memory()

print(f"Total: {get_size(svmen.total)}")
print(f"Available: {get_size(svmen.available)}")
print(f"Used: {get_size(svmen.used)}")
print(f"Percentage: {svmen.percent}%")
print("="*20, "SWAP", "="*20)

#get the swap memory details
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")


#disk Informatinon
print("="*40, "Disk Info", "="*40)
print("Partitions and usage :")
#get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"====Device: {partition.device}====")
    print(f"    Moutnpoint: {partition.mountpoint}")
    print(f"    File system type: {partition.fstype}")
    try :
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"    total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")

#network information 
print("="*40, "Network Information", "="*40)

#get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_adresses in if_addrs.items():
    for adress in interface_adresses:
        print(f"=== Interface: {interface_name}===")
        if str(adress.family) == 'AdressFamily.AF_INET':
            print(f"   IP ADRESS: {adress.address}")
            print(f"   NETMASK: {adress.netmask}")
            print(f"   BROADCAST IP: {adress.broadcast}")
        elif str(adress.family) == 'AdressFamily.AF_PACKET':
            print(f"   MAC ADRESS: {adress.address}")
            print(f"    NETMASK: {adress.netmask}")
            print(f" BROADCAST MAC: {adress.broadcast}")

#get IO stats since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes received: {get_size(net_io.bytes_recv)}")