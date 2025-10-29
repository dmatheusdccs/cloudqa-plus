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



## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)




Features


End-to-End automation for SauceDemo and BigCommerce

Supports UI, API, Integration, Performance, Security, Regression, Usability, and Compatibility tests

Real-time webhook processing via AWS Lambda

Dynamic HTML reports using Jinja2 templates

Screenshots and video recording of test runs

Cloud integration for scalable test execution



Project Structure
```bash
cloudqa-plus/
│
├── TESTS_CASES/
│   ├── API TEST/
│   ├── UI TEST/
│   ├── COMPATIBILITY TEST/
│   ├── INTEGRATION TEST/
│   ├── PERFORMANCE TEST/
│   ├── REGRESSION TEST/
│   ├── SECURITY TEST/
│   └── USABILITY TEST/
│
├── reports/          # Generated test reports
├── pipeline/         # CI/CD configuration files
├── dashboards/       # Test dashboards
├── alerts/           # Notification configurations
├── infra/            # Infrastructure files (AWS setup)
├── venv/             # Python virtual environment
├── requirements.txt  # Project dependencies
└── README.md         # This file


---

## Virtual Environment Setup
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
Linux/Mac:


python -m venv venv
source venv/bin/activate
Upgrade pip:


pip install --upgrade pip
Install Dependencies

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


python -m playwright install
How to Run Tests
Run all tests:


pytest
Run specific folder:


pytest TESTS_CASES/API\ TEST/TESTS/
Topics / Tags
python, playwright, selenium, jinja2, aws, automation, qa, e2e-tests, bigcommerce, saucedemo

License
MIT License

