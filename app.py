import streamlit as st
import joblib
import os

# Load the model and vectorizer
model = joblib.load('classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title('SQL Query Classifier')

st.write("""
## About the Classifier
This classifier determines whether a given SQL query is malicious or non-malicious.

- **Non-malicious (0)**: These queries are considered safe and typically involve regular database operations such as SELECT, INSERT, UPDATE, or DELETE.
- **Malicious (1)**: These queries are potentially harmful and might include SQL injection attacks or other forms of database exploitation.

### Enter an SQL query to classify it:
""")

# Input form for SQL query
query = st.text_input('Enter SQL Query')

if st.button('Classify'):
    if query:
        query_transformed = vectorizer.transform([query])
        prediction = model.predict(query_transformed)[0]
        
        if prediction == 1:
            st.markdown(f'<p style="color:red;">Query: {query}</p>', unsafe_allow_html=True)
            st.markdown('<p style="color:red;">Prediction: Malicious</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:green;">Query: {query}</p>', unsafe_allow_html=True)
            st.markdown('<p style="color:green;">Prediction: Non-malicious</p>', unsafe_allow_html=True)
    else:
        st.write('Please enter a SQL query.')


st.markdown("""<br><br><br>
<div style="text-align: center;">
    <p>Developed By Yogesh, Soham, Akash & Yash</p>
</div>
""", unsafe_allow_html=True)
