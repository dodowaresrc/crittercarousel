from fastapi import HTTPException, status
from typing import Generator

from ._database_context import DatabaseContext

from crittercarousel.api.models import (CritterModel, EventModel, SpeciesModel,
                                        UserModel)

SPECIES_LIST = [
    "armadillo",
    "bunny",
    "chipmunk",
    "fox",
    "hedgehog",
    "iguana",
    "mole",
    "opossum",
    "otter",
    "porcupine",
    "skunk",
    "snake",
    "squirrel",
    "turtle",
    "weasel",
    "wombat"
]

CREATE_EVENTS_TABLE = """
    create table events (
        id integer primary key generated always as identity,
        username varchar(32),
        species varchar(32),
        name varchar(32),
        action varchar(32),
        time timestamp
    )"""

CREATE_USERS_TABLE = """
    create table users (
        name varchar(32) primary key,
        clams int,
        spawn_count int,
        adopt_count int,
        glue_count int
    )"""

CREATE_SPECIES_TABLE = """
    create table species (
        name varchar(32) primary key
    )"""

CREATE_CRITTERS_TABLE = """
    create table critters (
        username varchar(32) references users(name),
        species varchar(32) references species(name),
        name varchar(32),
        last_feed_time timestamp,
        last_pet_time timestamp,
        last_play_time timestamp,
        spawn_time timestamp,
        primary key (username, species, name)
    )"""

class CritterContext(DatabaseContext):

    def init(self, drop=False) -> None:

        if drop:
            self.execute("drop table if exists events")
            self.execute("drop table if exists critters")
            self.execute("drop table if exists species")
            self.execute("drop table if exists users")

        self.execute(CREATE_USERS_TABLE)
        self.execute(CREATE_SPECIES_TABLE)
        self.execute(CREATE_CRITTERS_TABLE)
        self.execute(CREATE_EVENTS_TABLE)

        statement = "insert into species values (%s)"

        for species in SPECIES_LIST:
            self._cursor.execute(statement, [species])

    def update_user(self, user:UserModel) -> None:

        self.update("users", user.dict(), ["name"])

    def update_species(self, species:SpeciesModel) -> None:

        self.update("species", species.dict(), ["name"])

    def update_critter(self, critter:CritterModel) -> None:

        self.update("critters", critter.dict(), ["username", "species", "name"])

    def insert_critter(self, critter:CritterModel) -> None:

        self.insert("critters", critter.dict())

    def insert_species(self, species:SpeciesModel) -> None:

        self.insert("species", species.dict())

    def insert_user(self, user:UserModel) -> None:

        self.insert("users", user.dict())

    def insert_event(self, event:EventModel) -> None:

        self.insert("events", event.dict(), ignore=["id"])

    def get_species(self, name:str=None) -> Generator[SpeciesModel, None, None]:

        where_eq = {"name": name}

        dict_generator = self.select("species", where_eq=where_eq)

        return (SpeciesModel(**x) for x in dict_generator)
    
    def get_users(self, name:str=None, limit:int=None) -> Generator[UserModel, None, None]:

        where_eq = {"name": name}

        dict_generator = self.select("users", where_eq=where_eq, limit=limit)

        return (UserModel(**x) for x in dict_generator)
    
    def delete_critter(self, critter:CritterModel):

        where_eq = {"username": critter.username, "species": critter.species, "name": critter.name}

        self.delete("critters", where_eq)

    def get_critters(
        self,
        username:str=None,
        species:str=None,
        name:str=None,
        limit:int=None
    ) -> Generator[CritterModel, None, None]:

        where_eq = {"username": username, "species": species, "name": name}

        dict_generator = self.select("critters", where_eq=where_eq, limit=limit)

        return (CritterModel(**x) for x in dict_generator)
    
    def get_events(
        self,
        username:str=None,
        species:str=None,
        name:str=None,
        action:str=None,
        limit:int=None
    ) -> Generator[EventModel, None, None]:
    
        where_eq = {"username": username, "species": species, "name": name, "action": action}

        dict_generator = self.select("events", where_eq=where_eq, limit=limit)

        return (EventModel(**x) for x in dict_generator)

    def fetch_user(self, name:str) -> UserModel:

        where_eq = {"name": name}

        self.select("users", where_eq=where_eq, limit=1)

        user_list = [UserModel(**x) for x in self._cursor]

        if not user_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"user not found: name={name}")
        
        return user_list[0]

    def fetch_species(self, name:str) -> SpeciesModel:

        where_eq = {"name": name}

        self.select("species", where_eq=where_eq, limit=1)

        species_list = [SpeciesModel(**x) for x in self._cursor]

        if not species_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"species not found: name={name}")
        
        return species_list[0]

    def fetch_critter(self, username:str, species:str, name:str) -> CritterModel:

        where_eq = {"username": username, "species": species, "name": name}

        self.select("critters", where_eq=where_eq, limit=1)

        critter_list = [CritterModel(**x) for x in self._cursor]

        if not critter_list:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"critter not found: username={username} species={species} name={name}")
        
        return critter_list[0]

    def assert_no_user(self, name:str):

        user_list = self.get_users(name=name, limit=1)

        if next(user_list, None):
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"user already exists: {name}"
            )

    def assert_no_species(self, name:str):

        species_list = self.get_species(name=name)

        if next(species_list, None):
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"species already exists: {name}"
            )

    def assert_no_critter(self, username:str, species:str, name:str):

        critter_list = self.get_critters(username=username, species=species, name=name, limit=1)

        if next(critter_list, None):
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = f"critter already exists: user={username} species={species} name={name}"
            )
