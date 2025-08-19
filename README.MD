QA End-to-End Automation Framework - SauceDemo + BigCommerce + AWS

Python



Playwright



Selenium



AWS



Pytest



MIT License




Project Description

This repository contains a QA End-to-End automation framework for testing web applications, including SauceDemo and BigCommerce.

It uses Playwright, Selenium, and Jinja2 templates for dynamic reports, and integrates with AWS services to scale test execution in cloud environments.



Tech Stack


Python – main programming language

Playwright – browser automation (Chromium, Firefox, WebKit)

Selenium – traditional browser automation

Jinja2 – dynamic templates for test reports

AWS Services:

Lambda (serverless functions)

API Gateway (HTTP/REST APIs)

DynamoDB (NoSQL database)



HTML & CSS – for test reports and UI templates



Features


End-to-End automation for SauceDemo and BigCommerce

Supports UI, API, Integration, Performance, Security, Regression, Usability, and Compatibility tests

Real-time webhook processing via AWS Lambda

Dynamic HTML reports using Jinja2 templates

Screenshots and video recording of test runs

Cloud integration for scalable test execution



Project Structure
cloudqa-plus/
│
├── TESTS_CASES/
│ ├── API TEST/
│ ├── UI TEST/
│ ├── I COMPATIBILITY TEST/
│ ├── INTEGRATION TEST/
│ ├── PERFORMANCE TEST/
│ ├── REGRESSION TEST/
│ ├── SECURITY TEST/
│ └── USABILITY TEST/
│
├── reports/ # Generated test reports
├── pipeline/ # CI/CD configuration files
├── dashboards/ # Test dashboards
├── alerts/ # Notification configurations
├── infra/ # Infrastructure files (AWS setup)
├── venv/ # Python virtual environment
├── requirements.txt # Project dependencies
└── README.md # This file

copy
download

---

## Virtual Environment Setup
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
Linux/Mac:

copy
download
python -m venv venv
source venv/bin/activate
Upgrade pip:

copy
download
pip install --upgrade pip
Install Dependencies
copy
download
pip install -r requirements.txt
Essential libraries:

pytest – testing framework
selenium – browser automation
webdriver-manager – automatic driver management
pytest-xdist – parallel execution
pytest-html – HTML reports
pytest-mock – mocks for tests
pytest-cov – test coverage
playwright – modern browser automation
jinja2 – dynamic report templates
Install Playwright browsers:

copy
download
python -m playwright install
How to Run Tests
Run all tests:

copy
download
pytest
Run specific folder:

copy
download
pytest TESTS_CASES/API\ TEST/TESTS/
Topics / Tags
python, playwright, selenium, jinja2, aws, automation, qa, e2e-tests, bigcommerce, saucedemo

License
MIT License

