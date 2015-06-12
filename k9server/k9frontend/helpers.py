__author__ = 'les'

from textblob import TextBlob
from k9models.models import Message
from dateutil.parser import parse


def get_polarity(phrase):
    blob = TextBlob(phrase)
    return blob.polarity


def get_sentiments(user):
    message_list = Message.objects.filter(user=user)
    text = get_text_from_message_list(message_list)
    blob = TextBlob(text)

    print blob.tags
    print blob.sentiment.polarity



def get_text_from_message_list(m_list):
    text = ""

    for message in m_list:
        text += " "
        #text += text.join(message.message_text)
        text += message.message_text
    return text

def convert_date(date):
    dt = parse(date)
    return dt.strftime('%Y/%m/%d %H:%M:%S')