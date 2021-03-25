import json
import requests

AUTH_URL = 'http://localhost:8069/web/session/authenticate/'

headers = {'Content-type': 'application/json'}


# Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
# Authentication credentials
data = {
    'params': {
         'login': 'mc@piros.be',
         'password': 'Dfuwksx4!',
         'db': 'Dev'
    }
}

# Authenticate user
res = requests.post(
    AUTH_URL, 
    data=json.dumps(data), 
    headers=headers
)

# Get session_id from the response
# We are going to use this as our API key
#print(res.text)
#session_id = json.loads(res.text)['result']['session_id']
session_id="a64313046fd530baf4f6ed8021addc38e308baf1"


# Example 1
# Get users
USERS_URL = 'http://localhost:8069/api/res.users/?query={id,name}'
CRM_GET_URL = 'http://localhost:8069/api/crm.lead/?query={id,name}'
CRM_URL = 'http://localhost:8069/api/crm.lead/'
#CRM_URL = 'http://localhost:8069/api/product.public.category/'

# Pass session_id for auth
# This will take time since it retrives all res.users fields
# You can use query param to fetch specific fields
params = {'session_id': session_id}
params2 = {
	"params": {
		"data": {
			"name": "Test category_2"
		},
		"session_id": "2"
	}
}

res = requests.get(
    CRM_GET_URL, 
    params=params
)

res2 = requests.post(
    CRM_URL,
    params=params2,
    json={'name':'test'}
)

# This will be a very long response since it has many data
print(res.text)
