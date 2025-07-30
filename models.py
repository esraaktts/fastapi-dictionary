from pydantic import BaseModel
from typing import List, Optional, Dict

class WordResponse(BaseModel):
    word: Optional[str]
    phonetic: Optional[str] = None
    meanings: Optional[List[str]] = None
    tags :Optional [List[Dict]] = None
    title: Optional[str] = None
    message: Optional[str] = None
    resolution: Optional[str] 
