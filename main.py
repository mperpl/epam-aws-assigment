import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/az-region")
async def get_region_data():
    try:
        az = requests.get(
            "http://169.254.169.254/latest/meta-data/placement/availability-zone",
            timeout=2,
        ).text
        region = az[:-1]
        return {"region": region, "availability_zone": az}

    except requests.exceptions.RequestException:
        return {
            "error": "Could not connect to AWS Metadata API.",
            "message": "API accessible only from within an EC2 instance.",
        }