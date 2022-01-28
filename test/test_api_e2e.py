import pytest
from utilities.Api_keywords import Api_keywords
import properties
class Test_apis(Api_keywords):

    @pytest.fixture(autouse=True)
    def _auth_token(self, authToken):
        self.token= authToken

    @pytest.mark.Smoke
    def test_createnewuser(self):
        res=self.create_user(self.token,properties.create_userjson)
        assert res.status_code == 201
        res=res.json()
        print(res)
        data=self.readJsonFromFile(properties.create_userjson)
        print(data)
        assert (res["data"]["name"]==data["name"])
        assert (res["data"]["gender"] == data["gender"])
        assert (res["data"]["email"] == data["email"])
        assert (res["data"]["status"] == data["status"])
        print(res["data"]["id"])
        self.delete_user(self.token,res["data"]["id"])

    @pytest.mark.Regression
    def test_createDuplicateuser(self):
        newres = self.create_user(self.token, properties.create_userjson)
        rewres=newres.json()
        res = self.create_user(self.token, properties.create_userjson)
        assert res.status_code == 422
        res = res.json()
        print(res)
        data = self.readJsonFromFile(properties.create_userjson)
        print(data)
        assert (res["data"][0]["message"] == properties.duplicate_error)
        self.delete_user(self.token,rewres["data"]["id"])

    def test_updateExistingUser(self):
        res = self.create_user(self.token, properties.create_userjson)
        assert res.status_code == 201
        res = res.json()
        print(res)
        data = self.readJsonFromFile(properties.create_userjson)
        print(data)
        assert (res["data"]["name"] == data["name"])
        assert (res["data"]["gender"] == data["gender"])
        assert (res["data"]["email"] == data["email"])
        assert (res["data"]["status"] == data["status"])
        print(res["data"]["id"])
        updateres=self.update_existinguser(self.token, res["data"]["id"],properties.update_userjson)
        print(updateres.json())
        updateres=updateres.json()
        updateddata = self.readJsonFromFile(properties.update_userjson)
        assert (updateres["data"]["name"] == updateddata["name"])
        assert (updateres["data"]["gender"] == updateddata["gender"])
        assert (updateres["data"]["email"] == updateddata["email"])
        assert (updateres["data"]["status"] == updateddata["status"])
        self.delete_user(self.token, res["data"]["id"])

    @pytest.mark.parametrize("id",[3841,3841,3843,3845,3849])
    def test_dataDriven_Testing(self,id):
        res=self.getUser_details(id,self.token)
        assert res.status_code==200
        res=res.json()
        assert res["data"]["id"]==id






