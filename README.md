# WhatsApp Communication Analytics Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Built an end-to-end communication analytics solution that converts **thousands and lakhs** of raw WhatsApp chat logs into structured business intelligence. The platform leverages Python, NLP, sentiment analysis, topic modeling, and statistical analytics to generate **20+ actionable insights**, helping users understand engagement trends, conversation themes, and user interaction patterns.

### Live Demo
https://analysing-whatsapp-chats.streamlit.app/

---

# Project Overview

WhatsApp chat logs are unstructured text files filled with valuable data. However, manually extracting insights is impossible. This project was built to solve that problem by providing a user-friendly interface to upload a chat file and automatically generate a comprehensive report.

The project's key challenge and feature is its ability to accurately analyze **Hinglish (a mix of Hindi and English)**, a common language in informal chats where standard NLP tools fail.



The platform enables users to:

- Analyze chat activity
- Discover communication patterns
- Track sentiment trends
- Identify active users
- Detect conversation topics
- Explore emoji usage

---
<img width="1370" height="346" alt="Top Statistics" src="https://github.com/user-attachments/assets/6f0510c1-a861-409b-b10b-c405dcd7c454" />
<img width="1155" height="575" alt="Monthly Timeline" src="https://github.com/user-attachments/assets/4de018ad-f1ba-4a4b-b290-2b2f73171f5f" />
<img width="951" height="809" alt="Daily Timeline" src="https://github.com/user-attachments/assets/9541b1f5-0040-4cec-b42b-8f2a476f1ad9" />


# Features
Comprehensive Statistical Dashboard: The main view displays key metrics, including total messages, words, media shared, and links. It also visualizes user activity through timelines, heatmaps, and rankings of the busiest users, days, and months.
<img width="1444" height="756" alt="Most Challant Users" src="https://github.com/user-attachments/assets/aefc6be2-588f-4053-a558-6e6bbb36e33f" />
<img width="959" height="809" alt="Weekly Activity Map" src="https://github.com/user-attachments/assets/95ecbfff-ff88-47be-9a19-e77b03ebdefb" />

**Accurate Hinglish Sentiment Analysis:** The app goes beyond simple analysis by using a state-of-the-art Hugging Face transformer model (pascalrai/hinglish-twitter-roberta-base-sentiment). This model is specifically fine-tuned on Hinglish social media text, allowing it to accurately determine if messages are positive, negative, or neutral.

<img width="1502" height="761" alt="Sentimental Analysis" src="https://github.com/user-attachments/assets/69d5dcb1-0579-4a58-9cc7-7d1bf5e56d26" />

**Automatic Topic Modeling:** Filters out system notifications, media placeholders, deleted messages, and custom Hinglish stop words to focus on meaningful conversation content. The function then counts the frequency of the remaining words and returns the **top 20 most frequently used terms**, helping identify the dominant topics and recurring discussions in the chat.
<img width="1010" height="759" alt="Most Common Words" src="https://github.com/user-attachments/assets/4dad8377-dcc2-4c1c-8787-2ebb7adcbfb7" />

**In-Depth Word and Emoji Analysis:** Identifies and visualizes the most frequently used words and emojis in the chat. This feature uses a custom Hinglish stop-word list to filter out common, non-essential words, ensuring the results are meaningful.
<img width="1466" height="651" alt="Emoji Analysis" src="https://github.com/user-attachments/assets/a201ad2c-099b-4821-9a56-9260a3fe12df" />


# Workflow Explained

The project follows a standard data science application workflow:

**Data Ingestion & Preprocessing:** The user uploads a .txt file via the Streamlit interface. A dedicated preprocessing module (preprocessor.py) parses the raw text using regular expressions and converts the data into a clean Pandas DataFrame.

**Feature Engineering:** New columns (like year, month, day, hour) are extracted from the datetime objects to enable time-based analysis.

**Backend Analysis:** The helper.py  and sentiments.py script takes the clean DataFrame and applies various functions to calculate statistics and perform NLP tasks like sentiment analysis and topic modeling.

**Frontend Visualization:** The main application script (app.py) uses Matplotlib and Seaborn to generate plots, charts, and tables, which are then displayed to the user in an organized layout.

# Folder Structure

```text
Communication-Analytics-Platform
│
├── app.py          # Main Streamlit app
├── helper.py       # show chat analysis  
├── sentiments.py   # Analytics and NLP functions   
├── preprocessor.py   # Data cleaning
├── stop_hinglish.txt  #To remove buzz words 
├── requirements.txt  # Dependencies
├── Data insights    #show chat analysis
└── README.md
```

# Tech Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| Frontend | Streamlit |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-Learn |
| Sentiment Analysis | VADER Sentiment,Hugging Face Transformers (pipeline), NLTK|
| Data Viz | WordCloud, Matplotlib, Seaborn |
| Dev Tools | Git, GitHub, PyCharm |

---


# Project Summary

**Communication Analytics Platform | Python, Streamlit, NLP, Scikit-Learn**

- Developed an end-to-end analytics platform for WhatsApp chat data using Python and Streamlit.
- Built NLP pipelines for sentiment analysis, topic modeling, and communication pattern discovery.
- Designed interactive dashboards featuring timelines, heatmaps, word clouds, and user engagement metrics.
- Implemented Latent Dirichlet Allocation (LDA) for automatic conversation topic extraction.
- Performed sentiment classification and behavioral analytics on thousands of chat messages.

---

# Author

### Shreyansh Rathi

GitHub: https://github.com/Shreyansh123Rathi

LinkedIn: https://www.linkedin.com/in/shreyanshrathi1/

---

# License

This project is licensed under the MIT License.
