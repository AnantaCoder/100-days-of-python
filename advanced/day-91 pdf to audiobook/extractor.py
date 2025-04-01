import edge_tts
import asyncio

async def generate_speech(text, output_filename="output.mp3"):
    
    try:
        communicate = edge_tts.Communicate(text, "en-US-JennyNeural")
        await communicate.save(output_filename)
        return output_filename
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None