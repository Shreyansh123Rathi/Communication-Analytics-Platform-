# WhatsApp Communication Analytics Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Built an end-to-end communication analytics solution that converts **thousands and lakhs** of raw WhatsApp chat logs into structured business intelligence. The platform leverages Python, NLP, sentiment analysis, topic modeling, and statistical analytics to generate **20+ actionable insights**, helping users understand engagement trends, conversation themes, and user interaction patterns.

### Live Demo
https://your-streamlit-link.streamlit.app/

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

# Features

## Statistical Dashboard

- Total Messages
- Total Words
- Media Shared
- Links Shared
- Most Active Users

## Activity Analytics

- Monthly Timeline
- Daily Timeline
- Weekly Activity Map
- Monthly Activity Map
- Hourly Heatmap

## NLP Features

- Word Cloud Generation
- Most Common Words
- Emoji Analysis
- Sentiment Analysis
- Topic Modeling (LDA)

## Advanced Insights

- Most Positive Message
- Most Negative Message
- Conversation Trends
- User Behaviour Analysis

---

# Workflow

## Step 1: Data Ingestion

Upload WhatsApp exported `.txt` chat file.

↓

## Step 2: Preprocessing

Raw chat text is transformed into a structured Pandas DataFrame.

↓

## Step 3: Feature Engineering

Generate:

- Year
- Month
- Date
- Day Name
- Hour
- Period

↓

## Step 4: Analytics Engine

Perform:

- Statistical Analysis
- Sentiment Analysis
- Topic Modeling
- Emoji Analytics

↓

## Step 5: Visualization

Generate:

- Charts
- Timelines
- Heatmaps
- Word Clouds
- User Reports

---

# Folder Structure

```text
WhatsApp-Communication-Analytics/
│
├── app.py
├── helper.py
├── sentiments.py
├── preprocessor.py
├── stop_hinglish.txt
├── requirements.txt
│
├── screenshots/
│   ├── dashboard.png
│   ├── heatmap.png
│   ├── sentiment.png
│   └── topics.png
│
└── README.md
```

---

# Screenshots

## Dashboard

![Dashboard](screenshots/dashboard.png)

## Activity Heatmap

![Heatmap](screenshots/heatmap.png)

## Sentiment Analysis

![Sentiment](screenshots/sentiment.png)

## Topic Modeling

![Topics](screenshots/topics.png)

---

# Tech Stack

| Category | Technologies |
|-----------|-------------|
| Language | Python |
| Frontend | Streamlit |
| Data Analysis | Pandas, NumPy |
| NLP | NLTK |
| Machine Learning | Scikit-Learn |
| Topic Modeling | LDA |
| Sentiment Analysis | VADER Sentiment |
| Visualization | Matplotlib, Seaborn |
| Word Cloud | WordCloud |
| Version Control | Git, GitHub |

---

# Key Analytics Implemented

✅ Message Statistics

✅ User Activity Analysis

✅ Timeline Analysis

✅ Word Cloud Generation

✅ Common Word Detection

✅ Emoji Analytics

✅ Sentiment Analysis

✅ Topic Modeling

✅ Activity Heatmaps

---

# Future Enhancements

- Response Time Analytics
- User Interaction Network Graph
- Hinglish Transformer Sentiment Model
- Plotly Interactive Dashboards
- Chat Personality Detection
- WhatsApp Wrapped Report
- AI Generated Conversation Summary

---

# Resume Project Description

**WhatsApp Communication Analytics Platform | Python, Streamlit, NLP, Scikit-Learn**

- Developed an end-to-end analytics platform for WhatsApp chat data using Python and Streamlit.
- Built NLP pipelines for sentiment analysis, topic modeling, and communication pattern discovery.
- Designed interactive dashboards featuring timelines, heatmaps, word clouds, and user engagement metrics.
- Implemented Latent Dirichlet Allocation (LDA) for automatic conversation topic extraction.
- Performed sentiment classification and behavioral analytics on thousands of chat messages.

---

# Author

### Shreyansh Rathi

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# License

This project is licensed under the MIT License.
