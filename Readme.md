# SachAI

Welcome to the **DLFPS Hackathon Project - SachAI** for **Shriteq 2024**! This repository contains our solution to combat **misinformation and fake news** using advanced tools and datasets. The project aligns with the challenge of detecting and mitigating misinformation across various media forms. 

## Table of Contents
- [Introduction](#introduction)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Dataset](#dataset)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgments](#acknowledgments)

## Introduction
This project aims to provide a robust solution to detect and mitigate misinformation and fake content using **AI-powered detection tools**. With the rise of manipulated media, our project integrates **state-of-the-art algorithms and datasets** to analyze content and distinguish real from fake images, videos, and news articles.

This work is part of our participation in the **Shriteq Hackathon 2024**, where we focus on building **tools for automated fake news detection**.

## Features
- **Fake Image Detection**: Uses **open-source fake image datasets** from Hugging Face and OpenXLab.
- **Sentiment Analysis for News**: Identifies emotionally misleading news articles.
- **Browser Extension**: Highlights questionable news links to alert users in real-time.
- **Credibility API**: Scores articles for authenticity using key metadata features.
- **Comprehensive Reporting**: Logs detected misinformation and provides analytics.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask/Node.js  
- **AI/ML Models**: TensorFlow, OpenCV, Hugging Face datasets
- **Browser Extension**: JavaScript, Manifest v3 

## Dependencies
The following libraries and tools are required to run the project:

- deepface  
- deeplake  
- dlib  
- face-recognition  
- face-recognition-models  
- huggingface-hub  
- kaggle  
- keras  
- keras-models  
- Keras-Preprocessing  
- np_utils  
- numpy  
- pandas  
- pillow  
- scikit-image  
- scikit-learn  
- streamlit  
- tensorflow  
- tf-explain  
- tf_keras  
- tokenizers  

To install these dependencies, run:
   ```bash
   pip install -r requirements.txt
```

## Installation
To set up the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/niveaaa/DLFPS-Hackathon-Shriteq-2024.git
   cd DLFPS-Hackathon-Shriteq-2024

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt  # For Python dependencies
   npm install  # For JavaScript dependencies

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/niveaaa/DLFPS-Hackathon-Shriteq-2024.git
   cd DLFPS-Hackathon-Shriteq-2024

## Usage
1. **Detect Fake Images**:  
   - Navigate to the tool’s interface and upload an image to verify its authenticity.  
   - The system will return a **"Real"** or **"Fake"** label based on the AI model's prediction.

2. **Analyze News Articles**:  
   - Enter a news article URL in the provided input field.  
   - The system will perform **sentiment analysis** and generate a **credibility score**.  
   - It flags articles with suspicious or biased content to alert users.

3. **Browser Extension**:  
   - Install the extension by navigating to the `extension/` folder and loading it as an **unpacked extension** in your browser.  
   - When browsing news websites, the extension will highlight links with questionable content.

4. **API Usage for Credibility Verification**:  
   - Use the **REST API** to verify the credibility of articles programmatically.
   - Example API request:
     ```bash
     curl -X POST https://your-api-endpoint.com/verify \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com/news-article"}'
     ```
   - The API responds with metadata and a credibility score:
     ```json
     {
       "title": "Example News Article",
       "credibility_score": 65,
       "sentiment": "Neutral"
     }
     ```

## Dataset
We leverage the **Fake Image Dataset** from:
- **[Hugging Face (InfImagine)](https://huggingface.co/)**  
- **[OpenXLab](https://openxlab.org/)**  

These datasets contain real and fake images with corresponding metadata, which help in training, testing, and evaluating the models. Feel free to explore the datasets to understand how the detection model works.
