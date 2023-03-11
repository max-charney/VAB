from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import openai

#INPUTS
video_id = 'Video ID (last part of video URL)'
question = "Question; for example: What is this video about?"

unformatted_transcript = YouTubeTranscriptApi.get_transcript(video_id)
fmt = TextFormatter()
transcript = fmt.format_transcript(unformatted_transcript)

def gpt3(prompt):
    openai.api_key = 'Open AI api key'

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.1,
    max_tokens=256,
    #top_p=1,
    #frequency_penalty=0,
    #presence_penalty=0
    )
    content = response.choices[0].text.split(".")
    #print(content)
    #print(response.choices[0].text)
    return (response.choices[0].text)


query = 'Here is a youtube transcript. Base your answer off of it. '+question+': '+transcript
response = gpt3(query)
print(response)
