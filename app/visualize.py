import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/results.csv")
normal = df[df['anomaly']==1]
anomalies = df[df['anomaly']==-1]

plt.figure(figsize=(10,6))
plt.scatter(normal['length'], normal['delta_time'], s=10, label='Normal')
plt.scatter(anomalies['length'], anomalies['delta_time'], color='red', s=20, label='Anomaly')
plt.xlabel('Packet Length')
plt.ylabel('Δ Time')
plt.title('ThreatEye Anomaly Detection')
plt.legend()
plt.show()