import sys
import os

# Fix import path (VERY IMPORTANT)
sys.path.append(os.getcwd())

from fastapi import FastAPI
from anomaly import run_anomaly_analysis

app = FastAPI()

# ✅ Basic test (should NEVER fail)
@app.get("/")
def home():
    return {"status": "running"}

# ✅ REAL test endpoint (this is what we use to debug)
@app.get("/test")
def test():
    import numpy as np
    import pandas as pd

    # Create dummy data (so no dependency issues)
    df = pd.DataFrame({
        "vibration_mm_s": np.random.randn(100),
        "stress_ratio": np.random.uniform(0.5, 1.2, 100),
        "temperature_c": np.random.uniform(20, 50, 100)
    })

    result = run_anomaly_analysis(df)
    return result