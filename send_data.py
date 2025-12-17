from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# -------------------------------
# CONFIGURATION
# -------------------------------
token = "Evc6BO5o-jUvDafRtBejjp9V5gFalNLWB0G4UPp-0x956gyJq-Qlxvn0BomxBPA6iuBoCuFZBS8JBPSLo-MA8g=="
org = "myorg"
bucket = "mybucket"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# -------------------------------
# BOUCLE D'ENVOI DE DONNÉES
# -------------------------------
while True:
    # 1. Charge CPU (%)
    cpu_usage = random.uniform(100, 90)  # valeur simulée entre 10% et 90%
    point_cpu = Point("cpu").field("usage", cpu_usage)
    
    # 2. Température d’un capteur (°C)
    temp_sensor = random.uniform(20, 35)  # valeur simulée entre 20°C et 35°C
    point_temp = Point("temperature").field("value", temp_sensor)
    
    # 3. Taux d’erreur (%)
    error_rate = random.uniform(0, 5)  # valeur simulée entre 0% et 5%
    point_error = Point("error_rate").field("value", error_rate)
    
    # 4. Métrique simulée (ex: stock ou flux financier)
    metric_value = random.uniform(1000, 5000)
    point_metric = Point("metric").field("value", metric_value)
    
    # Envoi dans InfluxDB
    write_api.write(bucket=bucket, org=org, record=[point_cpu, point_temp, point_error, point_metric])
    
    print(f"Data sent: CPU={cpu_usage:.1f}%, Temp={temp_sensor:.1f}°C, Error={error_rate:.2f}%, Metric={metric_value:.2f}")
    
    time.sleep(1)  # pause 1 seconde
