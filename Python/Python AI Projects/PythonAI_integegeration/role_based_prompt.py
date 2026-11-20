from aiconfig import client
from aiconfig import aimodel

# Prompt Template (Reusable prompt)
user_prompt="""
  You are an experienced  {role}
  Analyze the following customer review based on your professional role.
   Review:
    {review}
                Give your response in simple language.
"""
role="CEO"
user_review="I purchased an HP laptop two weeks ago. The laptop has an excellent display and looks stylish. However, it becomes very slow when I open multiple applications simultaneously. The battery lasts only around 2 hours, even with normal usage. The laptop also gets heated during long working hours. Overall, I am not satisfied with its performance"
user_prompt=user_prompt.format(role=role,review=user_review)

response=client.responses.create(model=aimodel,
                        input=user_prompt)
print(response.output_text)