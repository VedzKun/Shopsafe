from playwright.async_api import async_playwright

class PlaywrightScraper:
    async def scrape(self, url: str):
        url = str(url)
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080}
            )
            page = await context.new_page()
            
            try:
                from playwright_stealth import Stealth
                stealth = Stealth()
                await stealth.apply_stealth_async(page)
            except ImportError:
                pass # Proceed without stealth if not installed

            await page.goto(url, wait_until="domcontentloaded")
            title = await page.title()
            html = await page.content()
            await browser.close()
            return {
                "url": url,
                "title": title,
                "html": html
            }