================================================================
  Tech_world — Selenium Test Project
  Student ID: 2420067
================================================================

CONTENTS
--------
  index.html              — Tech_world website (main page)
  script.js               — Site logic (login, tabs, form, logout)
  2420067_py_test.py   — Selenium test suite (14 tests)
  README.txt              — This file


REQUIREMENTS
------------
  - Python 3.x
  - Google Chrome browser
  - ChromeDriver (same version as your Chrome)
  - pytest
  - selenium


INSTALLATION
------------
  1. Install Python libraries:
       pip install pytest selenium

  2. Check your Chrome version:
       Open Chrome → type in address bar: chrome://version
       Example: "Google Chrome 124.0.6367.119"

  3. Download ChromeDriver:
       Go to: https://chromedriver.chromium.org/downloads
       Download the version matching your Chrome.
       Place chromedriver.exe in the same folder as the test file
       OR add it to your system PATH.


SETUP BEFORE RUNNING
--------------------
  Open 2420067_py_test.py and find line ~30:

       BASE_URL = r"file:///C:\Users\maxim\Downloads\selenium_project\index.html"

  Change the path to the actual location of index.html on your computer.

  IMPORTANT: Use the r"..." format (raw string) to avoid errors with
  backslashes on Windows. Example:

       BASE_URL = r"file:///C:\Users\YourName\Desktop\project\index.html"

  Or use forward slashes:

       BASE_URL = "file:///C:/Users/YourName/Desktop/project/index.html"


HOW TO RUN
----------
  Open a terminal (Command Prompt or PowerShell) in the project folder:

       cd C:\Users\YourName\Downloads\selenium_project

  Run all tests:

       pytest st12345678_py_test.py -v

  The -v flag shows each test name and PASSED / FAILED status.


WHAT IS TESTED
--------------
  test_01  Login page loads correctly
  test_02  Error shown for wrong credentials
  test_03  Successful login with admin / @Dm1n
  test_04  Cameras tab is active by default after login
  test_05  Navigation to Lenses tab
  test_06  Navigation to Contact tab
  test_07  Navigation back to Cameras tab
  test_08  Contact form — Name field accepts input
  test_09  Contact form — Email field accepts input
  test_10  Contact form — Password field accepts input
  test_11  Send Message button shows success message
  test_12  Send Message shows error when fields are empty
  test_13  Logout button is visible in the header
  test_14  Logout returns user to the login screen


LOGIN CREDENTIALS
-----------------
  Username : Maksym
  Password : grisha1337                 


EXPECTED OUTPUT (all tests passing)
------------------------------------
  collected 14 items

  st12345678_py_test.py::TestTechWorld::test_01_login_page_loads                PASSED
  st12345678_py_test.py::TestTechWorld::test_02_login_error_on_wrong_credentials PASSED
  st12345678_py_test.py::TestTechWorld::test_03_login_with_valid_credentials     PASSED
  st12345678_py_test.py::TestTechWorld::test_04_cameras_tab_is_active_after_login PASSED
  st12345678_py_test.py::TestTechWorld::test_05_navigate_to_lenses_tab           PASSED
  st12345678_py_test.py::TestTechWorld::test_06_navigate_to_contact_tab          PASSED
  st12345678_py_test.py::TestTechWorld::test_07_navigate_back_to_cameras_tab     PASSED
  st12345678_py_test.py::TestTechWorld::test_08_contact_form_name_field          PASSED
  st12345678_py_test.py::TestTechWorld::test_09_contact_form_email_field         PASSED
  st12345678_py_test.py::TestTechWorld::test_10_contact_form_password_field      PASSED
  st12345678_py_test.py::TestTechWorld::test_11_send_message_shows_success       PASSED
  st12345678_py_test.py::TestTechWorld::test_12_send_message_error_when_empty    PASSED
  st12345678_py_test.py::TestTechWorld::test_13_logout_button_is_visible         PASSED
  st12345678_py_test.py::TestTechWorld::test_14_logout_returns_to_login_screen   PASSED

  14 passed in X.XXs


TROUBLESHOOTING
---------------
  SyntaxError: unicode error
    → Use r"..." for BASE_URL path (see SETUP section above)

  SessionNotCreatedException: ChromeDriver version mismatch
    → Download ChromeDriver that matches your exact Chrome version

  WebDriverException: chromedriver not found
    → Place chromedriver.exe in the project folder or add to PATH

  TimeoutException on a test
    → The selector did not find an element in time.
      Make sure index.html and script.js are in the same folder.


================================================================
  Submitted by: 2420067
  Date: 08.04.2026
================================================================
