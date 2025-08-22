from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess
import json

app = FastAPI()

@app.get("/api")
def download_info(url: str = Query(..., description="Video URL kerak")):
    try:
        command = ["/var/www/downloader-api/venv/bin/yt-dlp", "-j", url]

        result = subprocess.run(command, capture_output=True, text=True)

        if result.stdout:
            # Har bir qatorni alohida JSON sifatida o‘qiymiz
            data = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
            return JSONResponse(content=data)
        else:
            return JSONResponse(
                content={
                    "error": "Video yuklab bo‘lmadi",
                    "stderr": result.stderr  # ❗ log ham qaytadi
                },
                status_code=500
            )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
