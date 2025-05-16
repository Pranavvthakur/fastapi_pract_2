from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()



@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    try:
        df = pd.read_csv(file.file)
        return JSONResponse(content=df.head().to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





@app.get("/data/")
def get_data():
    df = pd.read_csv("data.csv")
    filtered = df[df["sales"] > 1000]
    return JSONResponse(content=filtered.to_dict(orient="records"))


import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [100, 200, 150, 300, 250]
})

fig = px.line(df, x='Day', y='Sales', title='Daily Sales')
fig.show()
