import sys
import os
# Add framework to path so we can import it
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from framework.config.settings import config

def test_base_url_is_set():
    assert config.BASE_URL is not None
    assert "herokuapp" in config.BASE_URL
def test_browser_is_chromium():
    assert config.BROWSER == "chromium"
def test_headless_is_boolean():        #it must be a boolean, not a string
    assert isinstance(config.HEADLESS, bool)
    assert config.HEADLESS is True
def test_timeout_is_integer():          #it must be an int, not a string
    assert isinstance(config.TIMEOUT, int)
    assert config.TIMEOUT > 0


