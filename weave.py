import weave
import json
from openai import OpenAI

@weave.op() # 🐝 Decorator to track requests
def extract_fruit(sentence: str) -> dict:
    client = OpenAI()
    system_prompt = "Parse sentences into a JSON dict with keys: fruit, color and flavor."
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": sentence}
      ],
      temperature=0.7,
      response_format={"type": "json_object"}
    )
    extracted = response.choices[0].message.content
    return json.loads(extracted)

weave.init('intro-example') # 🐝
sentence = "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy."
extract_fruit(sentence)