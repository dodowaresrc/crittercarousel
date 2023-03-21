import os

from fastapi import HTTPException, status


def getenv(name:str, default:str=None, required:bool=False):

    value = os.getenv(name)

    if value:
        return value
    
    if required:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"environment variable not set: {name}"
        )
    
    return default
