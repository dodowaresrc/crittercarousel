from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    clams: int
    spawn_count: int
    adopt_count: int
    glue_count: int
