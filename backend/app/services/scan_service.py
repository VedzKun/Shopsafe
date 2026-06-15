from app.scraper.playwright_scraper import PlaywrightScraper

class ScanService:
    def __init__(self):
        self.scraper = PlaywrightScraper()

    async def scan(self, url: str):
        return await self.scraper.scrape(url)