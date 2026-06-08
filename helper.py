from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

#AA
def fetch_stats(selected_user, df):
#1.Number of messages
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
#2.Word Count
    words = []
    for message in df['message']:
        words.extend(message.split())

#3.Fetch number of media shared
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0] #\n kyuki read lrte time esa he show ho rah hai
# 4.fetch number of links shared
    extract = URLExtract()
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

#BB)Most talkative users
def most_busy_users(df):
    x = df['user'].value_counts().head() #x=number of times a person messaged is calculated
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

#CC: WordCloud
def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt', 'r')           #1.Read stop words
    stop_words = f.read()

    if selected_user != 'Overall':               #2.Select user
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']  #3.Removing unnecessary words repetition
    temp = temp[~temp['message'].isin([
        '<Media omitted>\n',
        'deleted message',
        'edited message'
    ])]
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():              #4.In lower case, as in stop_word file has everything in lower case
            if word not in stop_words:
                y.append(word)
        return " ".join(y)          #5. Combines all words stored in the list y into a single string separated by spaces and returns it.

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


#DD) To get most common words bar chart, how much time they r repeated.
def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[~temp['message'].isin([
        '<Media omitted>\n',
        'deleted message',
        'edited message'
    ])]

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])  #1.Emoji.UNICODE_EMOJI['en'] :-Collection of all valid emojis
#2.C: character

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

#EE)Timeline of messages
def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index() #Reset index helps to give o/p as dataframe

    time = []
    for i in range(timeline.shape[0]):           #loop b/w indexes chalega
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

#FF)daily messages
def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

#GG)Weekly messages
def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

#HH)Activity maps

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0).reindex(
        ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    ).reindex(
        columns=[
            '00-1','1-2','2-3','3-4','4-5','5-6',
            '6-7','7-8','8-9','9-10','10-11','11-12',
            '12-13','13-14','14-15','15-16','16-17','17-18',
            '18-19','19-20','20-21','21-22','22-23','23-00'
        ]
    )

