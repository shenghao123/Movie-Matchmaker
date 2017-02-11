from watson_developer_cloud import AlchemyLanguageV1

# bluemix AlchemyApi API key
api_key = '6487efd8fd5427eec5345d11fa679e3293370dd2'

# construct API object from key
alchemy_language = AlchemyLanguageV1(api_key=api_key)

# example text for testing
test_text = "Daunted by the singular tastes and dark secrets of the handsome, tormented young entrepreneur Christian Grey, Anastasia Steele has broken off their relationship to start a new career with a Seattle Independent Publishing House (SIP); but desire for Christian still dominates her every waking thought, and when he proposes a new arrangement, Anastasia cannot resist. They rekindle their searing sexual affair, and Anastasia learns more about the harrowing past of her damaged, driven and demanding Fifty Shades. \n"\
            "While Christian wrestles with his inner demons, Anastasia must confront the anger and envy of the women who came before her, and make the most important decision of her life. All about the sex."

# get dictionary of data from text
text_dict = alchemy_language.emotion(text = test_text, language = 'english')

# get dictionary from text_dict
emotion_dict = text_dict['docEmotions']

# convert individual emotions percents to floats
(joy, disgust, anger, fear, sadness) = (float(emotion_dict["joy"]),
                                        float(emotion_dict["disgust"]),
                                        float(emotion_dict["anger"]),
                                        float(emotion_dict["fear"]),
                                        float(emotion_dict["sadness"]))

# recalculate emotion percents and store them back in emotion_dict as floats
total = (joy + disgust + anger + fear + sadness)
emotion_dict["joy"] = joy/total
emotion_dict["disgust"] = disgust/total
emotion_dict["anger"] = anger/total
emotion_dict["fear"] = fear/total
emotion_dict["sadness"] = sadness/total