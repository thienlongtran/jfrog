import requests

class JFrogAPI:
    def __init__(self, JFROG_API_URL, USERNAME, API_KEY):
        self.JFROG_API_URL = JFROG_API_URL
        self.USERNAME = USERNAME
        self.API_KEY = API_KEY

    def get_storage_info(self):
        response = requests.get(self.JFROG_API_URL + "storageinfo", auth=(self.USERNAME, self.API_KEY))
        return response.content

    def list_repositories(self):
        response = requests.get(self.JFROG_API_URL + "repositories", auth=(self.USERNAME, self.API_KEY))
        return response.content

    def update_repository(self, repository_key, configuration):
        response = requests.put(self.JFROG_API_URL + "repositories/" + repository_key, data=configuration, auth=(self.USERNAME, self.API_KEY))
        return response.content

    def update_repository(self, repository_key, configuration):
        response = requests.post(self.JFROG_API_URL + "repositories/" + repository_key, data=configuration, auth=(self.USERNAME, self.API_KEY))
        return response.content

    def delete_user(self, username):
        response = requests.delete(self.JFROG_API_URL + "v1/scim/v2/Users/" + username, auth=(self.USERNAME, self.API_KEY))
        return response.content

if __name__ == "__main__":
    jfrog = JFrogAPI(JFROG_API_URL="https://thienlongtran.jfrog.io/artifactory/api/",
                     USERNAME=None, #ENTER USERNAME HERE
                     API_KEY=None) #ENTER API KEY HERE