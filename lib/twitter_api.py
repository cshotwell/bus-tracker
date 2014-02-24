import urllib
import httplib
import json
class Api(object):

    token_url = "https://api.twitter.com/oauth2/token"

    def __init__(self, key, secret):
        self.key = key 
        self.secret = secret
        self.auth_token = self._get_auth()

    def _url_encode(self, value):
        return urllib.quote(value)

    def _get_bearer_token(self, key, secret):
        return "%s:%s" % (self._url_encode(key), self._url_encode(secret))

    def _get_auth(self):
        bearer_token = self._get_bearer_token(self.key, self.secret).encode('base64')
        auth_param = "Basic %s" % bearer_token.replace("\n", "") 
        headers = { 
            "Authorization" : auth_param.strip(),
            "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8",
            "Host:" : "api.twitter.com",
        }   
        body = "grant_type=client_credentials"
        requestor = httplib.HTTPSConnection('api.twitter.com')
        requestor.request("POST", self.token_url, body=body, headers=headers)
        response = requestor.getresponse()
        d = json.load(response)
        return d["access_token"]

    def get_search(self, tag):
        auth_token = self._get_auth()

        url = "https://api.twitter.com/1.1/search/tweets.json?q=%s&result_type=mixed" % tag 
        auth_param = "Bearer %s" % auth_token.strip()
        headers = { 
        "Authorization" : auth_param,
            "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8",
        "Accept" : "*/*"
        }   
        requestor = httplib.HTTPSConnection('api.twitter.com')
        requestor.request("GET", url, headers=headers)
        response = requestor.getresponse()
        return json.loads(response.read())
