import pytest
@pytest.fixture(scope="class")
def setup():
    print("I ll execute first")
    yield
    print("I ll execute last")
@pytest.fixture()
def dataLoad():
    print("User profile Created")
    return["sree","lekha","kare"]

@pytest.fixture(params=[("chrome","sree","lekha"),("firefox","kare"),"IE"])
def crossBrowser(request):
    return request.param
