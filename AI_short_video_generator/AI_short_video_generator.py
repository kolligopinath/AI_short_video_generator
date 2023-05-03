import openai
import requests
import nltk
import urllib.request
from datetime import datetime
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import time

# Declaration of variables like API keys and others
#replace the API keys
api_key = "openai_api_key"
ADVISOR_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
ELEVEN_LABS_API_KEY = "Elevenlabs_api_key"

# Set up the OpenAI API client
openai.api_key = api_key

# Define a function to send a prompt to the API


def chat_with_gpt(prompt, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message = response.choices[0].text.strip()
    return message
    
    
def remove_special_characters(input_string):
    # Replace any non-alphanumeric characters with an empty string
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    return cleaned_string


def generate_video(prompt):
    audio_folder = "Generated audios"
    image_folder = "Generated images"

    if not os.path.exists(audio_folder):
        # Create folder if it doesn't exist
        os.makedirs(audio_folder)
        print("Folder created - Generated audios")

    if not os.path.exists(image_folder):
        # Create folder if it doesn't exist
        os.makedirs(image_folder)
        print("Folder created - Generated images")

    print("Input received from UI: " + prompt)
    response = chat_with_gpt(prompt)
    print("ChatGPT generated response: " + response)

    # Wait for 60 seconds
    # time.sleep(60)

    sentences = nltk.sent_tokenize(response)

    timestamp_string = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    for index, sentence in enumerate(sentences):

        print("Sentence " + str(index + 1) + ": " + sentence)

        # text to speech request with eleven labs
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ADVISOR_VOICE_ID}/stream"
        data = {
            "text": sentence.replace('"', ''),
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8
            }
        }

        r = requests.post(
            url, headers={'xi-api-key': ELEVEN_LABS_API_KEY}, json=data)

        audio_filename = "Generated audios/audio" + \
            timestamp_string + "-" + str(index) + ".mp3"
        with open(audio_filename, "wb") as output:
            output.write(r.content)

        Sentence_for_image = chat_with_gpt(
            "Enhance the following sentense with painstaking details and adjectives - " + sentence)
        print("Enhanced sentence " + str(index + 1) +
              " for image generation: " + Sentence_for_image)

        response_image = openai.Image.create(
            prompt=Sentence_for_image,
            n=1,
            size="1024x1024"
        )
        image_url = response_image['data'][0]['url']

        image_filename = "Generated images/image" + \
            timestamp_string + "-" + str(index) + ".png"
        urllib.request.urlretrieve(image_url, image_filename)

        videos = []

        # Load the image and audio files
        image = ImageClip(image_filename)
        audio = AudioFileClip(audio_filename)

        # Set the image duration to match the audio duration
        image = image.set_duration(audio.duration)

        # Set the audio to the image
        image = image.set_audio(audio)

        # Set the fps (frames per second) for the image clip
        image.fps = 24

        if index > 0:
            # Write the result to the output video file
            combined = concatenate_videoclips([combined, image])
        else:
            combined = image

    # Set the output video file
    output_video_file = "output_video" + timestamp_string + ".mp4"
    combined.write_videofile(output_video_file)

    title_text = chat_with_gpt(
        "Generate topic title in 4-5 words using the following sentense - " + prompt)

    print("prompt value before title generation: " + prompt)
    print("generated title from chatGPT: " + title_text)

    video_title = remove_special_characters(title_text) + ".mp4"

    print("prompt value before title generation: " + prompt)

    os.rename(output_video_file, video_title)

    return video_title
