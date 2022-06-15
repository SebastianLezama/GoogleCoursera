"""
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

import shutil
import psutil



def check_disk_usage(disk):
    """Returns True if free disk is less than 20%"""
    disk_usage = shutil.disk_usage(disk)
    free_disk_percent = disk_usage.free/disk_usage.total*100
    return free_disk_percent < 20


def check_cpu_usage():
    """Returns True if cpu usage is greater than 80%"""
    cpu_percent = psutil.cpu_percent(1)
    return cpu_percent > 80

