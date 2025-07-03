from pydantic import BaseModel
from typing import Optional, List
import json

class PersonalityInputSchema(BaseModel):
    """
    Schema for personality trait prediction input.
    """
    # 9.0,1,3.0,1.0,1,2.0,1.0
    name: str = "John"
    timeSpentAlone: int = 9
    stageFear: int = 1
    socialEventAttendance: int = 3
    goingOutside: int = 1
    drainedAfterSocializing: int = 1
    friendsCircleSize: int = 2
    postFrequency: int = 1
    
class PersonalityTraitResponseSchema(BaseModel):
    """
    Schema for personality trait prediction output.
    """
    #name: str
    prediction: int

class ErrorResponseSchema(BaseModel):
    """
    Schema for error responses.
    """
    message: str

