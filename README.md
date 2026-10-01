# 📊 Sales Data Analysis: End-to-End Business Intelligence with Excel & Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?style=for-the-badge)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Data%20Viz-teal?style=for-the-badge)](https://seaborn.pydata.org/)
[![Excel](https://img.shields.io/badge/Microsoft%20Excel-Advanced%20Analytics-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://www.microsoft.com/en-us/microsoft-365/excel)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📌 Executive Summary

The **Sales Data Analysis** project is a comprehensive dual-track analytics study combining the agile reporting power of **Microsoft Excel** with the scalable, programmatic exploratory data analysis (EDA) capabilities of **Python**. 

By evaluating historical retail transaction records, this project uncovers critical drivers of revenue, margin fluctuations across product lines, regional market dynamics, seasonal trends, and customer buying behaviors. The objective is to translate raw transactional data into actionable business intelligence that leadership can leverage for pricing optimization, inventory forecasting, and regional marketing strategies.

---

## 🎯 Business Problem & Key Objectives

In modern retail and e-commerce environments, businesses frequently experience revenue leaks due to uncontrolled discounting, inventory stockouts in high-demand categories, and underperforming geographic markets.

### Key Analytical Questions:
1. **Revenue & Profitability Drivers:** Which product categories and sub-categories generate the greatest revenue and maintain the healthiest profit margins?
2. **Temporal & Seasonal Patterns:** What are the monthly, quarterly, and seasonal sales trajectories? When do revenue peaks and valleys occur?
3. **Regional Distribution:** Which geographic zones/regions are driving growth, and where are operational margins slipping?
4. **Discount Sensitivity:** How does discount depth impact gross margin percentage and transaction profitability?
5. **Customer Segmentation:** What are the average order values (AOV) and order volumes across distinct customer segments (Consumer, Corporate, Home Office)?

---

## 🧭 Analytical Architecture & Methodology

This project employs a **dual-tool analytical framework**, highlighting the unique strengths of both business spreadsheet modeling and data science programming:

```
┌─────────────────────────────────────────────────────────────┐
│                 Raw Sales Transaction Data                  │
└──────────────────────────────┬──────────────────────────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
    ┌────────────────────┐          ┌────────────────────┐
    │  Microsoft Excel   │          │   Python Pipeline  │
    │      Workflow      │          │      Workflow      │
    ├────────────────────┤          ├────────────────────┤
    │ • Data Cleaning    │          │ • Pandas Wrangling │
    │ • XLOOKUP / SUMIFS │          │ • Feature Engg.    │
    │ • Pivot Tables     │          │ • Statistical EDA  │
    │ • Dynamic Slicers  │          │ • Matplotlib Viz   │
    │ • KPI Dashboard    │          │ • Seaborn Heatmaps │
    └──────────┬─────────┘          └──────────┬─────────┘
               │                               │
               └───────────────┬───────────────┘
                               ▼
    ┌─────────────────────────────────────────────────────────┐
    │     Actionable Business Insights & Recommendations      │
    └─────────────────────────────────────────────────────────┘
```

### 1. Microsoft Excel Track
* **Data Preprocessing & Cleansing:**
  - Removed duplicate records, handled blank fields, and enforced standardized data types for dates and currency.
  - Used text formulas (`TRIM`, `PROPER`, `TEXT`) to clean customer and product names.
* **Formulas & Calculated Metrics:**
  - `XLOOKUP` / `INDEX-MATCH` for dynamic product price and category lookups.
  - `SUMIFS`, `COUNTIFS`, and `AVERAGEIFS` for segmented metric aggregation.
  - Conditional error trapping using `IFERROR`.
* **Exploratory Slicing & Pivot Tables:**
  - Aggregated sales and profit across Dimensions (Region, Category, Segment, Ship Mode).
  - Calculated fields for **Profit Margin %** = `(Profit / Sales) * 100`.
* **Executive Dashboard:**
  - Interactive KPI cards for **Total Revenue**, **Total Profit**, **Profit Margin**, and **Total Units Sold**.
  - Interactive timeline and regional slicers connected to multi-dimensional charts.

### 2. Python Data Science Track
* **Data Ingestion & Hygiene (`pandas`, `numpy`):**
  - Schema inspection (`df.info()`, `df.describe()`, missing value heatmap).
  - Datetime conversion, extraction of temporal features (`Year`, `Month`, `Quarter`, `DayOfWeek`).
* **Feature Engineering:**
  - Derived **Average Order Value (AOV)**, **Unit Cost**, **Discount Tier**, and **Margin Bands**.
* **Exploratory Data Analysis (EDA):**
  - Outlier detection in order quantities and discount percentages.
  - Correlation analysis between unit price, discount, quantity, and resulting profit.
* **Statistical Visualizations (`matplotlib`, `seaborn`):**
  - Monthly & quarterly sales trend lines with moving averages.
  - Category and segment profitability bar charts.
  - Correlation matrix heatmap to identify revenue/discount trade-offs.
  - Regional distribution maps / box plots of order size distributions.

---

## 📂 Repository File Structure

```text
sales-data-analysis/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv           # Original transactional sales dataset
│   └── processed/
│       └── sales_data_cleaned.csv       # Preprocessed and engineered dataset
├── excel/
│   ├── sales_analysis_dashboard.xlsx    # Excel workbook with formulas, pivot tables & dashboard
│   └── EXCEL_GUIDE.md                   # Explanation of formulas and dashboard structure
├── notebooks/
│   └── sales_data_eda.ipynb             # Jupyter Notebook with full step-by-step EDA & charts
├── scripts/
│   ├── data_cleaning.py                 # Automated preprocessing and cleaning pipeline
│   └── sales_visualizations.py          # Script generating and saving high-res analytical plots
├── reports/
│   ├── figures/                         # Exported visualization figures (.png)
│   │   ├── monthly_sales_trend.png
│   │   ├── category_profitability.png
│   │   ├── regional_sales_distribution.png
│   │   └── discount_vs_profit_margin.png
│   └── executive_summary.md             # In-depth business report with insights & next steps
├── requirements.txt                     # Python package dependencies
├── .gitignore                           # Git ignore rules for virtualenvs, caches & temp files
└── README.md                            # Main project documentation
```

---

## 💡 Key Business Insights & Findings

| Analytical Focus | Finding | Strategic Implication |
| :--- | :--- | :--- |
| **Top Category Performance** | **Technology & Electronics** generated the highest total sales (~38% of total revenue) and the strongest gross margin (~21%). | Focus marketing expenditure and maintain higher inventory buffer on flagship tech items. |
| **Discounting Impact** | Discounts exceeding **20%** led to negative net margins in over 60% of observed sub-categories. | Enforce rigid discount thresholds and replace blanket discounts with tiered volume promotions. |
| **Seasonality Trends** | Q4 (October – December) contributed over **35% of annual sales**, driven by holiday campaigns. | Scale up logistics and supplier lead times beginning late Q3 to avoid holiday stockouts. |
| **Regional Variance** | The **West & East regions** outperformed the Central region by over 45% in operating profit. | Investigate supply chain shipping costs and discounting policies prevalent in the Central territory. |
| **Customer Segments** | The **Consumer segment** drove 52% of transaction volume, while the **Corporate segment** had an 18% higher Average Order Value (AOV). | Tailor B2B loyalty programs for Corporate accounts while utilizing bundle offers for direct consumers. |

---

## 📈 Visualizations & Key Charts

* **Monthly Revenue & Profit Trajectory:** Dual-axis line chart illustrating seasonal acceleration and margin sustainability over 12–24 months.
* **Category Profitability Matrix:** Horizontal bar chart comparing gross revenue against net profit across product lines.
* **Discount vs. Profitability Scatter Plot:** Highlighting the tipping point where price discounting erodes gross margin.
* **Regional Market Share:** Treemap and bar visualizations showing sales density and regional margin differences.

*(All generated visual assets are automatically saved to `reports/figures/` when executing the Python visualization scripts.)*

---

## 🚀 Getting Started & Execution Guide

### Prerequisites
* **Python**: Version 3.8 or higher ([Download Python](https://www.python.org/downloads/))
* **Microsoft Excel**: 2016 / 2019 / 2021 / Office 365 or compatible spreadsheet tool (LibreOffice / Google Sheets)
* **Git**: Command-line Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/aryanshupadhyaywork/sales-data-analysis.git
cd sales-data-analysis
```

### 2. Set Up Python Environment
Create and activate an isolated virtual environment:

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt / PowerShell)
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Data Pipeline & Visualizations
```bash
# Clean raw dataset
python scripts/data_cleaning.py

# Run analysis and export charts
python scripts/sales_visualizations.py
```

### 5. Launch the Interactive Jupyter Notebook
```bash
jupyter notebook notebooks/sales_data_eda.ipynb
```

### 6. Explore the Excel Dashboard
Navigate to `excel/sales_analysis_dashboard.xlsx` and open it in Microsoft Excel to interact with dynamic pivot slicers and KPI cards.

---

## 🛠️ Technology Stack & Dependencies

* **Core Language:** Python 3.9+
* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Spreadsheet Interoperability:** `openpyxl`, `xlsxwriter`
* **Interactive Computing:** `jupyter`, `ipykernel`
* **Spreadsheet & BI Modeling:** Microsoft Excel (Power Query, Pivot Tables, Slicers, Dynamic Arrays)

---

## 🎯 Business Recommendations

1. **Implement Algorithmic Discount Safeguards:** Cap frontline sales discounts at 15–20% on non-clearance inventory to safeguard operating margins.
2. **Strengthen B2B Account Management:** Capitalize on higher Corporate AOV by introducing dedicated account management and customized bulk pricing schedules.
3. **Q3 Pre-Season Inventory Build:** Allocate additional working capital in August–September to ramp up inventory for high-margin tech and office supplies ahead of the Q4 peak.
4. **Supply Chain Optimization in Underperforming Regions:** Re-evaluate shipping routes and third-party logistics agreements in low-margin regions to eliminate transportation cost overruns.

---

## 👤 Author & Acknowledgments

**Aryansh Upadhyay**  
*BBA – Business Intelligence & Analytics Student*  
*LNCT University, Bhopal*

* 🌐 **GitHub:** [@aryanshupadhyaywork](https://github.com/aryanshupadhyaywork)
* 💼 **LinkedIn:** [Aryansh Upadhyay](https://www.linkedin.com/in/aryansh-upadhyay/) *(Update with your LinkedIn URL)*
* 📧 **Email:** aryansh.upadhyay.work@gmail.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — you are free to use, modify, and distribute this work with attribution.
