from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess
import json

app = FastAPI()

@app.get("/api")
def download_info(url: str = Query(..., description="Video URL kerak")):
    try:
        # yt-dlp ni JSON formatda ishga tushirish
        command = ["yt-dlp", "-j", url]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.stdout:
            data = json.loads(result.stdout)
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"error": "Video yuklab bo‘lmadi"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
