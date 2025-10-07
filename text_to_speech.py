import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY=os.getenv("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key = ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="iP95p4xoKVk53GoZ742B",
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32"
    )
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath])
        elif os_name == "Linux":
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}") 
    
    
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"
    
    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )   
    audioobj.save(output_filepath)
    os_name = platform.system()
    
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hi, I am doing fine, how are you? This is a test for Checking TTS"
output_filepath = "test_text_to_speech.mp3"
# text_to_speech_with_elevenlabs(input_text, output_filepath)
text_to_speech_with_gtts(input_text, output_filepath)