# takes in movie object and a ranked list of emotions
def isClose(movie, emotion_rank, user_emotions):
    emo0 = emotion_rank[0]
    emo1 = emotion_rank[1]
    emo2 = emotion_rank[2]
    dist0 = abs(movie.emotion_dict[emo0] - user_emotions[emo0])
    dist1 = abs(movie.emotion_dict[emo1] - user_emotions[emo1])
    dist2 = abs(movie.emotion_dict[emo2] - user_emotions[emo2])
    smalldist = .3

    if ((dist0 > smalldist) or (dist1 > smalldist) or (dist2 > smalldist)): return False
    else: return True

class AlgoMachine(object):

    def __init__(self, movie_list, user_emotions):
        self.movie_list = movie_list
        self.user_emotions = user_emotions

    def calculate(self):
        # rank the emotions
        emotion_rank = []

        highest_percent = -1
        highest_emotion = None
        while (len(emotion_rank) != len(self.user_emotions.keys())): # keep looping until all emotions included
            for emotion in self.user_emotions.keys(): # loop through all emotions and find best percent
                if ((emotion not in emotion_rank) and (self.user_emotions[emotion] > highest_percent)):
                    (highest_percent, highest_emotion) = (self.user_emotions[emotion], emotion)
            emotion_rank.append(highest_emotion)
            highest_percent = -1
            highest_emotion = None
        # print(emotion_rank)

        # iterate through all movies and get ones who have close percents for top 3 images
        relevant_movies = []
        for movie in self.movie_list:
            if isClose(movie, emotion_rank, self.user_emotions):
                relevant_movies.append(movie)
        return relevant_movies[:4]


# ab = {"anger":.01, "joy":.30, "disgust":.23, "fear":.12, "sadness":.1}
# a = AlgoMachine("hi", ab)
# a.calculate()