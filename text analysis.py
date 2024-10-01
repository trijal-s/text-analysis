#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = str(input())
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
products = soup.find_all("div")
ti = [product.get_text(strip=True) for product in products]
print(ti)


# In[3]:


from textblob import TextBlob
for text in ti:
    blob = TextBlob(text)
    p_score = blob.sentiment.polarity
    n_score = 1 - p_score
    sub_score = blob.subjectivity
    asl= sum(len(sentence) for sentence in text.split()) / len(text.split()) if len(text.split())!=0 else 0
    wc = sum(len(sentence.split()) for sentence in text.split()) / len(
        text.split("."))
    awl= sum(len(w) for w in text.split()) / len(text.split()) if len(text.split())!=0 else 0
    print(f"\nText: {text}")
    print(f"Positive Score: {p_score}")
    print(f"Negative Score: {n_score}")
    print(f"Subjectivity Score: {sub_score}")
    print(f"Average Sentence Length: {asl}")
    print(f"Word Count: {len(text.split())}")
    print(f"Average Word Length: {awl:.2f}")
    if p_score>n_score:
        print("positive sentiment")
    elif p_score==0.0:
        print("neutral sentiment")
    else:
        print("negative sentiment")


# In[ ]:




