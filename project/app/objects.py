from PyQt6.QtWidgets import (QMainWindow, QLabel, QDoubleSpinBox)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Flight")
window.setGeometry(500, 300, 500, 500)


# parameters
def SetSpinBox(spin_box: QDoubleSpinBox, above: int) -> None:
    spin_box.setRange(-10, 10)
    spin_box.setSingleStep(0.1)
    spin_box.move(65, above)


def SetLable(label: QLabel, text: str, above: int) -> None:
    label.setText(text)
    label.move(20, above)


height_l = QLabel(window)
height_sb = QDoubleSpinBox(window)
angle_l = QLabel(window)
angle_sb = QDoubleSpinBox(window)
size_l = QLabel(window)
size_sb = QDoubleSpinBox(window)
weight_l = QLabel(window)
weight_sb = QDoubleSpinBox(window)
speed_l = QLabel(window)
speed_sb = QDoubleSpinBox(window)

param = {height_l: height_sb, angle_l: angle_sb, size_l: size_sb, weight_l: weight_sb, speed_l: speed_sb}
text = ["height", "angle", "size", "weight", "speed"]
i = 1
for key, value in param.items():
    SetLable(key, text[i - 1], 40 * i)
    SetSpinBox(value, 40 * i)
    i += 1

window.show()
