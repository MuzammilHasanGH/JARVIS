from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("CUSTOM_ENV_KEY"),
)