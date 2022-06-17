"""
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""

import os
import shutil
import psutil
import emails
import subprocess
import re


def check_disk_usage(disk):
    """Returns True if free disk is less than 20%"""
    disk_usage = shutil.disk_usage(disk)
    free_disk_percent = disk_usage.free/disk_usage.total*100
    return free_disk_percent < 20


def check_cpu_usage():
    """Returns True if cpu usage is greater than 80%"""
    cpu_percent = psutil.cpu_percent(1)
    return cpu_percent > 80


def check_host():
    """Returns True if localhost not 127.0.0.1"""
    result = subprocess.run(["host", "127.0.0.1"], capture_output=True)
    regex = re.search(r"localhost", result[-1])
    return regex != None


def check_ram():
    """Returns True if free RAM is less than 500 MB"""
    ram_usage = dict(psutil.virtual_memory()._asdict())
    free_ram = float("{:.2f}".format(ram_usage['free']/ 1024 / 1024)) 
    return free_ram < 500


def email_err(subject):
    sender = "automation@example.com"
    to = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    emails.generate_email(sender, to, subject, body)
    emails.send_email()

def main():
    if check_ram():
        subject = "Error - Available memory is less than 500MB"
        email_err(subject)
    elif check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        email_err(subject)
    elif check_disk_usage():
        subject = "Error - Available disk space is less than 20%"
        email_err(subject)
    elif check_host():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        email_err(subject)


if __name__ == '__main__':
    main()
