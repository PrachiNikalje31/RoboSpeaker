import gtts
import playsound

if __name__ == "__main__":
        text = input ("Enter what you want to speak: ")
        sound = gtts.gTTS(text , lang="en")
        sound.save("TextToSound.mp3")
        playsound.playsound("TextToSound.mp3")


