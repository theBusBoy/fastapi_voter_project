from sqlalchemy.orm import Session

from . import models


def get_voter_by_id(db: Session, voter_id: int):
    return db.query(models.Voter).filter(models.Voter.voter_id == voter_id).first()


def get_voter_history_by_id(db: Session, voter_id: int):
    return db.query(models.Voter).filter(models.Voter.voter_id == voter_id).all()


def get_voters_by_name(db: Session, first_name: str, last_name: str):
    return db.query(models.Voter).filter_by(
        first_name=first_name.upper(),
        last_name=last_name.upper()
    ).all()


def get_challenged_voters(db: Session):
    return db.query(models.Voter).filter(
        models.Voter.ballot_status.in_(["C", "S"])
    ).all()
