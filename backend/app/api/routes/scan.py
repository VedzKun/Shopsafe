from fastapi import APIRouter

from app.services.scan_service import ScanService
from app.schemas.scan_schema import ScanRequest, ScanResponse

router = APIRouter (
    prefix = "/scan",
    tags = ["Scanner"]
)

scan_service = ScanService()

@router.post("", response_model = ScanResponse)
async def scan_website(request: ScanRequest):
    page_data = await scan_service.scan(request.url)
    return {
        "url":page_data["url"],
        "title":page_data["title"],
        "html_length":len(page_data["html"])
    }
    