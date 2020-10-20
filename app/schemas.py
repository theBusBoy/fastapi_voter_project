from typing import Optional

from pydantic import BaseModel


class VoterBase(BaseModel):
    pass


class Voter(VoterBase):
    index: int
    voter_id: Optional[int] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    city: Optional[str] = None
    county: Optional[str] = None
    ballot_style: Optional[str] = None
    ballot_status: Optional[str] = None
    status_reason: Optional[str] = None
    challenged_or_provisional: Optional[str] = None
    ballot_id: Optional[int] = None

    class Config:
        orm_mode = True
