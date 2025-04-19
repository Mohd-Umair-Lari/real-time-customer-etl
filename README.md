# Real-Time Customer Feedback ETL Pipeline 🧠📊

This project simulates a real-world ETL (Extract, Transform, Load) data engineering pipeline using Python. It collects product data from a public API, cleans and transforms it, loads it into an SQLite database, and analyzes the price distribution using Matplotlib.

## 🔧 Features

- Extracts product data from [FakeStore API](https://fakestoreapi.com/products)
- Cleans titles, categories, and formats data
- Loads data into a local SQLite database
- Generates a histogram of product prices
- Demonstrates core data engineering skills

## 📁 Project Structure

real-time-customer-etl/ 
├── extract.py # Pulls product data from the API 
├── transform.py # Cleans and formats data using Pandas 
├── load.py # Loads data into SQLite ├── main.py # Orchestrates the ETL pipeline 
├── analyze.py # Visualizes price distribution 
├── requirements.txt # Python libraries required 
├── README.md # This file

## 🧪 How to Run

1. Clone the repository:

git clone https://github.com/Mohd-Umair-Lari/real-time-customer-etl.git 
cd real-time-customer-etl

2. Install dependencies:

pip install -r requirements.txt


3. Run the ETL pipeline:

python main.py


4. View data insights:

python analyze.py


## 📊 Sample Output

- SQLite database: `database.db`
- Histogram plot showing price distribution

## 👨‍💻 Author

Mohd Umair Lari  
[LinkedIn](https://www.linkedin.com/in/mohd-umair-lari/)  
[GitHub](https://github.com/Mohd-Umair-Lari)  
