```markdown
# 🐢 ROS2 Jazzy | Turtlesim Auto Controller

---

## 📌 Overview
This project demonstrates how to control the **Turtlesim** node automatically using a custom Python node in **ROS2 Jazzy**.  
The turtle will move forward and rotate continuously without manual input.

---

## ✅ Features
- Automated movement control using ROS2 publisher.
- Built on **ROS2 Jazzy** (Ubuntu 24.04).
- Easy to build and run.

---

## 📂 Project Structure
```
ros2_ws/
├── src/
│   └── my_turtle_controller/
│       ├── package.xml
│       ├── setup.py
│       ├── my_turtle_controller/
│       │   └── move_turtle.py
└── README.md
```

---

## 🔧 Requirements
```bash
Ubuntu 24.04
ROS2 Jazzy
Python 3.x
colcon build tools
```

---

## ⚙️ Installation
```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/ros2-turtlesim-auto-controller.git
cd ros2-turtlesim-auto-controller

# Source ROS2
source /opt/ros/jazzy/setup.bash

# Build workspace
colcon build
source install/setup.bash
```

---

## ▶️ Run the Project
### 1. Start Tu
