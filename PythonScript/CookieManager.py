import asyncio
import subprocess

from pyppeteer import launch


class CookieManager:
    def __init__(self) -> None:
        pass
    # end def

    async def show_cookies(self, url: str) -> None:
        # Launch Chrome browser
        browser = await launch()
        page = await browser.newPage()

        # Go to a website
        await page.goto(url)

        # Get all cookies
        cookies = await page.cookies()
        print("All Cookies:")
        for cookie in cookies:
            print(cookie)

        # Close the browser
        await browser.close()
    # end def
# end class


class RunShellCode:
    def foo(self):
        command = "whoami"
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Print the output
        print(result.stdout.decode())
    # end def
# end class


if __name__ == '__main__':
    manager = CookieManager()
    
    shell = RunShellCode()
    shell.foo()

    # Run the script
    asyncio.get_event_loop().run_until_complete(
        manager.show_cookies('https://hiking.biji.co/')
    )

    input('press any key to exit.')
