from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import openai

video_id = 'kyvw6G9Max0'
question = "What findings were made based on the Mayan Hieroglyphics, and at about what time in the transcript does the video talk about the hieroglyphics?"

unformatted_transcript = YouTubeTranscriptApi.get_transcript(video_id)

# base_lang='en'
# wanted_lang = 'en'

# base_obj=unformatted_transcript.find_transcript([base_lang])
# base_tran = base_obj.fetch()

fmt = TextFormatter()
transcript = fmt.format_transcript(unformatted_transcript)

def gpt3(prompt):
    openai.api_key = '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'

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