from fastapi import Depends, FastAPI, HTTPException, Header
from sqlalchemy.orm import Session

from typing import Optional, List

from . import crud, models, schemas

from .database import SessionLocal, engine

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
def read_voter(firstName: str = Header(None, convert_underscores=False),
               lastName: str = Header(None, convert_underscores=False),
               db: Session = Depends(get_db)):
    db_voters = crud.get_voters_by_name(db, first_name=firstName, last_name=lastName)
    if db_voters is None:
        raise HTTPException(status_code=404, detail=f"No entries found for {firstName} {lastName}")
    return db_voters


@app.get('/api/v1/voters/{voter_id}', response_model=schemas.Voter)
def read_voter(voter_id: int, db: Session = Depends(get_db)):
    db_voter = crud.get_voter(db, voter_id=voter_id)
    if db_voter is None:
        raise HTTPException(status_code=404, detail="Voter not found")
    return db_voter


@app.get('/api/v1/challenged_voters/', response_model=List[schemas.Voter])
def read_voter(db: Session = Depends(get_db)):
    db_voters = crud.get_voters_by_ballot_status(db)
    if db_voters is None:
        raise HTTPException(status_code=404, detail=f"No challenged ballots found")
    return db_voters


def main():
    app.run(
        host='0.0.0.0'
    )


if __name__ == '__main__':
    main()
