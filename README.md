# harbinger-v2023.01

STEP 1 - open terminal

STEP 2 - run: pip3 install python-owasp-zap-v2.4

STEP 3 - copy this repository to your device: https://github.com/zaproxy/zap-api-python.git

STEP 4 - go the location of this repository and run: python3 setup.py build

STEP 5 - once the build is ready run: python3 setup.py install

DO STEPS 3 to 5 with this repository also:
https://github.com/Grunny/zap-cli.git

AFTER THIS ALL THE NECESSARY DEPENDENCIES AND LIBRARIES WILL BE INSTALLED

STEP 6 - Start the OWASP ZAP GUI Client and dont close it till the end of the session (ZAP daemon can also be used)

STEP 7 - If using the GUI Client, Disable the API key from Tools > Options > API > Disable API Key

STEP 8 - Open another terminal and navigate to the location of the code and run: python3 webscanner.py


NOTE: 
opening code in pycharm might show error with importing the module 'zapv2'
ignore this error and run the code via terminal
