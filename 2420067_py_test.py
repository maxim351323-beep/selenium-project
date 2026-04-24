"""
Tech_world Website — Selenium Test Suite
==========================================
Student ID : 2420067
Framework  : Pytest + Selenium WebDriver
Browser    : Google Chrome (mandatory)

HOW TO RUN:
  1. pip install pytest selenium
  2. Make sure chromedriver is on PATH (same version as your Chrome)
  3. Set BASE_URL below to the path of your index.html
  4. pytest 2420067_py_test.py -v
"""

import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ─────────────────────────────────────────────────────────────────────
#  CONFIGURATION  ← change BASE_URL to your actual path
# ─────────────────────────────────────────────────────────────────────
# Example Windows : "file:///C:/Users/YourName/Desktop/index.html"
# Example Mac/Linux: "file:///home/yourname/project/index.html"
BASE_URL = r"file:///C:\Users\maxim\Downloads\selenium_project\index.html"
USERNAME = "admin"
PASSWORD = "@Dm1n"
WAIT     = 10   # seconds for explicit waits


# ─────────────────────────────────────────────────────────────────────
#  FIXTURE — opens Chrome once for the whole test class
# ─────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # Uncomment next line to run without a visible browser window (CI mode):
    # options.add_argument("--headless=new")

    drv = webdriver.Chrome(options=options)
    drv.get(BASE_URL)
    yield drv
    drv.quit()


# ─────────────────────────────────────────────────────────────────────
#  HELPER
# ─────────────────────────────────────────────────────────────────────
def wait_visible(driver, by, value):
    """Wait up to WAIT seconds until element is visible, then return it."""
    return WebDriverWait(driver, WAIT).until(
        EC.visibility_of_element_located((by, value))
    )

def wait_clickable(driver, by, value):
    """Wait until element is clickable, then return it."""
    return WebDriverWait(driver, WAIT).until(
        EC.element_to_be_clickable((by, value))
    )


