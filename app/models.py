from sqlalchemy import Column, Integer, TEXT, REAL
from .database import Base


class Voter(Base):
    __tablename__ = "voter"

    index = Column(Integer, primary_key=True, autoincrement=True)
    county = Column(TEXT)
    voter_id = Column(Integer)
    last_name = Column(TEXT)
    first_name = Column(TEXT)
    middle_name = Column(TEXT)
    suffix = Column(TEXT)
    street_no = Column(TEXT)
    street_name = Column(TEXT)
    apt_or_unit = Column(TEXT)
    city = Column(TEXT)
    state = Column(TEXT)
    zip_code = Column(TEXT)
    mailing_street_no = Column(TEXT)
    mailing_street_name = Column(TEXT)
    mailing_apt_or_unit = Column(TEXT)
    mailing_city = Column(TEXT)
    mailing_state = Column(TEXT)
    mailing_zip_code = Column(TEXT)
    application_status = Column(TEXT)
    ballot_status = Column(TEXT)
    status_reason = Column(TEXT)
    application_date = Column(TEXT)
    ballot_issued_date = Column(TEXT)
    ballot_return_date = Column(TEXT)
    ballot_style = Column(TEXT)
    ballot_assisted = Column(TEXT)
    challenged_or_provisional = Column(TEXT)
    id_required = Column(TEXT)
    municipal_precinct = Column(TEXT)
    county_precinct = Column(TEXT)
    cng = Column(Integer)
    sen = Column(Integer)
    house = Column(Integer)
    jud = Column(TEXT)
    combo_no = Column(Integer)
    vote_center_id = Column(REAL)
    ballot_id = Column(REAL)
    post_no = Column(REAL)
    party = Column(REAL)

    def __repr__(self):
        return '<Voter: {} - Name: {} - Status: {}>'. \
            format(self.voter_id, self.first_name + " " + self.last_name, self.ballot_status)
