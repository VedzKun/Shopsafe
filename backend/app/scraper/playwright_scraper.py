from playwright.async_api import async_playwright

class PlaywrightScraper:
    async def scrape(self, url: str):
        url = str(url)
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded")
            title = await page.title()
            html = await page.content()
            await browser.close()
            return {
                "url": url,
                "title": title,
                "html": html
            }