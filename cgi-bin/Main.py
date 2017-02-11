import Text2Emotion
import soup
import AlgoMachine

class Movie(object):

    def __init__(self,name):
        self.description = name
        self.emotion_dict = None

def main(user_emotions):
    text2emotion = Text2Emotion.Text2Emotion()
    scraped_data = soup.parse()
    movie_limit = 50

    movie_list = []
    for movie_name in scraped_data:
        movie_list.append(Movie(movie_name))

    for movie in movie_list[:movie_limit]:
        movie.emotion_dict = text2emotion.generate(movie.description)

    algorithm_machine = AlgoMachine.AlgoMachine(movie_list[:movie_limit],user_emotions)
    top_five = algorithm_machine.calculate()

    return top_five

# a = {"joy":.4, "sadness":.3, "fear":.1, "anger":.05, "disgust":.05}
# print(main(a))