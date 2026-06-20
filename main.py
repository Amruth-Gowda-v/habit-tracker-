import requests
from datetime import *
import quantity
TOKEN = "9591331bc"
USERNAME = "amruthgowda"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}


#---------------creating a user----------------
# pixela_endpoint = f"https://pixe.la/v1/users/<username>/graphs/<graphID>"

# user_params = {
#     "token": "9591331bc",
#     "username": "amruthgowda",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)



#---------------creating a graph----------------

# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Reading Graph",
#     "unit": "Pages",
#     "type": "int",
#     "color": "shibafu"
# }


# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )
 #---------------adding a pixel----------------

pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
 "date": datetime.now().strftime("%Y%m%d"),
 "quantity":str(quantity.quantity)
 }

response = requests.post(
    url=pixela_endpoint,
    json=pixel_config,
    headers=headers
)


print(response.text)

