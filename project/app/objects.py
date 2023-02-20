from PyQt6.QtWidgets import (QMainWindow, QLabel, QDoubleSpinBox, QPushButton, QTableWidget)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Flight")
window.setGeometry(350, 300, 270, 400)


# parameters
def SetSpinBox(spin_box: QDoubleSpinBox, above: int) -> None:
    spin_box.setRange(0, 1000)
    spin_box.setSingleStep(0.01)
    spin_box.move(65, above)


def SetLable(label: QLabel, text: str, above: int, left: int = 20) -> None:
    label.setText(text)
    label.move(left, above)


height_l = QLabel(window)
height_sb = QDoubleSpinBox(window)
height_sb.setValue(10)

angle_l = QLabel(window)
angle_sb = QDoubleSpinBox(window)
angle_sb.setValue(45)

size_l = QLabel(window)
size_sb = QDoubleSpinBox(window)
size_sb.setValue(0.1)

weight_l = QLabel(window)
weight_sb = QDoubleSpinBox(window)
weight_sb.setValue(1)

speed_l = QLabel(window)
speed_sb = QDoubleSpinBox(window)
speed_sb.setValue(10)

step_l = QLabel(window)
step_sb = QDoubleSpinBox(window)
step_sb.setValue(0.01)

param = {height_l: height_sb, angle_l: angle_sb, size_l: size_sb, weight_l: weight_sb, speed_l: speed_sb,
         step_l: step_sb}
text = ["height", "angle", "size", "weight", "speed", "step"]
i = 1
for key, value in param.items():
    SetLable(key, text[i - 1], 40 * i)
    SetSpinBox(value, 40 * i)
    i += 1

# buttons
launch_btn = QPushButton(window)
launch_btn.move(20, 300)
launch_btn.setText("Launch")

clear_btn = QPushButton(window)
clear_btn.move(20, 340)
clear_btn.setText("Clear the table")

# result table
table = QTableWidget()
table.setWindowTitle("Simulation: Flight - RESULTS")
table.setGeometry(1300, 300, 400, 400)

table.setColumnCount(4)
table.setHorizontalHeaderLabels(["Time step", "Distance", "Max height", "End speed"])

window.show()
table.show()
