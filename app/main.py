from fastapi import Depends, FastAPI, HTTPException, Header
from sqlalchemy.orm import Session

from typing import List

from . import crud, models, schemas

from .database import SessionLocal, engine

from app.helper_functions import create_voter_dict

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    debug=True,
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/v1/voters/', response_model=List[schemas.Voter])
def get_voter_by_name(
        first_name: str = Header(None, convert_underscores=False),
        last_name: str = Header(None, convert_underscores=False),
        db: Session = Depends(get_db)):
    db_voters = crud.get_voters_by_name(db, first_name=first_name, last_name=last_name)
    if db_voters is None:
        raise HTTPException(status_code=404, detail=f"No entries found for {first_name} {last_name}")
    return db_voters


@app.get('/api/v1/voter_history/')
def get_voter_history_by_name(
        first_name: str = Header(None, convert_underscores=False),
        last_name: str = Header(None, convert_underscores=False),
        db: Session = Depends(get_db)):
    db_voters = crud.get_voters_by_name(db, first_name=first_name, last_name=last_name)
    if db_voters is None:
        raise HTTPException(status_code=404, detail=f"No entries found for {first_name} {last_name}")

    return create_voter_dict(db_voters)


@app.get('/api/v1/voters_with_county/', response_model=List[schemas.Voter])
def get_voter_by_name_county(
        first_name: str = Header(None, convert_underscores=False),
        last_name: str = Header(None, convert_underscores=False),
        county: str = Header(None, convert_underscores=False),
        db: Session = Depends(get_db)):
    db_voters = crud.get_voters_by_name_county(db, first_name=first_name, last_name=last_name, county=county)
    if db_voters is None:
        raise HTTPException(status_code=404, detail=f"No entries found for {first_name} {last_name}")
    return db_voters


@app.get('/api/v1/voters/{voter_id}', response_model=schemas.Voter)
def get_voter_by_id(voter_id: int, db: Session = Depends(get_db)):
    db_voter = crud.get_voter_by_id(db, voter_id=voter_id)
    if db_voter is None:
        raise HTTPException(status_code=404, detail="Voter not found")
    return db_voter


@app.get('/api/v1/voters_history/{voter_id}')
def get_voter_history_by_id(voter_id: int, db: Session = Depends(get_db)):
    db_voter = crud.get_voter_history_by_id(db, voter_id=voter_id)
    if db_voter is None:
        raise HTTPException(status_code=404, detail="Voter not found")

    return create_voter_dict(db_voter)


def main():
    app.run(
        host='0.0.0.0'
    )


if __name__ == '__main__':
    main()
