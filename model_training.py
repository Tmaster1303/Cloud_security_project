import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Simulation data
data = {
    'requests_per_minute': [100, 110, 95, 105, 120, 2000, 100, 98, 99, 3000],
    'response_time': [0.2, 0.25, 0.19, 0.23, 0.21, 5, 0.22, 0.2, 0.2, 10]
}

# Create DataFrame and normalize data
df = pd.DataFrame(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Isolation Forest Training
model = IsolationForest(contamination=0.2)
model.fit(scaled_data)

# Save model and scaler
joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')

print("Model and scaler saved.")
