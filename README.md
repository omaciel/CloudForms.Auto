This is the automation testing framework for CloudForms, including SystemEngine, CloudEngine and upstream projects Katello, Aeolus and Headpin:  

* [Aeolus](http://aeolusproject.org/)
* [Katello](http://katello.org) Note: Headpin is a lite version of Katello

This test framework was originally written for Katello and headpin, and extended by the Red Hat CloudForms QE Integration team. Tests use Mozilla's [pytest-mozwebqa plugin](https://github.com/davehunt/pytest-mozwebqa).

## Documentation
Documentation is [hosted here](http://eanxgeek.github.com/katello_challenge/index.html). It is out of date.

## Dependencies and Installation
* selenium webdriver or selenium server
* pytest==2.2.3
* pytest-xdist==1.6
* pytest-mozwebqa==0.7.1
* unittestzero

1. Clone this project and install dependencies. Dependencies may be installed by running `pip-python install -r ./requirements.txt` from the root of the project.
2. Verify `data/large_dataset.py` is pointed to correct system templates.
3. Update `data/private_data.template` file with private provider account details. Add base64 encoded passwords to `data/private_data.ini` for aeolus and katello projects. You can use `scripts/generate_password.py` to encode passwords.
4. Rename `data/private_data.template` to `data/private_data.ini` and add `data/private_data.template` to `.gitignore` file
5. Update `tests/aeolus2/pytest.ini` with correct args for your environment.
6. Run tests: `py.test tests/aeolus2`.
7. Monitor log: `tail -f cloudforms_test.log`.

## Requirements
The end-to-end test run assumes a fresh default install of the product(s) that are accessible from the machine running the tests. Aeolus tests assume a configserver is running and credentials are included in `data/private_data.ini`.

## Executing Tests
There are two ways to run Selenium tests.

1. Use the Selenium WebDriver. Executing the tests with argument `--driver=firefox` allows for simple test runs. This is the method most commonly used during development.
2. Use the Selenium Server. Running a standalone Selenium Server supports test distribution on multiple hosts.

To start the Selenium Server for local testing:
`java -jar /path/to/your/selenium/selenium-X.Y.jar \`
`-firefoxProfileTemplate /path/to/ff_profile/.mozilla/firefox/[profile]/`

See [Selenium documentation](http://seleniumhq.org/docs/03_webdriver.html) for more details.

### Basic Usage
`py.test --driver=firefox --baseurl=https://<FQDN>/conductor|katello --project=[project] -q testdir/path/my_test_file.py`

To reduce command line arguments include a `pytest.ini` file in the test directory. See example `tests/aeolus2/pytest.ini`.

### Options
* `--driver=firefox` Allows tests to be run without a separate Selenium server running.
* `--baseurl=...` FQDN of product under test. Include `/conductor` or `/katello`
* `--project=katello|aeolus|katello.cfse|aeolus.cfce` Specify project under test.
* `-q path/to/test_file.py` Point to dir to run all tests in dir, or single file
* `-k [test_keyword]` Test keyword to run specific tests.
* `-m <marker>` For running tests tagged with py.test markers.

Run `py.test -h` for help or refer to [py.test documentation](http://pytest.org/) for complete documentation.

## About the Files
`tests/` Test code goes here. These are typically simple calls to the more complex operations in `apps/`. Update pytest.ini file to simplify test runs.

`apps/`:
* `__init__.py` Provides base objects for use inherited projects and convenience methods to initialize projects.  Setup methods to use throughout the page objects. By inheritance these methods are accessible in other page objects. It is important not to include locators or site specific functions in this file.  The functions in this file are common across our projects and don't change often.

* `locators.py` Base locator object inherited by project-specific locators.  It's rare to have locators that work across applications.  However, if any exist they'll live here.

* `[project]/__init__.py` Project specific handlers.

* `[project]/locators.py` Project specific locators.

`pages/` Deprecated.  The pages/ heirarchy exists for historic purposes.  The apps/ heirarchy is intended to replace the need for pages.

`api/` API helper methods.

* `[project]/api.py` Project-specific API helper methods.

`data/`:
* `large_dataset.py` Dataset that drives the data-driven testing performed.

* `private_data.ini` Credentials file for users, EC2 provider and configserver. Update before running provider tests.

* `manifests/` Content provider manifest.zip files.

### Configuration
* `credentials.yaml` Not currently in use. Update `data/private_data.ini` instead.

* `conftest.py` Specify custom command-line options.

* `mozwebqa.cfg` The mozwebqa plugin will read the parameters in this file and automatically add them onto the py.test command line. It is handy for parameters that are constant like --browsername=firefox.

* `requirements.txt` Lists required packages. Running `sudo pip install -r requirements.txt` (Mac/Linux) will automatically download and install the packages in this file. We recommend 'pinning' the packages to a specific version, for example pytest==2.1.3. This decreases the chance that a change to py.test will affect your test suite.

* `sauce_labs.yaml` username, password, api-key for Saucelabs testing.

