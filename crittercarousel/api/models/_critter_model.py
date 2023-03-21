from datetime import datetime

from pydantic import BaseModel

class CritterModel(BaseModel):
    username: str
    species: str
    name: str
    last_feed_time: datetime
    last_pet_time: datetime
    last_play_time: datetime
    spawn_time: datetime
