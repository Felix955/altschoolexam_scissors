# PROJECT NAME SCISSORS
# FELIX OLADELE

import crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, ShortenedURL
from database import engine, SessionLocal
from schemas import LongURL, ShortenedURLResponse
from crud import create_shortened_url, get_original_url
from qrcode_generator import generate_qr_code
from exam import crud


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/long_url/")
async def shorten_url(long_url: str, db: Session = Depends(get_db)):
    db_url = crud.create_shortened_url(db, long_url)
    return db_url

@app.get("/{shortened_url}")
async def redirect_to_original(shortened_url: str, db: Session = Depends(get_db)):
    original_url = get_original_url(db, shortened_url)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"Location": original_url}

@app.get("/generate_qr/{shortened_url}")
async def generate_qr(shortened_url: str, db: Session = Depends(get_db)):
    original_url = get_original_url(db, shortened_url)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    qr_code = generate_qr_code(original_url)
    return qr_code
