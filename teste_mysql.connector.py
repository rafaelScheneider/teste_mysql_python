import psutil
import mysql.connector
import time

#percent_cpu = psutil.cpu_percent(interval=1)

#print(percent_cpu, "\n")

#part_disk = psutil.disk_partitions()

#print(part_disk, "\n")

#use_disk = psutil.disk_usage("/home")

#print(use_disk, "\n")

#use_RAM = (psutil.virtual_memory().used)/100

#print(use_RAM, "\n")

mydb_init = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="jonas"
)

mycursor_init = mydb_init.cursor()

#mycursor.execute("CREATE DATABASE jonas")

#print('executado!')
#mycursor.execute("CREATE TABLE registros (CPU_perc int, disk_use int, RAM_use int)")


def inserir(mycursor, mydb, percent_cpu, use_disk, use_RAM):
    sql = "INSERT INTO registros (CPU_perc, disk_use, RAM_use) VALUES (%s, %s, %s)"
    val = (round(percent_cpu), round(use_disk.percent), round(use_RAM))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def select(mycursor):
    mycursor.execute("SELECT * FROM registros")
    return mycursor.fetchall()

valor_range = 5

for i in range(0,valor_range):
    percent_cpu = psutil.cpu_percent(interval=1)
    part_disk = psutil.disk_partitions()
    use_disk = psutil.disk_usage("/home")
    use_RAM = (psutil.virtual_memory().used)/100

    inserir(mycursor_init, mydb_init, percent_cpu, use_disk, use_RAM)

    time.sleep(3)
retorno_valores = select(mycursor_init)


for i in range(0, valor_range):print(retorno_valores[i*-1])
