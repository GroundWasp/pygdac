import datetime
import requests
import logging
import jwt


order_id_list = []

### Login GDAC
logging.basicConfig(level=logging.DEBUG)

### Enter API key
if __name__ == '__main__':
    API_KEY = '==============API_KEY=============='
    SECRET = '==============SECRET_KEY=============='

    payload = {
        'api_key': "api:ak:" + API_KEY,
        'nonce': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    jwtToken = jwt.encode(payload, SECRET, 'HS256')
    headers = {'Authorization': 'Bearer '+jwtToken}
    

### Choose Num
    while 1:
        print("\n\n1.. Account balance check\n2.. Sell\n3.. Show order id")
        userIn = int(input())
        
        if userIn == 1:
            #Account balance check
            r = requests.get("https://partner.gdac.com/v0.4/balance", headers=headers)

            print('Request')
            print(r.request.headers)
            print('Response')
            print(r.status_code)
            print(r.headers)
            print(r.content)


        elif userIn == 2:
            # Sell
            data = {"pair":"USDT/KRW","side":"S","price":"3000.0000","quantity":"1.0000"}
            print(type(data))
            print("Sell Price")
            data["price"] = input()
            print("Sell Count [ex.1.0000]")
            data["quantity"] = input()

            print(data)
            
            r = requests.post("https://partner.gdac.com/v0.4/orders", headers=headers, data=data)

            print('Request')
            print(r.request.headers)
            print('Response')
            print(r.status_code)
            print('NO1')
            print(r.headers)
            print('NO2')
            print(r.content)
            #order_id_list.append(r.json()['order_id'])

        elif userIn == 3:   
            print(order_id_list)

