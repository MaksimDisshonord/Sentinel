import psutil
import platform

#переменная хранит в себе метод измерения средней нагрузки на процессор интервалом в 1 секунду
cpu = psutil.cpu_percent(interval=1)

#переменная хранит в себе измерение нагрузки на оперативную память, percent какая доля ресурса используется в процентах
memory= psutil.virtual_memory().percent

# переменная хранит в себе вычисление заполнености диска C в процентах
disk = psutil.disk_usage("C:\\").percent

print(f"""
        ================================
                    SENTINEL
                System Monitor v0.2
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
""")

#Доделать диск