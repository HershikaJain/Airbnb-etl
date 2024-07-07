import pandas as pd
from sqlalchemy import create_engine

def transform_data(df):
    # Normalize date
    df['last_review'] = pd.to_datetime(df['last_review'])
    df['last_review_year'] = df['last_review'].dt.year
    df['last_review_month'] = df['last_review'].dt.month

    # Calculate average price per neighborhood
    avg_price_per_neighbourhood = df.groupby('neighbourhood')['price'].mean().reset_index()
    avg_price_per_neighbourhood.columns = ['neighbourhood', 'avg_price']

    # Handle missing values
    df['reviews_per_month'].fillna(0, inplace=True)
    
    return df, avg_price_per_neighbourhood


if __name__ == '__main__':
    # Database connection
    engine = create_engine('postgresql://postgres:Hersheys29@localhost:5432/airbnb_nyc')

    # Extract data from PostgreSQL into a DataFrame
    df = pd.read_sql('SELECT * FROM airbnb_listings', engine)

    # Perform data transformation
    df_transformed, avg_price_per_neighbourhood = transform_data(df)

    # Load transformed data into a new table in PostgreSQL
    df_transformed.to_sql('airbnb_listings_transformed', engine, if_exists='replace', index=False)
    avg_price_per_neighbourhood.to_sql('avg_price_per_neighbourhood', engine, if_exists='replace', index=False)

    print("Data transformation and loading completed.")
