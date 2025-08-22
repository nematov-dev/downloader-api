from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import yt_dlp

app = FastAPI()

@app.get("/api")
def download_info(url: str = Query(..., description="Video URL kerak")):
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # download=False faqat info uchun
            return JSONResponse(content=info)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
