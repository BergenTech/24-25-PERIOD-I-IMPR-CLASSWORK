def calculate_song_mood(tempo, pitch, volume):
    try:
        # pass - if everything goes well
        # if tempo < 60 or (pitch < 0 or  pitch >10) or (volume < 0 or volume >10):
        if not(60<= tempo <=180) or not (0 <= pitch <=10) or not (0 <= volume <=10):
            raise Exception
        tempo_normalized = (tempo-60)/12 #This converts 60-180 to 0-10
        mood_score = (tempo_normalized + pitch + volume)/3
        if mood_score < 5:
            return "Sad"
        elif mood_score <=7:
            return "Neutral"
        else:
            return "Happy"
    except:
        return "Invalid Inputs!"

def test_song_mood():
    print('Testing Song Mood Calculator...')
    # print(calculate_song_mood(120, 3, 4))
    print(calculate_song_mood(-60, 8, -2))
    print(calculate_song_mood(140, 7, 8))
    
if __name__ == "__main__":
    test_song_mood()
    