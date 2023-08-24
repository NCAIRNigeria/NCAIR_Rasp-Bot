#!/bin/bash

# Display welcome message
echo "Setting up NCAIR_Rasp-Bot project..."


# Update and upgrade
sudo apt-get update
sudo apt-get upgrade -y

# Install required packages
sudo apt-get install -y python3-pip python3-dev libatlas-base-dev
sudo apt-get install python3-opencv
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update
sudo apt-get install libedgetpu1-std
sudo apt-get install python3-pycoral

# Install required Python packages from requirements.txt
echo "Installing required Python packages..."
pip3 install -r requirements.txt

# Set up the robot folder as a Python library
cd robot
sudo python3 setup.py install
cd ..

# Display completion message
echo "Setup completed successfully."
