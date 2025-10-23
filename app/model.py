import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/features.csv")
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df[['length','delta_time']])
df['anomaly'] = model.predict(df[['length','delta_time']])
df.to_csv("data/results.csv", index=False)
print("✅ Model trained & anomalies detected!")