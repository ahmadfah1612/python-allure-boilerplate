import pytest
import os
import allure
from datetime import datetime


def pytest_configure(config):
    """Create allure results directory and environment file"""
    allure_dir = "allure-results"
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)

    # Add environment info
    with open(f"{allure_dir}/environment.properties", "w") as f:
        f.write("Framework=Pytest")
        f.write("Timestamp={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        f.write("Base_URL=https://jsonplaceholder.typicode.com")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach additional test info to Allure report"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Add test docstring to Allure report
        if str(item.function.__doc__).strip():
            allure.dynamic.description(str(item.function.__doc__).strip())
