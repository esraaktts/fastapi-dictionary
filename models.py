from pydantic import BaseModel
from typing import List, Optional, Dict, Union
from enum import Enum

class WordResponse(BaseModel):
    word: Optional[str]
    phonetic: Optional[str] = None
    meanings: Optional[List[Union[str, Dict[str, List[str]]]]] = None
    tags: Optional[List[str]] = None
    title: Optional[str] = None
    message: Optional[str] = None
    resolution: Optional[str] = None

class HistoryItem(BaseModel):
    word: str
    timestamp: str

class HistoryResponse(BaseModel):
    ip: str
    history: List[HistoryItem]

class ExportFormat(str, Enum):
    json = "json"
    csv = "csv"
    txt = "txt"


