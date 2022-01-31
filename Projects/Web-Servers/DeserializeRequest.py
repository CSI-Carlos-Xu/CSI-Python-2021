import json, ssl
from random import Random
import urllib.request
from RandomPhoneNumber import RandomPhoneNumber

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
addressURL = "https://random-data-api.com/api/phone_number/random_phone_number?size=100"

# Create a list to populate with our data
phoneNumbers:RandomPhoneNumber = [] 

# Execute HTTP Request
req = urllib.request.Request(addressURL)
requestData = json.loads(urllib.request.urlopen(req).read())

# Loop over JSON items and Deserialize them into python objects
for r in requestData:  
    # Deserialize 
    phoneNumber:RandomPhoneNumber = RandomPhoneNumber(**r)
    # Add object to list
    phoneNumbers.append(phoneNumber) 
    # Print phone number
    print(phoneNumber.phone_number)