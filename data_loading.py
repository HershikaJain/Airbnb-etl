import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db():
    # Load dataset
    df = pd.read_csv(r'D:\archive\AB_NYC_2019.csv')

    # Database connection
    engine = create_engine('postgresql://postgres:Hersheys29@localhost:5432/airbnb_nyc')

    # Load data into PostgreSQL
    df.to_sql('airbnb_listings', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    load_data_to_db()
