from pydantic import BaseModel
from typing import List, Optional

class WordResponse(BaseModel):
    word: str
    phonetic: Optional[str] = None
    meanings: Optional[List[str]] = None
    title: Optional[str] = None
    message: Optional[str] = None
    resolution: Optional[str] 
