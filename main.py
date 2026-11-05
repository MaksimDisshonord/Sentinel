import psutil
from rich.table import Table
from rich.live import Live


def make_table():
    table = Table(title="Sentinel")

    table.add_column("Parameter")
    table.add_column("Value")

    cpu(table)
    memory(table)
    disk(table)

    return table

def cpu(table):
    table.add_row("CPU Used",f"{psutil.cpu_percent(interval=1)}%")


def memory(table):
    table.add_row("Memory Used",f"{round(psutil.virtual_memory().used / (1024 ** 3), 2)} GB")



def disk(table):
    table.add_row("Disk Used",f"{round(psutil.disk_usage('C:\\').used / (1024 **  3), 2)} GB")


with Live(make_table()) as live:
    while True:
        live.update(make_table())


#Следовать задумкам-придумкам и мапе :)