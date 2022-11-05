# Pydantic models here (SQLAlchemy models are in file models.py)
from datetime import date as date_type
from typing import List, Optional

from pydantic import BaseModel
# from sqlalchemy.sql.sqltypes import Date


# pydantic model (if creating new items is requiered)
class PosterReachBase(BaseModel):
    date: date_type
    canton_code: str
    poster_spot_id: int
    contacts_per_day_spr: int
    avg_percent_change_from_baseline: float
    reach_delta: float
    adjusted_reach: float



class PosterReachCreate(PosterReachBase):
    pass

class PosterReach(PosterReachBase):
    pass

    class Config:
        orm_mode = True


