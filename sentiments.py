import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
    stop_words = set(f.read().split())

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def sentiment_analysis(df):
    # Create an instance of the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Create new columns for sentiment scores
    sentiment_scores = df['message'].apply(lambda msg: analyzer.polarity_scores(str(msg)))
    df['sentiment_scores'] = sentiment_scores

    # Extract the compound score, which is a single, useful metric
    df['sentiment_compound'] = df['sentiment_scores'].apply(lambda score_dict: score_dict['compound'])

    # Create a sentiment label based on the compound score
    def get_sentiment_label(compound_score):
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

    df['sentiment_label'] = df['sentiment_compound'].apply(get_sentiment_label)

    return df


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.stem import WordNetLemmatizer
import pandas as pd  # Make sure pandas is imported


# ... keep the STOP_WORDS_SET defined at the top of your file

def find_topics(df, num_topics=5, num_words=10):
    """
    Finds the main topics in the chat using LDA.
    """
    # 1. Filter and prepare the text data
    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>\n')].copy()

    # 2. Lemmatize the messages (reduce words to their root form)
    lemmatizer = WordNetLemmatizer()

    def lemmatize_text(message):
        tokens = nltk.word_tokenize(message.lower())
        lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
        return " ".join(lemmatized_tokens)

    temp['lemmatized'] = temp['message'].apply(lemmatize_text)

    # 3. Vectorize the text data (convert text to a matrix of word counts)
    vectorizer = CountVectorizer(max_df=0.95, min_df=2)
    doc_term_matrix = vectorizer.fit_transform(temp['lemmatized'])

    # 4. Create and fit the LDA model
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(doc_term_matrix)

    # 5. Get the top words for each topic
    topics = []
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_words_idx = topic.argsort()[:-num_words - 1:-1]
        top_words = [feature_names[i] for i in top_words_idx]
        topics.append(f"Topic {topic_idx + 1}: " + ", ".join(top_words))

    return topics

