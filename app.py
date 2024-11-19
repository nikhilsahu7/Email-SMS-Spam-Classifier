import streamlit as st
import pickle
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string


ps = PorterStemmer()
stop_words = stopwords.words('english')
puns = string.punctuation 

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y=[]
    for i in text:
        if i.isalnum() and i not in stop_words and i not in puns:
            y.append(ps.stem(i))
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transform_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transform_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. display

    if result ==1:
        st.header("Spam")
    else:
        st.header("No Spam")

    
