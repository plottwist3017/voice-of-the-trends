# 🧠 Voice of Trends 2025 — Social Media Analytics Dashboard

A Power BI + Python data visualization project analyzing 300,000+ global trending hashtags (2025) and transforming them into a brain-shaped word cloud that represents collective social media attention patterns.

This project focuses on data aggregation, trend analysis, and high-impact visualization storytelling using real-world social media data.

---

## 🚀 Project Overview

This project analyzes 300,000+ global trending hashtags (2025) and visualizes social media attention patterns using a Power BI dashboard with Python integration.

The main output is a brain-shaped word cloud, representing the intensity and distribution of global digital trends.

---

## 🖥️ Power BI Word Cloud (Brain Shaped)

The dashboard was built using Power BI with Python integration to generate a custom brain-shaped word cloud visual.

---

![Voice of Trends Word Cloud](wordcloud_preview.png)

---

## Features:

Data aggregation of hashtag mentions
Filtering of low-frequency noise
Top 1500 trending hashtags used
Embedded Python script for visualization

File:

powerbi/voice_of_trends_dashboard.pbix

---

## 📁 Project Structure

```text
│
├── dashboard/
│   └── wordcloud_preview.png
│
├── data/
│   └── global_trending_hashtags_2025.csv
│
├── powerbi/
│   └── voice_of_trends_dashboard.pbix
│
├── python/
│   └── wordcloud_generator.py
│
├── images/
│   └── brain.png
│
└── README.md
```

## 📊 Dataset

Global Trending Hashtags Dataset (2025)
Size: 300,000+ rows

Source: Kaggle (Global Social Media Trending Hashtags Dataset 2025)

---

## ⚙️ Tools & Technologies Used
- 📈 Power BI
- 📄 Microsoft Excel / CSV
- 🐍Python, Pandas & NumPy
- 📊 Matplotlib
- 🔠 WordCloud
- 🎨 Data Visualization
- 📖 Data Storytelling
- 🖼️ Dashboard Design 

---

## 🐍 Python Implementation

The word cloud is generated using Python inside Power BI.

Key Steps:
- Aggregate hashtag mentions
- Clean and filter dataset
- Convert to frequency dictionary
- Generate word cloud using custom mask
- freq = dict(zip(df['hashtag'], df['mentions']))
- Word Cloud Generation
- Custom brain-shaped mask (brain.png)
- WordCloud + Matplotlib
- High-resolution rendering
- Contour styling for shape clarity
- Color palette: tab20b

---

## 📌 Key Features
- Large-scale dataset processing (300K+ rows)
- Power BI + Python integration
- Custom shape-based word cloud
- Clean data aggregation pipeline
- High-resolution visualization output
- Data storytelling through visual design

---

## 🧠 Insights

The visualization represents global social media activity as a collective attention map, where:

Hashtag frequency → popularity
Trend density → global attention intensity
Spatial layout → conceptual “digital brain” of online discourse

---

## 👨‍💻 About Me

I am a Computer Science student passionate about:

- 📊 Data Analytics
- 📈 Data Visualization
- 🧠 Business Intelligence
- 🤖 AI & Technology Trends

Currently building projects using Tableau, Python, and analytics tools to strengthen my technical and analytical skills.

---
