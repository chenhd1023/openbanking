import json
import base64
import requests


def main():
    url='http://127.0.0.1:5000/'

    #id_oauth_url = 'http://127.0.0.1:5000/test/oauth'

    print('1.身份確認')
    print('1.1.	TSP呼叫財金路徑並取得銀行驗證主機')
    test_oauth = requests.get(url+"test/oauth")
    print(test_oauth)
    
    print('1.2.	TSP呼叫銀行驗證主機')
    oauth_authentication = requests.post(url+"oauth/authentication")
    print(oauth_authentication)

    print('2.消費者認證')
    print('2.1.	使用者輸入帳密')
    identity_queryAPI = requests.get(url+"identity/queryAPI")
    print(identity_queryAPI)
    
    print('2.2.	使用者確認授權範圍')
    get_authorization_code = requests.get(url+"identity/queryAPI?code=QDPsc0")
    print(get_authorization_code)

    print('3.授權/存取授權')
    print('3.1.	利用authorization code取得access token')
    oauth_token = requests.post(url+"oauth/token")
    print(oauth_token)

    print('3.2.利用access token取得消費者資料')
    user_testdata = requests.get(url+"user/testdata")
    print(user_testdata)

if __name__ == "__main__":
    main()
