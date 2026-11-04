import psutil
import platform


print(f"""
        ================================
                    SENTINEL
                System Monitor v0.3
        ================================
        
        [ SYSTEM ]
        System: {platform.system()}
        
        [ PROCESSOR ]
        Logical processors: {psutil.cpu_count(logical=True)} 
        Physical cores: {psutil.cpu_count(logical=False)}
        Current frequency: {round(psutil.cpu_freq().current / 1000, 2)} GHz
        Used CPU: {psutil.cpu_percent(interval=1)}%
        
        [ MEMORY ]
        Total Memory: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB
        Available Memory: {round(psutil.virtual_memory().available / (1024 ** 3), 2)} GB
        Used Memory: {round(psutil.virtual_memory().used / (1024 ** 3), 2)} GB
        
        [ DISK ]
        Disk Total: {round(psutil.disk_usage("C:\\").total / (1024 ** 3), 2)} GB
        Disk Used: {round(psutil.disk_usage("C:\\").used / (1024 ** 3), 2)} GB
        Disk Free: {round(psutil.disk_usage("C:\\").free / (1024 ** 3), 2)} GB
""")

#В дальнейшем придумать что-то нормальное