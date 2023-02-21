from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_TOKEN')

def gpthelp(dp):
    ac = openai.Completion.create(
        model="text-davinci-003",
        prompt=dp,
        temperature=1,
        max_tokens=1000        
    )
    zd = ac.get("choices")
    if zd and len(zd) > 0:
        pr = zd[0]["text"]
    return pr