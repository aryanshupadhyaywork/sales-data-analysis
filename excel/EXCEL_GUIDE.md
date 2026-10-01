# 📑 Microsoft Excel Analysis & Dashboard Guide

This guide details the Excel workflow, analytical calculations, pivot tables, and dashboard design used in the **Sales Data Analysis** project.

---

## 🏗️ Workbook Architecture

The analysis workbook is structured into four dedicated worksheets for modularity and auditability:

```
sales_analysis_dashboard.xlsx
├── 1. 🗃️ Raw_Data          (Untouched transactional records)
├── 2. 🧹 Cleaned_Data      (Standardized data types, trimmed fields, derived columns)
├── 3. 📊 Pivot_Calculations (Dynamic aggregations across Category, Region, Time, Segment)
└── 4. 🎛️ Executive_Dashboard(Interactive KPI cards, charts, and slicers)
```

---

## 🧼 1. Data Cleaning & Standardization Formulas

| Objective | Formula Example | Description |
| :--- | :--- | :--- |
| **Remove Leading/Trailing Whitespace** | `=TRIM(A2)` | Ensures accurate grouping in pivot tables and lookup operations. |
| **Proper Case Formatting** | `=PROPER(F2)` | Standardizes customer and city names (e.g., "alex johnson" -> "Alex Johnson"). |
| **Safe Margin Calculation** | `=IFERROR(T2/Q2, 0)` | Computes `Profit / Sales` while suppressing `#DIV/0!` errors on free/zero-revenue transactions. |
| **Order Duration (Days)** | `=INT(C2 - B2)` | Evaluates fulfillment speed by subtracting `Order Date` from `Ship Date`. |
| **Quarter Tagging** | `="Q" & ROUNDUP(MONTH(B2)/3, 0)` | Automatically tags dates with their fiscal/calendar quarter (Q1-Q4). |

---

## 🔍 2. Lookup & Segmented Aggregations

### Dynamic Product Price & Category Lookup
```excel
=XLOOKUP(M2, Product_Catalog!A:A, Product_Catalog!B:B, "Not Found", 0)
```
*Retrieves product categories or base catalog prices dynamically based on `ProductID`.*

### Conditional Segment Revenue Aggregation
```excel
=SUMIFS(Cleaned_Data!Q:Q, Cleaned_Data!L:L, "West", Cleaned_Data!N:N, "Technology")
```
*Calculates total sales revenue specifically for the Technology category in the West region.*

### Segmented Average Order Value (AOV)
```excel
=AVERAGEIFS(Cleaned_Data!Q:Q, Cleaned_Data!G:G, "Corporate")
```
*Determines average order value for Corporate accounts.*

---

## 📊 3. Pivot Tables & Summary Analysis

### Pivot Table 1: Category & Sub-Category Performance
* **Rows:** `Category`, `SubCategory`
* **Values:**
  * `Sum of Sales` (Formatted as Currency `$#,##0`)
  * `Sum of Profit` (Formatted as Currency `$#,##0`)
  * Calculated Field: `Profit Margin %` = `('Profit' / 'Sales')` (Formatted as Percentage `0.0%`)
* **Sort:** Descending by `Sum of Sales`.

### Pivot Table 2: Regional Sales & Profit Comparison
* **Rows:** `Region`
* **Columns:** `Segment`
* **Values:** `Sum of Profit`
* **Visual:** Stacked column chart comparing profitability across territories.

### Pivot Table 3: Monthly Trend & Seasonality
* **Rows:** `OrderDate` (Grouped by `Years` and `Months`)
* **Values:** `Sum of Sales`, `Sum of Profit`
* **Visual:** Dual-axis combination chart (Line chart for sales, Bar chart for profit).

---

## 🎛️ 4. Executive Dashboard Components

1. **Top KPI Scorecards:**
   * **Gross Sales Revenue:** Highlighting year-to-date sales with trend indicators.
   * **Net Profit:** Total dollar profit earned across all transactions.
   * **Blended Margin %:** Overall operating efficiency ratio.
   * **Total Units Shipped:** Total volume of products fulfilled.
2. **Interactive Slicers:**
   * `Region` (West, East, Central, South)
   * `Category` (Technology, Furniture, Office Supplies)
   * `Order Year / Quarter` (Dynamic timeline filtering)
   * `Customer Segment` (Consumer, Corporate, Home Office)
3. **Charts & Visual Hierarchy:**
   * **Sales by Category:** Bar chart comparing revenue volume.
   * **Monthly Trajectory:** Continuous trend line displaying seasonal spikes in Q4.
   * **Discount Sensitivity:** Scatter plot of discount tiers against profit yield.
