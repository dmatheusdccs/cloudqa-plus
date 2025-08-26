import pytest
import subprocess
import os

LOG_GROUP = "/aws/lambda/cloudqa-webhook-transform"
TABLE_NAME = "ProductUpdatesTransformed"
GENERATE_REPORT_SCRIPT = os.path.join(os.path.dirname(__file__), "../../generate_report.py")

def pytest_sessionfinish(session, exitstatus):
    """
    Hook de Pytest que se ejecuta al final de todos los tests.
    Llama automáticamente a generate_report.py para crear el HTML.
    """
    print("\n--- Generating automated QA report ---")
    subprocess.run(["python", GENERATE_REPORT_SCRIPT, LOG_GROUP, TABLE_NAME])
