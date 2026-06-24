# Mutual Fund Capstone Project

## Overview

This project focuses on Mutual Fund data analysis using Python, Pandas, and related data science libraries. The objective is to ingest, validate, and analyze mutual fund datasets and fetch live NAV (Net Asset Value) data from external APIs.

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
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Requests
* SciPy
* Jupyter Notebook

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

## Day 1 Tasks Completed

### Project Setup

* Created project folder structure.
* Initialized Git repository.
* Connected project to GitHub.

### Dependency Installation

Installed required Python libraries and created `requirements.txt`.

### Data Ingestion

Loaded all 10 CSV datasets using Pandas and reviewed:

* Dataset shape
* Data types
* Sample records

### Live NAV Fetching

Fetched live NAV data from MFAPI and saved the response as CSV.

### Data Quality Checks

* Verified dataset loading.
* Reviewed column data types.
* Identified missing values in selected fields.
* Prepared for AMFI code validation.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run data ingestion:

```bash
python data_ingestion.py
```

Run live NAV fetch:

```bash
python live_nav_fetch.py
```

