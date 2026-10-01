"""
data_cleaning.py
----------------
Automated data cleaning and feature engineering pipeline for Sales Data Analysis.
Author: Aryansh Upadhyay (BBA-BIA)
Supports both pandas (when installed) and native standard library fallback.
"""

import os
import csv
from datetime import datetime

def clean_with_stdlib(raw_filepath: str, processed_filepath: str):
    print(f"[*] Standard Library Mode: Reading raw dataset from {raw_filepath}")
    with open(raw_filepath, 'r', newline='') as f:
        reader = list(csv.DictReader(f))
    
    initial_count = len(reader)
    print(f"[*] Total records ingested: {initial_count}")
    
    seen = set()
    cleaned_rows = []
    
    total_sales = 0.0
    total_profit = 0.0
    total_quantity = 0
    
    for row in reader:
        # Deduplication key
        key = (row['OrderID'], row['ProductID'])
        if key in seen:
            continue
        seen.add(key)
        
        # String trimming
        for k in ['ShipMode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'SubCategory', 'ProductName']:
            if k in row:
                row[k] = row[k].strip()
                
        # Dates and Temporal Features
        dt_order = datetime.strptime(row['OrderDate'], '%Y-%m-%d')
        dt_ship = datetime.strptime(row['ShipDate'], '%Y-%m-%d')
        
        row['OrderYear'] = str(dt_order.year)
        row['OrderMonth'] = str(dt_order.month)
        row['OrderMonthName'] = dt_order.strftime('%B')
        row['YearMonth'] = dt_order.strftime('%Y-%m')
        quarter = (dt_order.month - 1) // 3 + 1
        row['OrderQuarter'] = f"Q{quarter}"
        row['DayOfWeek'] = dt_order.strftime('%A')
        row['ShippingDurationDays'] = str((dt_ship - dt_order).days)
        
        # Financial & Margin Calculations
        sales = float(row['Sales'])
        profit = float(row['Profit'])
        quantity = int(row['Quantity'])
        discount = float(row['Discount'])
        
        margin_pct = round((profit / sales) * 100, 2) if sales > 0 else 0.0
        row['ProfitMarginPct'] = str(margin_pct)
        row['UnitPrice'] = str(round(sales / quantity, 2)) if quantity > 0 else "0.0"
        
        # Discount tier
        if discount <= 0:
            row['DiscountTier'] = 'No Discount'
        elif discount <= 0.10:
            row['DiscountTier'] = 'Low (1-10%)'
        elif discount <= 0.20:
            row['DiscountTier'] = 'Moderate (11-20%)'
        else:
            row['DiscountTier'] = 'High (>20%)'
            
        row['IsProfitable'] = 'True' if profit > 0 else 'False'
        
        total_sales += sales
        total_profit += profit
        total_quantity += quantity
        cleaned_rows.append(row)
        
    os.makedirs(os.path.dirname(processed_filepath), exist_ok=True)
    if cleaned_rows:
        fieldnames = list(cleaned_rows[0].keys())
        with open(processed_filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(cleaned_rows)
            
    print(f"[+] Cleaned dataset saved to: {processed_filepath} ({len(cleaned_rows)} records)")
    overall_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
    print("\n--- Summary Performance Metrics ---")
    print(f"Total Sales Revenue : ${total_sales:,.2f}")
    print(f"Total Gross Profit  : ${total_profit:,.2f}")
    print(f"Overall Net Margin  : {overall_margin:.2f}%")
    print(f"Total Units Sold    : {total_quantity:,}")
    print(f"Total Transactions  : {len(cleaned_rows):,}")
    print("------------------------------------\n")

def clean_sales_data(raw_filepath: str, processed_filepath: str):
    try:
        import pandas as pd
        import numpy as np
        
        print(f"[*] Pandas Mode: Reading raw dataset from {raw_filepath}")
        df = pd.read_csv(raw_filepath)
        df = df.drop_duplicates()
        
        text_cols = ['ShipMode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'SubCategory', 'ProductName']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
                
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])
        df['ShipDate'] = pd.to_datetime(df['ShipDate'])
        df['OrderYear'] = df['OrderDate'].dt.year
        df['OrderMonth'] = df['OrderDate'].dt.month
        df['OrderMonthName'] = df['OrderDate'].dt.strftime('%B')
        df['YearMonth'] = df['OrderDate'].dt.to_period('M').astype(str)
        df['OrderQuarter'] = 'Q' + df['OrderDate'].dt.quarter.astype(str)
        df['DayOfWeek'] = df['OrderDate'].dt.day_name()
        df['ShippingDurationDays'] = (df['ShipDate'] - df['OrderDate']).dt.days
        
        df['ProfitMarginPct'] = np.where(df['Sales'] > 0, (df['Profit'] / df['Sales']) * 100, 0.0).round(2)
        df['UnitPrice'] = (df['Sales'] / df['Quantity']).round(2)
        
        bins = [-0.01, 0.0, 0.10, 0.20, 1.0]
        labels = ['No Discount', 'Low (1-10%)', 'Moderate (11-20%)', 'High (>20%)']
        df['DiscountTier'] = pd.cut(df['Discount'], bins=bins, labels=labels)
        df['IsProfitable'] = df['Profit'] > 0
        
        os.makedirs(os.path.dirname(processed_filepath), exist_ok=True)
        df.to_csv(processed_filepath, index=False)
        print(f"[+] Cleaned dataset saved to: {processed_filepath} ({len(df)} rows)")
        
        total_sales = df['Sales'].sum()
        total_profit = df['Profit'].sum()
        overall_margin = (total_profit / total_sales) * 100
        print("\n--- Summary Performance Metrics ---")
        print(f"Total Sales Revenue : ${total_sales:,.2f}")
        print(f"Total Gross Profit  : ${total_profit:,.2f}")
        print(f"Overall Net Margin  : {overall_margin:.2f}%")
        print(f"Total Units Sold    : {df['Quantity'].sum():,}")
        print(f"Total Transactions  : {len(df):,}")
        print("------------------------------------\n")
    except ImportError:
        clean_with_stdlib(raw_filepath, processed_filepath)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_dir, "data", "raw", "sales_data_raw.csv")
    proc_path = os.path.join(base_dir, "data", "processed", "sales_data_cleaned.csv")
    clean_sales_data(raw_path, proc_path)
