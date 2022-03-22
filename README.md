# BlenderKit tests
Behavior driven E3E tests for BlenderKit web written in Python 3.9 and Cucumber.
Using Behave and Selenium modules with support for Podman/Docker.
Currently supporting Chrome and headless Chrome browsers.
You can run the tests locally on your machine or in a container.

## Local testing
### Installing
1. Create virtual environment and install dependencies.
```
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

2. Make sure you have Chrome browser installed.

### Setup testing account
Copy and rename file `env-example.sh` to `env.sh` and make it executable:
```
cp env-example.sh env.sh
chmod 755 env.sh
```

Fill in email address and password for testing account in the file `env.sh`.
`env.sh` file will then look like this:
```
export BK_USERNAME="set username of test account here"
export BK_PASSWORD="set password of test account here"
export PP_USERNAME="set paypal sandbox username of test account here"
export PP_PASSWORD="set paypal sandbox password of test account here"
source venv/bin/activate
```

If you have different usernames/passwords on staging or production server, you can overwrite default variables by setting up variables ending _STAGE or _PROD, for example:

export BK_USERNAME_PROD="production username overwrites BK_USERNAME for production tests"
export BK_USERNAME_STAGE="stage username overwrites BK_USERNAME for stage tests"

### Running the tests locally
```
# Source env.sh - this exports username/password and activates virtual environment
source env.sh

# Run the tests
behave
```

### Checking the results
Test progress and results are printed to the terminal.
Screenshot is taken after each test step.
These screenshots are available in directory `screenshots`.

## Testing in container
### Building the container
```
buildah build --tag bk-tests
```

### Running the tests
```
./container.sh
```

### Checking the results
Test progress is printed to the console.
Screenshots are copied to the local directory `screenshots-container` once all the tests are finished.

## Developing the tests
TBD

### Debugging the tests
Outputs of `print()` functions are normally deleted by Behave.
To overcome this problem run in plain format without capture:
```
behave --no-capture --format plain
```
