from sqlalchemy import create_engine
import pandas as pd

def load_transformed_data(df, avg_price_per_neighbourhood):
    # Database connection
    engine = create_engine('postgresql://postgres:Hersheys29@localhost:5432/airbnb_nyc')

    # Load transformed data into PostgreSQL
    df.to_sql('airbnb_listings_transformed', engine, if_exists='replace', index=False)
    avg_price_per_neighbourhood.to_sql('avg_price_per_neighbourhood', engine, if_exists='replace', index=False)

if __name__ == '__main__':
    from data_transformation import transform_data
    from data_extraction import extract_data
    
    df = extract_data()
    df_transformed, avg_price_per_neighbourhood = transform_data(df)
    load_transformed_data(df_transformed, avg_price_per_neighbourhood)
