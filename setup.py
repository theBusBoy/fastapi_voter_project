import uvicorn
import os

from app.main import app
import data_import

if __name__ == '__main__':
    data_import.main()
    uvicorn.run(app, port=os.getenv("PORT") or 8080)