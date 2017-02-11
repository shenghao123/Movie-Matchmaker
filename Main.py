import Text2Emotion
import soup
import AlgoMachine

class Movie(object):

    def __init__(self,name):
        self.description = name
        self.emotion_dict = None

def main(user_emotions):
    text2emotion = Text2Emotion.Text2Emotion()
    algorithm_machine = AlgoMachine.AlgoMachine()
    scraped_data = soup.parse()

    movie_list = []
    for movie_name in scraped_data:
        movie_list.append(Movie(movie_name))

    for movie in movie_list:
        movie.emotion_dict = text2emotion.generate(movie.description)

    top_five = algorithm_machine.calculate(movie_list, user_emotions)

    return top_five