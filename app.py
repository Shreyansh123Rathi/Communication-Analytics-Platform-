import streamlit as st
from matplotlib.pyplot import imshow
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Segoe UI Emoji'  #helps to read emojis


st.set_page_config(layout="wide")  #To keep alignment proper
import preprocessor,helper

import matplotlib.pyplot as plt
#1 Creating to choose a file

st.sidebar.title('WhatsApp Chat Analysis')
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue() #a.to read in bytes
    data = bytes_data.decode("utf-8") #b.To read file in string
    df = preprocessor.preprocess(data)

    #st.dataframe(df) #c.to display dataframe


# 2.Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):
        # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

#3.1. Monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

#3.2.Daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

#3.3. Activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy days")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='blue')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        #4. finding the talkative users in the group(Group level)
        if selected_user == 'Overall':
            st.title('Most Challant Users')
            x,new_df = helper.most_busy_users(df) #A:Calling helper
            fig, ax = plt.subplots() #B:ax is for axis

            col1, col2 = st.columns(2) #c:to divide the portion for 2 parts

            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df) #for table output

#5 Creating a word cloud
        df_wc = helper.create_wordcloud(selected_user,df)
        fig, ax =plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

#6 most common words
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()

        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')

        st.title('Most commmon words')
        st.pyplot(fig)

#7 Emoji Analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots(figsize=(8, 5))

            sns.barplot(
                x=emoji_df[1].head(),
                y=emoji_df[0].head(),
                ax=ax
            )

            ax.set_title("Top Emojis")
            st.pyplot(fig)