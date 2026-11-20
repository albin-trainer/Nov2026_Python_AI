from aiconfig import client
from aiconfig import aimodel

def sportsPersonality(sports):
    # Prompt Template (Reusable prompt)
    user_prompt="""
        Give me top 5 personalities in  {s}
    """
    
    user_prompt=user_prompt.format(s=sports)
    #connect with LLM and get top 5 sports personilities
    response=client.responses.create(model=aimodel, input=user_prompt)
    print(response.output_text)


sports=input("Enter your fav sports")
sportsPersonality(sports)