# ═════════════════════════════════════════════════════════════════════
#  TEST CLASS
# ═════════════════════════════════════════════════════════════════════
class TestTechWorld:

    # ── 1. LOGIN PAGE ─────────────────────────────────────────────────
    def test_01_login_page_loads(self, driver):
        """Login form is visible when the site first opens."""
        username_field = wait_visible(driver, By.ID, "username")
        assert username_field.is_displayed(), "Username field not visible on login page"

    def test_02_login_error_on_wrong_credentials(self, driver):
        """Wrong credentials must show an error message."""
        driver.find_element(By.ID, "username").send_keys("wrong")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.ID, "login-btn").click()
        time.sleep(0.4)

        error = driver.find_element(By.ID, "login-error")
        assert error.text != "", "No error shown for invalid credentials"

        # Clear fields for next test
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()

    def test_03_login_with_valid_credentials(self, driver):
        """Maksym / grisha1337 should log in and show the main app."""
        u = wait_visible(driver, By.ID, "username")
        u.clear()
        u.send_keys(USERNAME)

        p = driver.find_element(By.ID, "password")
        p.clear()
        p.send_keys(PASSWORD)

        driver.find_element(By.ID, "login-btn").click()

        # After login the Cameras tab must be visible
        cameras_tab = wait_visible(driver, By.ID, "tab-cameras")
        assert cameras_tab.is_displayed(), "Login failed — Cameras tab not visible"

    # ── 2. TAB NAVIGATION ─────────────────────────────────────────────
    def test_04_cameras_tab_is_active_after_login(self, driver):
        """Cameras panel is the default active panel after login."""
        cameras_panel = driver.find_element(By.ID, "cameras")
        assert "active" in cameras_panel.get_attribute("class"), \
            "Cameras panel should be active after login"

    def test_05_navigate_to_lenses_tab(self, driver):
        """Click Lenses tab — Lenses panel becomes visible."""
        wait_clickable(driver, By.ID, "tab-lenses").click()
        time.sleep(0.3)

        lenses_panel = driver.find_element(By.ID, "lenses")
        assert "active" in lenses_panel.get_attribute("class"), \
            "Lenses panel not active after clicking Lenses tab"

    def test_06_navigate_to_contact_tab(self, driver):
        """Click Contact tab — Contact panel becomes visible."""
        wait_clickable(driver, By.ID, "tab-contact").click()
        time.sleep(0.3)

        contact_panel = driver.find_element(By.ID, "contact")
        assert "active" in contact_panel.get_attribute("class"), \
            "Contact panel not active after clicking Contact tab"

    def test_07_navigate_back_to_cameras_tab(self, driver):
        """Navigate back to Cameras from Contact — panel switches correctly."""
        wait_clickable(driver, By.ID, "tab-cameras").click()
        time.sleep(0.3)

        cameras_panel = driver.find_element(By.ID, "cameras")
        assert "active" in cameras_panel.get_attribute("class"), \
            "Cameras panel not active after clicking back"

    # ── 3. CONTACT FORM FIELDS ────────────────────────────────────────
    def test_08_contact_form_name_field(self, driver):
        """Name field accepts text input."""
        wait_clickable(driver, By.ID, "tab-contact").click()
        time.sleep(0.3)

        name_field = wait_visible(driver, By.ID, "contact-name")
        name_field.clear()
        name_field.send_keys("Test User")
        assert name_field.get_attribute("value") == "Test User", \
            "Name field did not store input correctly"

    def test_09_contact_form_email_field(self, driver):
        """Email field accepts a valid email address."""
        email_field = wait_visible(driver, By.ID, "contact-email")
        email_field.clear()
        email_field.send_keys("test@example.com")
        assert email_field.get_attribute("value") == "test@example.com", \
            "Email field did not store input correctly"

    def test_10_contact_form_password_field(self, driver):
        """Password field accepts input (type=password)."""
        pwd_field = wait_visible(driver, By.ID, "contact-password")
        pwd_field.clear()
        pwd_field.send_keys("SecurePass123!")
        assert pwd_field.get_attribute("value") == "SecurePass123!", \
            "Password field did not store input correctly"

    # ── 4. SEND MESSAGE BUTTON ────────────────────────────────────────
    def test_11_send_message_shows_success(self, driver):
        """Clicking Send Message (with all fields filled) shows success text."""
        # Fields were filled in previous tests; click Send
        send_btn = wait_clickable(driver, By.ID, "send-btn")
        assert send_btn.is_enabled(), "Send Message button is disabled"
        send_btn.click()
        time.sleep(0.5)

        msg_div = wait_visible(driver, By.ID, "send-message")
        assert "sent" in msg_div.text.lower() or "success" in msg_div.text.lower(), \
            f"Expected success message, got: '{msg_div.text}'"

    def test_12_send_message_error_when_fields_empty(self, driver):
        """Send Message without filling fields shows a validation error."""
        # Wait for auto-reset (3 seconds) then try submitting empty form
        time.sleep(3.5)

        # Navigate away and back to get a fresh empty form
        wait_clickable(driver, By.ID, "tab-cameras").click()
        time.sleep(0.2)
        wait_clickable(driver, By.ID, "tab-contact").click()
        time.sleep(0.3)

        driver.find_element(By.ID, "send-btn").click()
        time.sleep(0.4)

        msg_div = driver.find_element(By.ID, "send-message")
        assert msg_div.text != "", "No validation error shown for empty form"

    # ── 5. LOGOUT ─────────────────────────────────────────────────────
    def test_13_logout_button_is_visible(self, driver):
        """Logout button is visible in the page header."""
        logout_btn = wait_visible(driver, By.ID, "logout-btn")
        assert logout_btn.is_displayed(), "Logout button is not visible"

    def test_14_logout_returns_to_login_screen(self, driver):
        """Clicking Logout hides the app and shows the login form."""
        logout_btn = wait_clickable(driver, By.ID, "logout-btn")
        logout_btn.click()
        time.sleep(0.5)

        username_field = wait_visible(driver, By.ID, "username")
        assert username_field.is_displayed(), \
            "After logout, login form did not reappear"

        login_screen = driver.find_element(By.ID, "login-screen")
        assert login_screen.is_displayed(), "Login screen not visible after logout"
