from dataclasses import dataclass

@dataclass
class settings:
    '''_____________________________________
    Central configuration for the Praman QA Engine.
    In future projects, these values will be loaded from YAML or env vars.
    '''
    BASE_URL: str= "https://the-internet.herokuapp.com/"
    BROWSER: str= "chromium"
    HEADLESS: bool= True
    TIMEOUT: int= 30000 # Playwright expects milliseconds

# Create a singleton instance that tests can import
config = settings()
