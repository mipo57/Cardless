import json
import os
from jwcrypto import jwt, jwk
import hashlib
import base64

def getUUID():
    return os.popen('uuidgen -t').read().strip()

def getHeaders():
    m = hashlib.sha256()
    cert = open("qseal3.pem", "rb").read()
    x5t = "87686e10d3ad1874ed11b3aa270d1b2c9471eec01712de53d5bd86369593f02a" # hashlib.sha256(cert).hexdigest()

    kid= "67:B4:E4:32:0E:81:23:26:43:16:88:E1:60:98:41:DC:3B:58:94:29".replace(":", "").lower()

    headers={
        "alg": "RS256",
        "typ": "JWT",
        'x5t#S256': x5t, 
        'kid': kid, 
        "x5u": "https://gist.githubusercontent.com/mipo57/411dcbc3fd9c6aebb851d14c645a06b8/raw/23f51d9ab733944ebd80e175e406d79189366ef7/qseal3.pem",
        }

    return headers

def PolishApiRequest(target, json_request):
    request_id = getUUID()

    json_string = json.dumps(json_request)

    filename = f"{request_id}.json"

    with open(filename, "w") as f:
        json.dump(json_request, f)

    key = open("private.pem", "rb").read()
    key = jwk.JWK().from_pem(key)

    Token = jwt.JWT(header=getHeaders(),
                        claims=json_string)
    Token.make_signed_token(key)
    Token.serialize()

    encoded_jwt = Token.serialize()

    jwt_split = encoded_jwt.split(".")
    jwt_split[1] = ""

    sign = ".".join(jwt_split)

    request = f"curl -X POST \"{target}\" -k --key private.pem --cert qwac_pub.pem -H \"accept: application/json\" -H  \"Accept-Encoding: gzip\" -H  \"Accept-Language: pl_PL\" -H  \"Accept-Charset: utf-8\" -H \"X-JWS-SIGNATURE: {sign}\" -H \"X-REQUEST-ID: {request_id}\" -H \"Content-Type: application/json\" -d @{request_id}.json --output - | gunzip"

    result = os.popen(request).read().strip()

    os.remove(filename)

    return result
    