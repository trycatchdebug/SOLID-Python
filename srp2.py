import requests

def get_auth_token():
    # hits some services to fetch token
    auth = "abc"
    return {"Auth": f"auth {auth}"}

def create_payload(data):
    # do some operations on the data
    return {**data}


def hit_random_api(headers, payload):
    # pagination, retry logic....
    try:
        response = requests.post(
            url='/abc',
            headers=headers,
            data=payload
        )
    except Exception as exc:
        # retry here....
        pass
    else:
        res = response.json()

    return res

def bulk_insert_to_db(res):
    # do bulk insert
    pass


def process_raw_data(data):

    # get token to hit the api
    headers = get_auth_token()

    # create payload to hit the api
    payload = create_payload()

    # hit a xyz api
    res = hit_random_api(headers=headers, payload=payload)

    # creates entry from the response
    # map it to db object and bulk insert
    bulk_insert_to_db(res)
