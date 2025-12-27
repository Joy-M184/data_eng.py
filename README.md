📦 Data Engineering Job Scraper (data_eng.py)
This project is a Python-based web scraper that collects real Data Engineering job postings from the UK Government’s Find a Job website. It extracts raw job information, cleans and structures the data, and loads it into a PostgreSQL database for analysis.

🎯 What This Project Does
After scraping the raw job listings, the pipeline performs several data engineering transformations:

Data Extraction
Job title

Company

Location

Salary text

Date posted

Data Cleaning & Transformation
Extracted postcode from messy location strings

Extracted min_salary using regex

Extracted max_salary using regex

Converted salary fields to numeric

Handled missing values safely

Reordered columns into a clean, logical structure

Saved cleaned dataset to cleaned_jobs.csv

Database Integration
Connected to PostgreSQL using SQLAlchemy

Uploaded the cleaned dataset into a relational table

Verified connection and data load successfully

🛠️ Tech Stack
Python

Selenium

BeautifulSoup

pandas

Regex

SQLAlchemy

PostgreSQL

✨ Features
Scrapes live job listings from a real government portal

Extracts 5+ structured fields per job

Cleans and enriches salary data with min/max values

Extracts postcode from location strings

Handles missing or inconsistent fields gracefully

Outputs clean CSV files for analysis

Uploads data to PostgreSQL for querying

Reusable, modular code structure