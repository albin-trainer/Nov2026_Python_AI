
from  openai import OpenAI
from dotenv import load_dotenv
import os

# cg_enteprise_url="https://openai.generative.engine.capgemini.com"
# aimodel="gpt-4o"
load_dotenv() ##This loads the envirornment variables
apikey=os.getenv("API_KEY")
cg_enteprise_url=os.getenv("CG_ENTERPRISE_URL")
aimodel=os.getenv("AI_MODEL")

#client=OpenAI(api_key=apikey, base_url=cg_enteprise_url)
client=OpenAI(api_key=apikey)