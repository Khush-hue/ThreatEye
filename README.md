🛰️ Network Analyzer Dashboard

An intelligent web-based network monitoring tool built with Flask, Scikit-learn, and Pandas — designed to analyze captured network packets, detect anomalies, and visualize real-time traffic statistics through an interactive dashboard.


---

🚀 Features

✅ Packet Capture & Analysis – Uses PyShark to parse .pcap files or live network data
✅ Real-Time Traffic Dashboard – Displays IP sources, protocols, and port usage trends
✅ Anomaly Detection (ML) – Scikit-learn model identifies unusual traffic patterns
✅ Data Visualization – Uses Pandas + Matplotlib for clean graphical insights
✅ Web-Based Interface – Flask-powered UI, deployable on Render or any cloud host


---

🧠 Tech Stack

Category	Tools Used

Backend	Python, Flask
Machine Learning	scikit-learn, pandas, numpy
Visualization	Matplotlib / Chart.js
Packet Capture	PyShark
Deployment	Render / GitHub Pages (frontend only)
Version Control	Git + GitHub



---

⚙️ Installation

1️⃣ Clone this repository

git clone https://github.com/Khush-hue/network-analyzer-dashboard.git
cd network-analyzer-dashboard

2️⃣ Create a virtual environment

python3 -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the app locally

python3 app/dashboard.py

5️⃣ Open your browser at
👉 http://127.0.0.1:5000
