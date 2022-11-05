from sqlalchemy.orm import Session

#import class for data query
from models import Poster_reach


# get single poster spot by id
def get_poster_spot(db: Session, poster_spot_id: int):
    return db.query(Poster_reach).filter(Poster_reach.poster_spot_id == poster_spot_id).all()


# get all poster spots
def get_poster_spots(db: Session, skip: int=0, limit: int=100):
    return db.query(Poster_reach).offset(skip).limit(limit).all()

