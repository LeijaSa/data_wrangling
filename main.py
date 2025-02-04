
import pandas as pd

from clean_products import get_cleaned_products
from clean_users import get_cleaned_users

def read_products_data():
    file_path='product_catalog_with_rubbish.csv'
    df=pd.read_csv(file_path)
    return df

def read_users_data():
    file_path='users_data_with_rubbish.csv'
    df=pd.read_csv(file_path)
    return df

def read_transactions_data():
    file_path='transactions_data.csv'
    df=pd.read_csv(file_path)
    return df

def main():
    
    products_data=read_products_data()
    users_data=read_users_data()
    

    cleaned_products_data=get_cleaned_products(products_data)
    cleaned_users=get_cleaned_users(users_data)
    transaction_data=read_transactions_data()


    merged_df = pd.merge(transaction_data, cleaned_users, on='user_id', how='inner')
    print(merged_df)

    merged_df2 = pd.merge(merged_df, cleaned_products_data, on='product_id', how='inner')
    print(merged_df2)
    
    # total_spending = transaction_data.groupby('user_id')['quantity'].sum() # total spending per user
    # print(f"Total spending per user: {total_spending}")
    # top5_sold = products.groupby(['Product ID']).agg(total_quantity_sold=('Price'), average_price=('Price')) # top 5 best-selling products & their avr price
    # most_popular = products.groupby('Category')['quantity'].sum() # most popular product category
    #transaction_data.to_json('transaction_data.json', orient='records', lines=True) # export dataset to json file
    #df_from_json = pd.read_json('transaction_data.json', lines=True) # read json file back into pandas dataframe
    #print(f"First few lines from the file: {df_from_json.head()}") # print the head of the file out

if __name__ == "__main__":
    main()