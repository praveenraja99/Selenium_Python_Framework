
from selenium import webdriver
import  pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
       driver = webdriver.Chrome()
    elif browser=="firefox":
        driver= webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value from setup method
    return request.config.getoption("--browser")

######################pytest HTML reports############################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'XDB App'
        config.stash[metadata_key]['Module Name'] = 'XDB Login'
        config.stash[metadata_key]['Tester'] = 'Praveenraj'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)