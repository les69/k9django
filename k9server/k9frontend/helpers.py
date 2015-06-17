__author__ = 'les'

from textblob import TextBlob
from k9models.models import Message
from dateutil.parser import parse
from sets import Set


# like a group by for getting all dates and messages

def get_message_dates_by_user(user):
    m_l = Message.objects.filter(user=user)
    dates = Set()

    for message in m_l:
        dates.add(message.recv_date.date())

    return dates


def get_dates_and_messages():
    m_l = Message.objects.all()

    dict = {}

    for message in m_l:
        date_m = message.recv_date.date()
        if not dict.has_key(date_m):
            dict[date_m] = []
        dict[date_m].append(message.message_text)

    return dict


def get_daily_polarity(date):
    m_list = Message.objects.filter(recv_date__year=date.year, recv_date__month=date.month, recv_date__day=date.day)
    tot_polarity = 0

    for message in m_list:
        tot_polarity += get_polarity(message.message_text)

    return round(tot_polarity / len(m_list), 2)


def get_daily_subjectivity(date):
    m_list = Message.objects.filter(recv_date__year=date.year, recv_date__month=date.month, recv_date__day=date.day)
    tot_subj = 0

    for message in m_list:
        tot_subj += get_subjectivity(message.message_text)

    return round(tot_subj / len(m_list),2)

def get_subjectivity(phrase):
    blob = TextBlob(phrase)
    return blob.subjectivity


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