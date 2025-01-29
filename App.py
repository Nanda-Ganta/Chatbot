from flask import Flask, render_template, request
import pandas as pd
from IPython.display import Image

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('company_summary.csv', header=[0,1], index_col=0)

# Predefined data (calculated from the dataframe)
apple_total_revenue = df.loc['Apple', ('Total Revenue', 'sum')]
microsoft_net_income = df.loc['Microsoft', ('Net Income', 'mean')]
apple_total_revenue_mean = df.loc['Apple', ('Total Revenue', 'mean')]

# Define the simple chatbot logic
def simple_chatbot(user_query):
    if user_query == "How is the trend for Average Cash Flow from Operating Activities Over Years?":
        return render_template('response.html', image='cash_flow_over_years.png', text="Here is the trend for Average Cash Flow from Operating Activities over the years.")
    
    elif user_query == "How is the trend for Total Assets Over Years?":
        return render_template('response.html', image='assets_over_years.png', text="Here is the trend for Total Assets over the years.")
    
    elif user_query == "How does net income by company over years look like?":
        return render_template('response.html', image='net_income_by_company_by_year.png', text="Here is the trend for Net Income by company over the years.")
    
    elif user_query == "How do total liabilities by company over years look like?":
        return render_template('response.html', image='total_liabilities_by_company_by_year.png', text="Here is the trend for Total Liabilities by company over the years.")
    
    elif user_query == "What is sum Total Revenue of Apple for the time period from 2021 to 2023?":
        return render_template('response.html', text=f"Total Revenue of Apple from 2021 to 2023: {apple_total_revenue}")
    
    elif user_query == "What is mean Net Income of Microsoft for the time period from 2021 to 2023?":
        return render_template('response.html', text=f"Net Income of Microsoft from 2021 to 2023: {microsoft_net_income}")
    
    elif user_query == "What is mean Total Revenue of Apple for the time period from 2021 to 2023?":
        return render_template('response.html', text=f"Mean Total Revenue of Apple from 2021 to 2023: {apple_total_revenue_mean}")
    
    else:
        return render_template('response.html', text="Sorry, I can only provide information on predefined queries.")

# Route for the main page (form to input query)
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing user queries
@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    return simple_chatbot(user_query)

if __name__ == '__main__':
    app.run(debug=True)
