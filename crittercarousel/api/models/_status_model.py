import math
from datetime import datetime

from pydantic import BaseModel

from ._critter_model import CritterModel


class StatusModel(BaseModel):
    username: str
    name: str
    species: str
    hunger: int
    sadness: int
    boredom: int
    health: int
    status: str
    detail: str

    @staticmethod
    def from_critter(critter: CritterModel):

        now = datetime.now()

        status = "happy"
        detail = f"{critter.name} the {critter.species} is happy"

        since_last_feed_time = (now - critter.last_feed_time).total_seconds()
        since_last_pet_time = (now - critter.last_pet_time).total_seconds()
        since_last_play_time = (now - critter.last_play_time).total_seconds()

        hungry_time = since_last_feed_time - 300
        sad_time = since_last_pet_time - 300
        bored_time = since_last_play_time - 300

        hunger = max(0, min(hungry_time/3600, 1))
        sadness = max(0, min(sad_time/3600, 1))
        boredom = max(0, min(bored_time/3600, 1))

        if hunger >= 1:
            status = "dead"
            detail = f"{critter.name} the {critter.species} died from hunger"

        elif sadness >= 1:
            status = "dead"
            detail = f"{critter.name} the {critter.species} died from sadness"

        elif boredom >= 1:
            status = "dead"
            detail = f"{critter.name} the {critter.species} died from boredom"

        elif hunger > 0 and hunger >= sadness and hunger >= boredom:
            status = "hungry"
            detail = f"{critter.name} the {critter.species} is hungry"

        elif sadness > 0 and sadness >= boredom:
            status = "sad"
            detail = f"{critter.name} the {critter.species} is sad"

        elif boredom > 0:
            status = "bored"
            detail = f"{critter.name} the {critter.species} is bored"
        
        health = math.sqrt((1 - hunger) * (1 - sadness) * (1 - boredom))

        hunger_percent = int(hunger * 100)
        sadness_percent = int(sadness * 100)
        boredom_percent = int(boredom * 100)
        health_percent = int(health * 100)

        return StatusModel(
            username = critter.username,
            species = critter.species,
            name = critter.name,
            hunger = hunger_percent,
            sadness = sadness_percent,
            boredom = boredom_percent,
            health = health_percent,
            status = status,
            detail = detail
        )
    