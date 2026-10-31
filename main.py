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
        ================================
        
        System: {platform.system()}
        
        Logical processors: {psutil.cpu_count(logical=True)} 
        Physical cores: {psutil.cpu_count(logical=False)}
        Current frequency: {round(psutil.cpu_freq().current / 1000, 2)} GHz
""")

#Потом доделать остальные показатели