from fastapi import APIRouter

from app.schemas.scan_schema import ScanRequest, ScanResponse

router = APIRouter (
    prefix = "/scan",
    tags = ["scan"]
)

@router.post("", response_model = ScanResponse)
async def scan_website(request: ScanRequest):
    return ScanResponse(
        status="scanning",
        url=str(request.url)
    )
    