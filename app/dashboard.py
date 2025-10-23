import os, subprocess

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

if __name__ == '__main__':
    app.run(debug=True)