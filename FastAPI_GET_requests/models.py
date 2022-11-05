# Create SQLAlchemy (database) models from the Base class
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DECIMAL
from sqlalchemy.orm import relationship

from database import Base



class Poster_reach(Base):
    __tablename__ = "poster_reach_full"

    date = Column(Date, primary_key=True)
    canton_code = Column(String)
    poster_spot_id = Column(Integer, primary_key=True)
    contacts_per_day_spr = Column(Integer)
    avg_percent_change_from_baseline = Column(DECIMAL)  # decimal(19,2) in db
    reach_delta = Column(DECIMAL)  # decimal(33,6) in db
    adjusted_reach = Column(DECIMAL)  # decimal(34,6) in db


