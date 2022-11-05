# main FastAPI app

from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# define endpoints and functions connected with them
# get all poster spots
@app.get("/poster_spots/", response_model=List[schemas.PosterReach])
def read_poster_spots(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    poster_spots= crud.get_poster_spots(db, skip=skip, limit=limit)
    return poster_spots


# get one certain poster spot id
@app.get("/poster_spots/{poster_spot_id}", response_model=List[schemas.PosterReach])
def read_poster_spot(poster_spot_id: int, db: Session = Depends(get_db)):
    db_poster_spot = crud.get_poster_spot(db, poster_spot_id=poster_spot_id)
    if db_poster_spot is None:
        raise HTTPException(status_code=404, detail="Poster spot ID not found")
    print(db_poster_spot)
    return db_poster_spot