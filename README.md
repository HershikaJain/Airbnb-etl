# Airbnb-etl

# Airbnb NYC ETL Pipeline

## Overview

This project implements a scalable ETL pipeline using the Airbnb New York City dataset. The pipeline involves data ingestion, transformation, and loading into a PostgreSQL database. Additionally, Metaflow is used to manage the ETL workflow.

## Prerequisites

- PostgreSQL database set up on your local machine or a cloud instance.
- Python environment with necessary libraries installed (`pandas`, `SQLAlchemy`, `Metaflow`, etc.).
- GitHub account for code repository.



##  Installing Python Libraries
pip install pandas SQLAlchemy metaflow

## Checking Versions
python -c "import pandas; print(pandas.__version__)"
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
python -c "import metaflow; print(metaflow.__version__)"

##Directory Structure
Organize the code in a well-structured directory:

airbnb_etl/
|-- data_loading.py
|-- data_extraction.py
|-- data_transformation.py
|-- data_loading_transformed.py
|-- etl_flow.py
|-- README.md

## Setup and Execution

### Step 1: Data Loading

1. Install PostgreSQL and create a database named `airbnb_nyc`.
2. Update the database connection string in `data_loading.py`.
3. Run the script to load data into PostgreSQL:
    ```sh
    python data_loading.py
    ```

### Step 2: ETL Process

1. Extract data from PostgreSQL:
    ```sh
    python data_extraction.py
    ```
2. Transform data:
    ```sh
    python data_transformation.py
    ```
3. Load transformed data into PostgreSQL:
    ```sh
    python data_loading_transformed.py
    ```

### Step 3: Workflow Management with Metaflow

1. Install Metaflow:
    ```sh
    pip install metaflow
    ```
2. Run the ETL pipeline using Metaflow:
    ```sh
    python etl_flow.py run
    ```

## Documentation

Detailed documentation on each step of the ETL process and data transformations is provided within the respective Python scripts.

## Demonstration

A short video or series of screenshots demonstrating the working ETL pipeline is available in the `demonstration` directory.

## References

- [Metaflow Documentation](https://docs.metaflow.org/)
- [New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
