from pydantic import BaseModel

class PageData(BaseModel):
    url:str
    html:str
    html_length: int