import pytest
import requests
import json
import properties

class Api_keywords:
    def readJsonFromFile(self,filename):
        file= open(filename)
        return json.load(file)
    def create_user(self,token,jsonFile):
        data=self.readJsonFromFile(jsonFile)
        header={"Content-Type":"application/json","Authorization":"Bearer "+token}
        res=requests.post(properties.base_url+"/public/v1/users", headers=header,json=data)
        print("post status code."+str(res.status_code))
        return res

    def delete_user(self,token,id):
        header = {"Authorization": "Bearer " + token}
        res=requests.delete(properties.base_url+"/public/v1/users/"+str(id),headers=header)
        print("Delete res status code"+str(res.status_code))
        assert res.status_code==204

    def update_existinguser(self,token,id,jsonFile):
        data = self.readJsonFromFile(jsonFile)
        header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        res = requests.put(properties.base_url+"/public/v1/users/"+str(id), headers=header, json=data)
        print("put status code" + str(res.status_code))
        return res

    def getUser_details(self,id,token):
        header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        res = requests.get(properties.base_url + "/public/v1/users/" + str(id), headers=header)
        print(str(id)+" status code" + str(res.status_code))
        return res



