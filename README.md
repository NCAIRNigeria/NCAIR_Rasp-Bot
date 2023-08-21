# Raspbot: Raspberry Pi-Powered Autonomous UGV

Turn your Raspberry Pi into a powerful Autonomous Unmanned Ground Vehicle (UGV) with the Raspbot project. Explore various autonomous modes to control your robot's movement and behavior.

## Modes

- **Basic Motion**: Control the robot's basic movement commands such as forward, backward, left, and right.
- **Collision Avoidance**: Navigate the robot to avoid obstacles and collisions using real-time image classification.
- **Object Following**: Teach your robot to follow a specific object using image recognition.
- **Road Following**: Implement road-following capabilities to guide the robot along a path.
- **Teleoperation**: Control the robot remotely using keyboard or joystick inputs.

## Setup

1. Clone this repository to your Raspberry Pi.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Connect the robot's motors, sensors, and any additional hardware components. 

## Usage

1. Navigate to the desired mode's directory.
2. Run the corresponding script.
3. Follow the on-screen instructions to observe autonomous behavior in the selected mode.

## Dependencies

- TensorFlow Lite
- Coral Edge TPU library
- OpenCV
- RPi.GPIO
- Motor Driver

## Contributing

Contributions are welcome! If you'd like to add new modes, features, fix bugs, or improve the documentation, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, you can reach out to [handanfoun@gmail.com](nathaniel-handan.me) or open an issue in the repository.

