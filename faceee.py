import paralleldots

paralleldots.set_api_key("eVmlBXycMO4Ms48MAngsteYBzhg2HoMTdYleGq8OP9Q")

path = "C:\\Users\\Shrijith\\Desktop\\sihh\\yola\\imagelol.png"

dict = paralleldots.facial_emotion(path)
d = dict['facial_emotion']
max = d[0]['score']
str = d[0]['tag']
for i in d:
    if(i['score'] > max):
        max=i['score']
        str=i['tag']

score=0
if str=='Neutral':
    score=3
elif str=='Sad':
    score=2
elif str=='Angry':
    score=-1
elif str=='Fear':
    score=1
elif str=='Suprise':
    score=4
elif str=='Happy':
    score=5
else:
    score=2
