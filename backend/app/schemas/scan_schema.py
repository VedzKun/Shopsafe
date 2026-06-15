from pydantic import BaseModel, HttpUrl


class ScanRequest(BaseModel):
    url: HttpUrl


class ScanResponse(BaseModel):
    status: str = "completed"
    url: str
    title: str | None = None
    html_length: int | None = None