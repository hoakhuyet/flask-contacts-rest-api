import requests
import json


class ContactCommon:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_contact_response(self, uri):
        """
        :param uri: '/contacts/<contact_id>' or '/contacts'
        :return: response of get content
        """
        url = "{}{}".format(self.api_url, uri)
        return requests.get(url)

    def get_all_contact(self, uri):
        response = self.get_contact_response(uri)
        if response.status_code == 200:
            dict_data = json.loads(response.text)
            # data = dict_data["items"]
            lst = []
            for item in dict_data["items"]:
                lst.append((item["contact_id"], item["name"], item["phone"], item["address"]))
            return lst
        else:
            return None

    def get_contact(self, uri):
        response = self.get_contact_response(uri)
        if response.status_code == 200:
            item = json.loads(response.text)
            # item = dict_data["items"](0)
            data = {
                "Name": item["name"],
                "Phone": item["phone"],
                "Address": item["address"],
                "Contact_id": item["contact_id"]
            }
            return data
        else:
            return None

    def delete_contact(self, uri):
        try:
            url = "{}{}".format(self.api_url, uri)
            requests.delete(url)
            return True
        except Exception as ex:
            print("delete_contact", ex.__str__())
            return False
        # return requests.get(url)
