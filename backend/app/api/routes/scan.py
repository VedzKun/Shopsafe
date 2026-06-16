from fastapi import APIRouter

from app.services.scan_service import ScanService
from app.services.scraper_service import ScraperService
from app.schemas.scan_schema import ScanRequest, ScanResponse

router = APIRouter (
    prefix = "/scan",
    tags = ["Scanner"]
)

scan_service = ScanService()
scraper_service = ScraperService()

@router.post("", response_model = ScanResponse)
async def scan_website(request: ScanRequest):
    result = await scraper_service.scan_url(str(request.url))
    return {
        "url":result["url"],
        "title":result["title"],
        "text_count":len(result["text"].split()),
        "html_length":len(result["html"])
    }
    