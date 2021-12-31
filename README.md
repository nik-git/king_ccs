# Matching Candies Challenge
### Recording link
Please download the demo video which shows the working automation

https://drive.google.com/file/d/1QdMfOtOo6FnsR7Ml-qHk9aGV-Gm6l--m/view?usp=sharing

### matching_candies.py
This is the Python script file which has the complete automation code for the challenge.

### How to run as Pytest
Run below command to test the steps as Pytest test case. This will work for two devices / brands.
#### pytest test_ccs.py --brand Samsung
Download conftest.py and test_ccs.py

### Setup
1. Create a Windows VM with 8 GB RAM and 4 core CPU.
2. Install Java 1.8
3. Install Appium Studio. 
4. Install Appium desktop server.
5. Put Android mobile phone in debugging mode and developer mode.
6. Connect android mobile to VM through USB.
7. Start adb server : adb start-server
8. Start Appium desktop server GUI.
9. From Pycharm run : matching_candies.py
10. Automation will be executed on connected mobile device.

### How to create Appium automation setup on Windows VM on Google Cloud Platform
  1. Create a Free account on GCP by providing details of your Debit card. Only Rs. 2.0 will be deducted for verification.
  2. Generally it is not allowed you to run Andriod Emulators on a VM. Use the link below to create a VM on GCP that will allow to run Android Emulators.
      https://cloud.google.com/community/tutorials/setting-up-an-android-development-environment-on-compute-engine
  3. Follow the steps given in the Setup section above to install all the required softwares.
  4. Create an Android Emulator in Android Studio using AVD Manager.


