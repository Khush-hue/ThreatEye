import pyshark
import pandas as pd

cap = pyshark.FileCapture("data/traffic.pcap")
data = []
last_time = None

for pkt in cap:
    try:
        curr_time = float(pkt.sniff_timestamp)
        delta = curr_time - last_time if last_time else 0
        last_time = curr_time
        data.append({
            'length': int(pkt.length),
            'protocol': pkt.highest_layer,
            'delta_time': delta
        })
    except:
        continue

df = pd.DataFrame(data)
df.to_csv("data/features.csv", index=False)
print("✅ Features extracted successfully! Saved as data/features.csv")