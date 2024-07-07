from metaflow import FlowSpec, step
import pandas as pd
from sqlalchemy import create_engine

class AirbnbETLFlow(FlowSpec):


    @step
    def start(self):
        self.next(self.load_data)

    @step
    def load_data(self):
        self.df = pd.read_csv('AB_NYC_2019.csv')
        self.next(self.transform_data)

    @step
    def transform_data(self):
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])
        self.df['last_review_year'] = self.df['last_review'].dt.year
        self.df['last_review_month'] = self.df['last_review'].dt.month
        self.df['reviews_per_month'].fillna(0, inplace=True)
        self.avg_price_per_neighbourhood = self.df.groupby('neighbourhood')['price'].mean().reset_index()
        self.avg_price_per_neighbourhood.columns = ['neighbourhood', 'avg_price']
        self.next(self.load_to_db)

    @step
    def load_to_db(self):
        engine = create_engine('postgresql://postgres:Hersheys29@localhost:5432/airbnb_nyc')
        self.df.to_sql('airbnb_listings_transformed', engine, if_exists='replace', index=False)
        self.avg_price_per_neighbourhood.to_sql('avg_price_per_neighbourhood', engine, if_exists='replace', index=False)
        self.next(self.end)

    @step
    def end(self):
        print("ETL job completed successfully!")

if __name__ == '__main__':
    AirbnbETLFlow()
