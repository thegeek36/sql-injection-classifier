# sql-injection-classifier

This project aims to classify SQL queries as either malicious or non-malicious using various machine learning algorithms. The dataset used for training the models was obtained from Kaggle, and it can be found at [SQL Injection Dataset](https://www.kaggle.com/datasets/sajid576/sql-injection-dataset).

## Algorithms Used

The following algorithms were implemented and evaluated for classification:

- Long Short-Term Memory (LSTM)
- Support Vector Machine (SVM)
- Random Forest
- Decision Trees
- Logistic Regression

## Data Cleaning

To preprocess the data, we used the CountVectorizer to tokenize and vectorize the SQL queries. The dataset consists of three columns:

1. Serial Number
2. Query
3. Label (0 for non-malicious, 1 for malicious)

## Model Selection

After evaluating the performance of different algorithms, the Support Vector Machine (SVM) classifier achieved the highest accuracy. Therefore, SVM was selected as the final model for deployment.

## Deployment

The web application was built using Streamlit, allowing users to input SQL queries and receive predictions on their maliciousness. The application has also been deployed on Streamlit Cloud for accessibility.

## Running the Application

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/thegeek36/sql-injection-classifier.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sql-injection-classifier
   ```

3. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **macOS and Linux**:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Conclusion

This project provided valuable insights into machine learning techniques for classifying SQL queries. Although it was a small-scale project, it served as an opportunity to revisit and reinforce fundamental concepts in machine learning.

Thank you for your interest in this project!

---