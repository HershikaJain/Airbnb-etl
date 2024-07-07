from sqlalchemy import create_engine
import pandas as pd

def extract_data():
    # Database connection
    engine = create_engine('postgresql://postgres:Hersheys29@localhost:5432/airbnb_nyc')
    
    # Extract data from PostgreSQL
    df = pd.read_sql('SELECT * FROM airbnb_listings', engine)
    return df

if __name__ == '__main__':
    df = extract_data()
    print(df.head())
