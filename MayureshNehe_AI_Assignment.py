import openai
import os

openai.api_key = "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"

def generate_story(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=5,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

story_prompt = "a haunted house"
story = generate_story(story_prompt)
print(story)
