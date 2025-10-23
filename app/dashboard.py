import os, subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("✅ Flask app starting... BASE_DIR =", BASE_DIR)

data_path = os.path.join(BASE_DIR, "data", "results.csv")
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    df = pd.DataFrame()

if not os.path.exists("data/results.csv"):
    print("⚠️ results.csv not found — running extractor & model...")
    subprocess.run(["python3", "app/extractor.py"])
    subprocess.run(["python3", "app/model.py"])


from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv("data/results.csv")
    total = len(df)
    anomalies = len(df[df['anomaly']==-1])
    percent = (anomalies/total)*100
    return render_template_string("""
    <h1 style='text-align:center;'>ThreatEye Dashboard</h1>
    <p style='text-align:center;'>Total Packets: {{total}}</p>
    <p style='text-align:center;'>Anomalies: {{anomalies}} ({{percent}}%)</p>
    <p style='text-align:center;color:red;'>⚠️ Monitoring Encrypted Traffic for Suspicious Patterns</p>
    """, total=total, anomalies=anomalies, percent=round(percent,2))

if __name__ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    print("✅ Starting Flask on port", port)
    app.run(host="0.0.0.0", port=port, debug=False)