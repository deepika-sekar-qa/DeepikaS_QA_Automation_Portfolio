# DeepikaS_QA_Automation_Portfolio

##  Overview
This repository contains two complete Selenium Python automation frameworks:

1. **SauceDemo_Automation**
2. **HerokuApp_Automation**

Each project demonstrates:
- Page Object Model (POM) framework
- Selenium WebDriver automation using Python
- Pytest for test execution
- Allure and HTML reporting for visualization
- Simulated bug examples and professional documentation

---

##  How to Run the Projects

### 1.Clone this Repository
```bash
git clone https://github.com/deepika-sekar-qa/DeepikaS_QA_Automation_Portfolio.git

2.Navigate to a Project
cd SauceDemo_Automation
OR
cd HerokuApp_Automation

3️. Install Dependencies
pip install -r requirements.txt

4️. Run Tests with HTML Report
pytest -s Tests/test_app_feature.py --html=Reports/report.html --self-contained-html

or (for HerokuApp)

pytest -s Tests/test_login.py --html=Reports/report.html --self-contained-html

5️. Run Tests with Allure Report
pytest -s Tests/test_app_feature.py --alluredir=Reports/allure-results
allure serve Reports/allure-results

or (for HerokuApp)

pytest -s Tests/test_login.py --alluredir=Reports/allure-results
allure serve Reports/allure-results

  Future Integrations & Version Control Setup

 Integrated Allure Reporting for visual test analytics
 Added requirements.txt for one-click dependency installation
 Captured and documented simulated bug examples
 Uploaded project to GitHub (Public Repository)
 Ready for CI/CD and GitHub Actions setup

 Portfolio Documentation

SauceDemo_Portfolio_DeepikaS.docx

HerokuApp_Portfolio_DeepikaS.docx

Author
Deepika Sekar
Email: deepika.sekar.qa@gmail.com
GitHub: https://github.com/deepika-sekar-qa

This QA Automation Portfolio demonstrates hands-on experience in building end-to-end Selenium Python frameworks with Allure reporting and CI/CD readiness.
