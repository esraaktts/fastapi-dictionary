from pydantic import BaseModel
from typing import List, Optional, Dict

class WordResponse(BaseModel):
    word: Optional[str]
    phonetic: Optional[str] = None
    meanings: Optional[List[Dict[str, List[str]]]] = None
    tags :Optional [List[str]] = None
    title: Optional[str] = None
    message: Optional[str] = None
    resolution: Optional[str] = None
