import pytest
from sree.baseclass import BaseClass


@pytest.mark.usefixtures("dataLoad")

class TestExamp3(BaseClass):

    def test_editProfile(self,dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        print(dataLoad)