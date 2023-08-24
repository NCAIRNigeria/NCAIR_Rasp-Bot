# Getting Started with NCAIR Rasp-Bot

Welcome to the NCAIR Rasp-Bot project! This guide will help you get started with setting up your Raspberry Pi-powered autonomous UGV.

## Step 1: Install Raspberry Pi OS

1. Download the Raspberry Pi OS (Bullseye) from the official Raspberry Pi website: [Download Raspberry Pi OS](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit)

2. Follow the installation instructions to flash the OS onto a microSD card.

## Step 2: Assemble the Chassis

1. Locate the 3D model files for the chassis in the `3D` folder of your project repository.

2. You have two options:
   - Print the chassis parts using a 3D printer.
   - Order the chassis parts from an online vendor that provides 3D printing services.

3. Assemble the chassis according to the provided assembly instructions or design.

## Step 3: Connect the Components

1. Refer to the images below for guidance on connecting the components:

   ![Raspberry Pi Connection](images/raspberry_pi_connection.png)
   ![Motor Driver Connection](images/motor_driver_connection.png)
   ![Power Station Schematics](images/power_station_schematics.png)

2. Follow the provided schematics to connect the components, including the Raspberry Pi, motor driver, wheels, and other necessary hardware.

### Raspberry Pi to Motor Driver Connections

For connecting the Raspberry Pi to the motor driver module, use the following GPIO pin assignments:

- M1a (Motor 1, Positive Terminal): GPIO Pin 11
- M1b (Motor 1, Negative Terminal): GPIO Pin 12
- M2a (Motor 2, Positive Terminal): GPIO Pin 15
- M2b (Motor 2, Negative Terminal): GPIO Pin 16

These connections allow the Raspberry Pi to control the direction and speed of the motors using the motor driver.

## Step 4: Install Dependencies

1. Set up your Raspberry Pi and connect it to the internet.

2. Clone your `NCAIR_Rasp-Bot` repository to the Raspberry Pi.
    ```bash
    git clone https://github.com/NCAIRNigeria/NCAIR_Rasp-Bot.git
    ```

3. Navigate to the `NCAIR_Rasp-Bot` folder, the repository base folder.

4. Run the setup script to install the required dependencies and set up the `setup.sh` script:

   ```bash
   cd robot
   sudo python3 setup.py install
   ```

Congratulations! You've successfully set up your NCAIR Rasp-Bot. Feel free to explore other modes like `basic_motion`, `collision_avoidance`, `object_following`, and `road_following` in the documentation to make the most out of your Rasp-Bot.
