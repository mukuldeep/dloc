import pyttsx3

def s(text,voice_index):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(text)
    #engine.save_to_file(text, 'speech.mp3')
    engine.runAndWait()


s(" Hello. Have you just arrived at the camp? I’m Bella.",0)
s(" My name is Kathie. Nice to meet you. No, I’ve been here for a while.",1)
s(" Oh, OK… Where are you from?",0)
s(" I’m from Greece, but I’ve lived in this area for a long time. You?",1)
s(" I’m from the USA. I’m here on holidays.",0)
s(" Are you from a big family?",1)
s(" No, there are just five of us- me, my sister, my brother and my parents. What about you?",0)
s(" I’ve got two sisters.",1)
s(" Oh, that’s nice. What do you usually do in your free time? Do you have any hobbies?",0)
s(" I love hanging out with my friends or stay at home and read a good book. I don’t have a lot of hobbies. I enjoy playing volleyball… What about you?",1)
s(" I love it, too…What’s your favourite subject?",0)
s(" I like Biology. I love learning about the Environment.",1)
s(" Me too. I think we are going to be great friends!",0)
s(" So do I!",1)
