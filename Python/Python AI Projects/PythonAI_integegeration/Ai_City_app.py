from aiconfig import client
from aiconfig import aimodel

# Prompt Template (Reusable prompt)
user_prompt="""
    Give 5 places to visit in
    city {city}
"""
inp_city=input("Enter the city Name :")
user_prompt=user_prompt.format(city=inp_city)

response=client.responses.create(model=aimodel,
                        input=user_prompt)
print(response.output_text)