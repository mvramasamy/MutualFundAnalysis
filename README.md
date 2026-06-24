# Mutual Fund Capstone Project

## Overview

This project focuses on Mutual Fund data analysis using Python, Pandas, SQL, and SQLite. The objective is to ingest, clean, validate, store, and analyze mutual fund datasets while fetching live NAV (Net Asset Value) data from external APIs.

---

## Project Structure

```text
MutualFundAnalysis/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── data_ingestion.py
├── live_nav_fetch.py
├── clean_nav_history.py
├── clean_investor_transactions.py
├── clean_scheme_performance.py
├── load_to_sqlite.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* SQLite
* Requests
* SciPy
* Jupyter Notebook

---

## Datasets

The project uses the following datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

# Day 1: Project Setup + Data Ingestion (ETL)

## Project Setup

* Created project folder structure.
* Initialized Git repository.
* Connected project to GitHub.

## Dependency Installation

Installed required Python libraries and created `requirements.txt`.

## Data Ingestion

Loaded all 10 CSV datasets using Pandas and reviewed:

* Dataset shape
* Data types
* Sample records

## Live NAV Fetching

Fetched live NAV data from MFAPI and saved the response as CSV.

## Data Quality Checks

* Verified dataset loading.
* Reviewed column data types.
* Identified missing values in selected fields.
* Prepared for AMFI code validation.

---

# Day 2: Data Cleaning + SQLite Database Design

## Data Cleaning

### NAV History Cleaning

Performed the following operations:

* Converted date column to datetime format.
* Sorted records by AMFI code and date.
* Removed duplicate records.
* Validated NAV values (> 0).
* Saved cleaned dataset.

Output:

* `cleaned_nav_history.csv`

### Investor Transactions Cleaning

Performed the following operations:

* Standardized transaction types.
* Validated transaction amounts.
* Verified KYC status values.
* Checked date formats.
* Saved cleaned dataset.

Output:

* `cleaned_investor_transactions.csv`

### Scheme Performance Cleaning

Performed the following operations:

* Validated return columns.
* Checked expense ratio values.
* Identified anomalies.
* Saved cleaned dataset.

Output:

* `cleaned_scheme_performance.csv`

---

## SQLite Database Creation

Created SQLite database using SQLAlchemy.

Database File:

```text
bluestock_mf.db
```

Loaded cleaned datasets into SQLite tables for further analysis.

Verified successful database creation and table loading.

---

## Data Validation

Performed:

* Duplicate checks
* Missing value checks
* Data type validation
* Expense ratio validation
* NAV validation

---

## Deliverables Completed

### Day 1

* data_ingestion.py
* live_nav_fetch.py
* requirements.txt
* GitHub repository setup

### Day 2

* clean_nav_history.py
* clean_investor_transactions.py
* clean_scheme_performance.py
* load_to_sqlite.py
* cleaned CSV datasets
* SQLite database (bluestock_mf.db)

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Ingestion

```bash
python data_ingestion.py
```

### Fetch Live NAV

```bash
python live_nav_fetch.py
```

### Clean NAV History

```bash
python clean_nav_history.py
```

### Clean Investor Transactions

```bash
python clean_investor_transactions.py
```

### Clean Scheme Performance

```bash
python clean_scheme_performance.py
```

### Load Data into SQLite

```bash
python load_to_sqlite.py
```

---

## Git Commits

### Day 1

```bash
git commit -m "Day 1: Data ingestion complete"
```

### Day 2

```bash
git commit -m "Day 2: Cleaned data + SQLite DB loaded"
```

---


