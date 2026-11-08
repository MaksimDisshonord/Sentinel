import psutil
from rich.table import Table
from rich.live import Live
from rich.console import Group


def make_table():
    table = Table(title="SENTINEL SYSTEM MONITOR")
    table_cpu = Table(title="Processor")
    table_memory = Table(title='Memory')
    table_disk = Table(title='Disk')

    table_cpu.add_column("Parameter")
    table_cpu.add_column("Value")

    table_memory.add_column("Parameter")
    table_memory.add_column("Value")

    table_disk.add_column("Parameter")
    table_disk.add_column("Value")

    group = Group(table_cpu, table_memory, table_disk,)

    cpu(table_cpu)
    memory(table_memory)
    disk(table_disk)

    return group

def cpu(table):
    table.add_row("CPU Used",f"{psutil.cpu_percent(interval=1)}%")
    table.add_row("Logical processors",f"{psutil.cpu_count(logical=True)}")
    table.add_row("Physical processors",f"{psutil.cpu_count(logical=False)}")


def memory(table):
    table.add_row("Memory Used",f"{round(psutil.virtual_memory().used / (1024 ** 3), 2)} GB")


def disk(table):
    table.add_row("Disk Total", f"{round(psutil.disk_usage("C:\\").total / (1024 ** 3), 2)} GB")
    table.add_row("Disk Free", f"{round(psutil.disk_usage("C:\\").free / (1024 ** 3), 2)} GB")
    table.add_row("Disk Used", f"{round(psutil.disk_usage('C:\\').used / (1024 ** 3), 2)} GB")


with Live(make_table()) as live:
    while True:
        live.update(make_table())


#Следовать задумкам-придумкам и мапе :)