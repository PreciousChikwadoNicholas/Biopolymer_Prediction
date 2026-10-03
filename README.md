# Agricultural Biopolymer Yield Prediction Pipeline

## Overview
An end-to-end data engineering and machine learning pipeline designed to store agricultural waste extraction parameters in a relational database and predict biopolymer yield using Python and scikit-learn.

## Architecture
- **Database**: Microsoft SQL Server (`agri_biopolymer_db`) storing experimental extraction records (`dbo.BIOPOLYMER_EXTRACTIONS`).
- **Data Engineering**: Python (`pandas`, `pyodbc`) for secure extraction and data frame transformation.
- **Machine Learning**: `scikit-learn` Linear Regression model trained to evaluate experimental yields based on process purity.

## Tech Stack
- Python 3.10
- SQL Server Management Studio (SSMS)
- PyCharm IDE
-