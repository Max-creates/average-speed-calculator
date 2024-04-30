from PyQt6.QtWidgets import QGridLayout, QWidget, QApplication, QLabel, QPushButton, QLineEdit, \
    QComboBox
import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()
        
        label_distance = QLabel("Distance:")
        self.input_distance = QLineEdit()
        
        label_time = QLabel("Time (hours):")
        self.input_time = QLineEdit()
        
        self.combobox_unit = QComboBox()
        self.combobox_unit.addItem("Metric(km)")
        self.combobox_unit.addItem("Imperial(miles)")
        
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        
        self.result_label = QLabel("")
        
        grid.addWidget(label_distance, 0, 0)
        grid.addWidget(self.input_distance, 0, 1)
        grid.addWidget(self.combobox_unit, 0, 2)
        
        grid.addWidget(label_time, 1, 0)
        grid.addWidget(self.input_time, 1, 1)
        
        grid.addWidget(calculate_button, 2, 1)
        
        grid.addWidget(self.result_label, 3, 0, 1, 2)
        
        self.setLayout(grid)
    
    def calculate(self):
        distance = self.input_distance.text()
        time = self.input_time.text()
        selected_unit = self.combobox_unit.currentText()
        speed = float(distance) / float(time)
        if selected_unit == "Metric(km)":
            result = round(speed, 2)
            unit = "km/h"
            
        if selected_unit == "Imperial(miles)":
            result = round(speed * 0.621371, 2)
            unit = "mph"
        
        self.result_label.setText(str(f"Average speed: {result}{unit}"))
            
        

app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
sys.exit(app.exec())