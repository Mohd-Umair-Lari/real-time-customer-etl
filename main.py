# main.py
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    raw=extract_data()
    if raw:
        clean_df=transform_data(raw)
        load_data(clean_df)
        print("ETL completed and data loaded to DB.")

if __name__=="__main__":
    main()
