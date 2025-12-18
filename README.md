Data Engineering Job Scraper (data_eng.py)
This project is a Python-based web scraper that collects real job postings for Data Engineering roles from the UK Government’s Find a Job website. It extracts structured information such as:

Job title

Company

Location

Salary

Date posted

The scraper uses Selenium to load dynamic content and BeautifulSoup to parse the HTML. The final dataset is exported as a clean CSV file for analysis.

Why This Project Exists
I built this project to practice real-world data engineering skills:

Extracting structured data from messy HTML

Understanding page structure and selectors

Handling missing or inconsistent fields

Building a repeatable ETL-style pipeline

Converting raw data into a usable dataset

This project demonstrates my ability to work with web data, automate extraction, and prepare datasets for analysis.

Tech Stack
Python

Selenium

BeautifulSoup

Pandas

Features
✅ Scrapes live job listings ✅ Extracts 5+ fields per job ✅ Handles missing data safely ✅ Converts results into a DataFrame ✅ Saves output to jobs.csv ✅ Clean, reusable code structure