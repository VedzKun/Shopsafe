import asyncio
import threading
from app.scraper.playwright_scraper import PlaywrightScraper

class ScraperService:
    def __init__(self):
        self.scraper = PlaywrightScraper()

    async def scan_url(self, url: str):
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        def run_in_thread():
            from asyncio.windows_events import ProactorEventLoop
            thread_loop = ProactorEventLoop()
            asyncio.set_event_loop(thread_loop)
            try:
                result = thread_loop.run_until_complete(self.scraper.scrape(url))
                
                # Extract clean text from HTML
                try:
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(result.get("html", ""), "html.parser")
                    for s in soup(["script", "style"]):
                        s.extract()
                    text = soup.get_text(separator=" ")
                    result["text"] = " ".join(text.split())
                except Exception:
                    result["text"] = ""

                loop.call_soon_threadsafe(future.set_result, result)
            except Exception as e:
                loop.call_soon_threadsafe(future.set_exception, e)
            finally:
                thread_loop.close()

        threading.Thread(target=run_in_thread, daemon=True).start()
        return await future