from pydantic import BaseModel
from typing import Optional, List
import json

class PersonalityTraitSchema(BaseModel):
    """
    Schema for personality trait prediction input.
    """
    name: str = "John"
    timeSpentAlone: int = 0
    stageFear: int = 0
    socialEventAttendance: int = 0
    goingOutside: int = 0
    drainedAfterSocializing: int = 0
    friendsCircleSize: int = 0
    postFrequency: int = 0
    
class PersonalityTraitResponseSchema(BaseModel):
    """
    Schema for personality trait prediction output.
    """
    name: str
    personalityTrait: int

class ErrorResponseSchema(BaseModel):
    """
    Schema for error responses.
    """
    message: str

