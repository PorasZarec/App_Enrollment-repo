from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6 import QtWidgets
from ui_dummy_main_window import Ui_MainWindow

import sqlite3
import sys 

class Program_Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #show the window fullscreen
        self.showMaximized()
        # show the screen
        self.show()
        
        # Back Button located at registration page
        self.ui.button_back_reg_pg.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.front_page))
         # Back Button located at second page
        self.ui.back_button_.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.front_page))
        
        # Left menu toggle button located at second_page (show hide menu panel)
        self.ui.open_close_side_bar_button.clicked.connect(lambda: self.slideLeftMenu())    

        
        # Front Page View button
        self.ui.view_button.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.second_page))
        # Front Page Register button
        self.ui.register_button.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.register_page))

        
        # Submit Button located at registration page    
        self.ui.button_submit_data.clicked.connect(self.data_validation_register)
        
        
        # Buttons located at Second page
        self.ui.queue_data.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.mixData))
        self.ui.elementary_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.elementary_data))
        self.ui.college_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.college_data))
        
        # Connect the save_all_data button to the save_data function
        self.ui.btn_save_all_data.clicked.connect(self.save_queueDatabase_data)

    def data_validation_register(self):
        
        # Terms and Conditions Checking
        if self.ui.checkBox_terms.isChecked():
            
            # Checking if Firsname and lastname are not empty
            if self.ui.lineEdit_firstname.text() == "" or self.ui.line_Edit_lastname.text() == "":
                QMessageBox.warning(self, "Warning", "Firstname and Lastname are required.")
                return
            else:
                self.enter_data()
        else:
            QMessageBox.warning(self, "Warning", "Accepting the terms are required.")
            return
        
    def save_queueDatabase_data(self):
        # Connect to the database
        connection = sqlite3.connect("queue.db")
        cursor = connection.cursor()
        
        # Iterate through the rows and columns of the tableWidget and update the database
        for i in range(self.ui.tableWidget.rowCount()):
            # Get the values from the tableWidget
            values = [self.ui.tableWidget.item(i, j).text() for j in range(self.ui.tableWidget.columnCount())]
            
            # Update the corresponding row in the database
            try:
                cursor.execute("UPDATE Student_Data SET firstname=?, lastname=?, gender=?, age=?, nationality=?, Registration=?, Semester=?, Course=?", values)
                
            # Commit the changes to the database
                connection.commit()
                QMessageBox.information(self, "Info", "Data saved successfully")
                
            except Exception as e:
                QMessageBox.warning(self, "Error", "Error saving data : {}".format(e))
                print(e)

                
        # Close the connection to the database
        connection.close()

        #Load different table from the database
    def load_queue_database(self):
        
        self.ui.searchLineEdit.textChanged.connect(self.filter_all_data)
        
        conn = sqlite3.connect('queue.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Queue_Student_Data
            (firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            Registration TEXT,
            Semester INT,
            Course INT)
        '''
        conn.execute(table_create_query)
        
        cursor = conn.cursor()
        conn.commit()
        
        sqlquery = "SELECT * FROM Queue_Student_Data"
        
        rows = cursor.execute(sqlquery).fetchall()
        
        
        self.ui.tableWidget.setRowCount(len(rows))
        
        #itterate to all data inside the database
        row_index = 0
        
        for row in rows:
            
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()
        
        # filter out different data from different data tables
    def filter_all_data(self):
        search_text = self.ui.searchLineEdit.text().lower()
        for i in range(self.ui.tableWidget.rowCount()):
            match = False
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if search_text in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget.setRowHidden(i, not match)                      
      
      
    # Slide left menu function second page
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_menu_cont_frame.width()
        
        # If minimized 
        if width == 60:
            # Expand menu
            newWidth = 220
            self.ui.left_menu_cont_frame.setMinimumSize(newWidth,0)
        
        # If maximized
        else:
            # Restore menu
            newWidth = 60
            self.ui.left_menu_cont_frame.setMinimumSize(newWidth,0)

    def enter_data(self):
        
        # Gathering all data from user inputs
        first_name = self.ui.lineEdit_firstname.text()
        last_name = self.ui.line_Edit_lastname.text()
        gender = self.ui.cmbbox_title.currentText()
        age = self.ui.spinBox_age.value()
        nationality = self.ui.cmbbox_nationality.currentText()
        completed_course = self.ui.spinBox_course.value()
        completed_semester = self.ui.spinBox_semester.value()
        
        
        if self.ui.checkBox_registered.isChecked():
            register_value = "Registered"
        else:
            register_value = "Unregistered"
            
            
        # Create SQL Table
        
        conn = sqlite3.connect('queue.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Queue_Student_Data
            (firstname TEXT, lastname TEXT, gender TEXT, age INT, nationality TEXT,
            Registration TEXT, Semester INT, Course INT)
        '''
        conn.execute(table_create_query)
        
        # Insert Data
        
        data_insert_query = '''INSERT INTO Queue_Student_Data (firstname, lastname, gender,
        age, nationality, Registration,Semester,Course) VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)''' 
        
        data_insert_tuple =(
            first_name,
            last_name,
            gender,
            age,
            nationality,
            register_value,
            completed_course,
            completed_semester
        )
        
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        
        
        
        # Clearing the last input of a user
        lineEdits = [self.ui.lineEdit_firstname, self.ui.line_Edit_lastname, self.ui.cmbbox_nationality]
        
        for lineEdit in lineEdits:
            lineEdit.clear()
            

        self.ui.cmbbox_title.setCurrentIndex(0)
        self.ui.cmbbox_nationality.setCurrentIndex(0)
        
        
        self.ui.spinBox_age.setValue(0)
        self.ui.spinBox_course.setValue(0)
        self.ui.spinBox_semester.setValue(0)
        
        
        self.ui.checkBox_registered.setChecked(False)
        self.ui.checkBox_terms.setChecked(False)
        
        sqlquery = "SELECT * FROM Queue_Student_Data"
        
        rows = cursor.execute(sqlquery).fetchall()
        
        
        self.ui.tableWidget.setRowCount(len(rows))
        
        #itterate to all data inside the database
        row_index = 0
        
        for row in rows:
            
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()
        
        QMessageBox.information(self, "Info", "Data inserted successfully")
 
      
# App execution context           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program_Window()
    
    window.setWindowTitle("Dominican College")
    window.load_queue_database()
    window.save_queueDatabase_data()
    sys.exit(app.exec())