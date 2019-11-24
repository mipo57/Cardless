from PolishApi import getUUID, PolishApiRequest
from datetime import datetime, timedelta
import json
from flask import Flask, request

def Authorize(callbackLink):
    timeout = datetime.now() + timedelta(hours=10)
    timeout = timeout.strftime("%Y-%m-%dT%H:%M:%S") + ".894Z"  # japierdole

    request = {
        "requestHeader": {
            "requestId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "userAgent": "Swagger-Codegen/1.0.0/python",
            "ipAddress": "23.97.142.158",
            "sendDate": "2019-11-23T08:27:54.893Z",
            "tppId": "PSDPL-KNF-7417004754",
            "isCompanyContext": True
        },
        "response_type": "code",
        "client_id": "5797",
        "redirect_uri": f"{callbackLink}",
        "scope": "ais-accounts",
        "scope_details": {
            "privilegeList": [
                {
                    "accountNumber": "35551905220000000000019315",
                    "ais-accounts:getAccounts": {
                        "scopeUsageLimit": "multiple"
                    },
                }
            ],
            "scopeGroupType": "ais-accounts",
            "consentId": f"{getUUID()}",
            "scopeTimeLimit": f"{timeout}",
            "throttlingPolicy": "psd2Regulatory"
        },
        "state": f"{getUUID()}"
    }

    result = PolishApiRequest("https://api-obh.kir.pl/v2_1_1.1/auth/v2_1_1.1/authorize", request)
    result = json.loads(result)

    return result["aspspRedirectUri"]


def Token(code, redirect):
    timeout = datetime.now() + timedelta(hours=10)
    timeout = timeout.strftime("%Y-%m-%dT%H:%M:%S") + ".894Z"  # japierdole

    request = {
        "requestHeader": {
            "requestId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "sendDate": "2019-11-23T16:17:47.398Z",
            "tppId": "PSDPL-KNF-7417004754",
            "isCompanyContext": True,
        },
        "grant_type": "authorization_code",
        "Code": f"{code}",
        "redirect_uri": f"{redirect}",
        "client_id": "5797",
        "scope": "ais",
        "scope_details": {
            "privilegeList": [
                {
                    "accountNumber": "35551905220000000000019315",
                    "ais:getTransactionsDone": {
                        "scopeUsageLimit": "multiple",
                        "maxAllowedHistoryLong": 0
                    },
                }
            ],
            "scopeGroupType": "ais",
            "consentId": f"{getUUID()}",
            "scopeTimeLimit": f"{timeout}",
            "throttlingPolicy": "psd2Regulatory"
        },
        "is_user_session": True,
        "user_ip": "23.97.142.158",
        "user_agent": "Swagger-Codegen/1.0.0/python"
    }

    return PolishApiRequest("https://api-obh.kir.pl/v2_1_1.1/auth/v2_1_1.1/token", request)


def FullAuthorize(code, redirect):
    Authorize()


def getAccounts(token):
    request = {
        "requestHeader": {
            "requestId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "userAgent": "Swagger-Codegen/1.0.0/python",
            "ipAddress": "23.97.142.158",
            "sendDate": "2019-11-23T14:19:38.201Z",
            "tppId": "PSDPL-KNF-7417004754",
            "token": f"{token}",
            "isDirectPsu": True,
            "callbackURL": "http://localhost",
            "apiKey": f"{getUUID()}"
        },
        "typeOfPsuRelation": "Owner",
        "pageId": "0",
        "perPage": 10
    }

    result = PolishApiRequest(
        "https://api-obh.kir.pl/v2_1_1.1/accounts/v2_1_1.1/getAccounts", request)
    result = json.loads(result)

    data = []

    print(result)

    for k, v in result["accounts"]:
        account = {
            "number": v["accountNumber"],
            "name": v["accountType"]["description"]
        }

        data.append(account)

    return data


def getTransactionList(token, account):
    request = {
        "requestHeader": {
            "requestId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "userAgent": "Swagger-Codegen/1.0.0/python",
            "ipAddress": "23.97.142.158",
            "sendDate": "2019-11-23T14:19:38.201Z",
            "tppId": "PSDPL-KNF-7417004754",
            "token": f"{token}",
            "isDirectPsu": True,
            "callbackURL": "http://localhost",
            "apiKey": f"{getUUID()}"
        },
        "accountNumber": f"{account}",
        "itemIdFrom": "",
        "transactionDateFrom": "2000-11-23",
        "transactionDateTo": "2019-11-23",
        "bookingDateFrom": "2000-11-23",
        "bookingDateTo": "2019-11-23",
        "minAmount": "0",
        "maxAmount": "5",
        "pageId": "0",
        "perPage": 5,
        "type": "CREDIT"
    }

    result = PolishApiRequest(
        "https://api-obh.kir.pl/v2_1_1.1/accounts/v2_1_1.1/getTransactionsDone", request)
    result = json.loads(result)

    return result


print(Authorize("http://23.97.142.158/auth"))
#print(Token("eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiM2Y4NDA3Ny0wYTA1LTRlOTctODk0NS1lN2ZjNTgzMmMzOWQiLCJpYXQiOjE1NzQ1Mjg4MzIsInN1YiI6IkRvc3RlcCBkbyB1c2x1ZyBQU0QyIiwiaXNzIjoiTW9ja293ZSBBc3BzcCIsImNvbnNlbnRJZCI6ImExMTE3OTFjLTBlMTMtMTFlYS05NDdiLTAwMGQzYWFhN2U5NiIsImV4cCI6MTU3NDUyODk1MiwibmJmIjoxNTc0NTI4ODMyfQ.bJJIfHi1Z5N0c4TdcwBu3leCVhR-ei5LeCwronUHVrc", "http://localhost"))
#print(getTransactionList("eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzlhNjFiYy1kZDEwLTQ3N2ItYjRiZC0yNzMwMDRkNjk1MzYiLCJpYXQiOjE1NzQ1Mjg4NzQsInN1YiI6IkRvc3RlcCBkbyB1c2x1ZyBQU0QyIiwiaXNzIjoiTW9ja293ZSBBc3BzcCIsImNvbnNlbnRJZCI6ImExMTE3OTFjLTBlMTMtMTFlYS05NDdiLTAwMGQzYWFhN2U5NiIsImV4cCI6MTU3NDUyODk5NCwibmJmIjoxNTc0NTI4ODc0fQ.4ClSITSexRZ-2hkGcjzvQ74CAQxk8sxlJvzwiz3wqHo", "35551905220000000000019315"))

app = Flask(__name__)


@app.route("/auth")
def auth():
    token = request.args.get("code")
    token_res = Token(token, "http://23.97.142.158")

    refresh_token = json.loads(token_res)["refresh_token"]
    access_token = json.loads(token_res)["access_token"]

    print("#########################")
    print(getTransactionList(refresh_token, "35551905220000000000019315"))
    return ""


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
