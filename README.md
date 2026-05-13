# African Device Financing Risk Analytics

## Overview

This project simulates an end-to-end telecom and fintech analytics platform for African smartphone financing markets.

The platform demonstrates:

- Synthetic telecom-fintech data generation
- Data quality validation frameworks
- ETL transformation pipelines
- Executive KPI reporting
- Risk segmentation analytics
- CI/CD-ready project structure
- Data engineering best practices

---

## Business Context

Smartphone financing is a major driver of digital inclusion across African telecom markets.

This project simulates how mobile network operators and fintech partners can use alternative data sources to analyze:

- Customer repayment behavior
- Credit risk exposure
- Device financing performance
- Market-level portfolio health
- Financial inclusion trends

Markets simulated include:

- South Africa
- Tanzania
- Mozambique
- DRC
- Lesotho
- Kenya
- Ethiopia
- Egypt

---

## Project Architecture

```
african-device-financing-risk-analytics/
│
├── data/
│   ├── device_financing_data.csv
│   └── processed_device_financing_data.csv
│
├── docs/
│
├── notebooks/
│
├── src/
│   ├── generate_data.py
│   ├── data_quality.py
│   ├── etl_pipeline.py
│   └── kpi_dashboard.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Data Engineering Components

### 1. Synthetic Data Generation
Generates telecom-fintech customer financing data using Python, NumPy, Pandas, and Faker.

### 2. Data Quality Validation
Implements governance checks including:
- Null validation
- Domain validation
- Financial consistency checks
- Risk category validation

### 3. ETL Pipeline
Transforms raw financing data into analytics-ready datasets with engineered features such as:
- Deposit ratio
- Loan-to-income ratio
- Default flags
- High-risk indicators

### 4. KPI Dashboard
Produces executive-level portfolio insights including:
- Total loan book
- Default rates
- Market performance
- Risk segmentation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Faker
- GitHub
- VS Code

---

## Future Enhancements

Planned future enhancements include:

- Machine learning credit scoring
- Power BI dashboards
- CI/CD automation with GitHub Actions
- Unit testing frameworks
- Cloud deployment
- API integration
- Real-time analytics pipelines

---

## Author

Dr. Mfanasibili Ngwenya

Telecom | AI | Fintech | Data Engineering