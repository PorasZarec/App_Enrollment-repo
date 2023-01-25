from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QAbstractItemView
from PySide6 import QtWidgets, QtCore 
from ui_main_window import Ui_MainWindow

import sqlite3
import sys 

class Program_Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.checkbox_column_index = None
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
        
        
        
        # self.ui.view_button.clicked.connect(self.load_queue_database)
        
        
        
        # Front Page Register button
        self.ui.register_button.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.register_page))

        
        # Submit Button located at registration page    
        self.ui.button_submit_data.clicked.connect(self.data_validation_register)
        
        
        # Buttons located at Second page
        self.ui.queue_data.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.mixData))
        self.ui.elementary_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.elementary_data))
        self.ui.college_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.college_data))
        
        # Connect the save_all_data button to the save_data function
        self.ui.btn_save_all_data.clicked.connect(self.save_table_execute)
        
        # Delete Selected button
        self.ui.btn_delete_selected.clicked.connect(self.delete_selected_execute)
        
        
        # Connect the button's clicked signal to the refresh_btn function
        self.ui.btn_refresh_page.clicked.connect(self.refresh_btn)

        self.ui.searchLineEdit.textChanged.connect(self.filter_all_data)
        
        
    def delete_selected_execute(self):
        
        try:
            QMessageBox.information(self, "Info", "Under Maintenance")
            
        except Exception as e:
            QMessageBox.warning(self, "Error", "Error deleting data : {}".format(e))
            print(e)
        
        # Checking if changes are made from the GUI tableWidget
    def save_table_execute(self):
        try:
            
            QMessageBox.information(self, "Info", "Under Maintenance")
            
        except Exception as e:
            QMessageBox.warning(self, "Error", "Error saving data : {}".format(e))
            print(e)
            
        # # Connect to the database
        # connection = sqlite3.connect("queue.db")
        # cursor = connection.cursor()
        
        # # Iterate through the rows and columns of the tableWidget and update the database
        # for i in range(self.ui.tableWidget.rowCount()):
            
        #     # Get the values from the tableWidget
        #     values = [self.ui.tableWidget.item(i, j).text() for j in range(self.ui.tableWidget.columnCount()-1)]
            
        #     # Update the corresponding row in the database
        # try:
        #     cursor.execute("UPDATE Queue_Student_Data SET firstname=?, lastname=?, gender=?, age=?, nationality=?, Registration=?, Semester=?, Course=?", values)
            
        #     connection.commit()
                
        # Close the connection to the database
        # connection.close()


    def start_queue_db(self):
        
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
        
        self.add_checkbox()

        #itterate to all data inside the database
        row_index = 0
        
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()


    def refresh_btn(self):
        self.ui.tableWidget.setRowCount(0) #clear the existing data 
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.columnCount()-1)
        self.load_queue_database()
        self.add_checkbox()

    
    def add_checkbox(self):
        
        if "SELECT ROW" not in [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount())]:
            if self.checkbox_column_index is None:
                self.checkbox_column_index = self.ui.tableWidget.columnCount()
            self.ui.tableWidget.insertColumn(self.checkbox_column_index)
            self.ui.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)

            # Add checkbox to the inserted column for each row
            for i in range(self.ui.tableWidget.rowCount()):
                check_box = QtWidgets.QCheckBox()
                self.ui.tableWidget.setCellWidget(i, self.checkbox_column_index, check_box)
                check_box.setStyleSheet("QCheckBox {margin-left: 43px;}")
                check_box.stateChanged.connect(lambda state, row=i: self.on_checkbox_state_changed(state, row))

            # Get the current header labels
            header_labels = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount()-1)]
            # Insert the new label at the end
            header_labels.append("SELECT ROW")
            # Set the new header labels
            self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)

        else:
            pass


    def load_queue_database(self):

        conn = sqlite3.connect('queue.db')
        cursor = conn.cursor()
        sqlquery = "SELECT * FROM Queue_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()

        self.ui.tableWidget.setRowCount(len(rows))
        
        row_index = 0
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()




    
        # Filter Data from table view
    def filter_all_data(self):
        search_text = self.ui.searchLineEdit.text().lower()
        for i in range(self.ui.tableWidget.rowCount()):
            match = False
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget.setRowHidden(i, not match)
     
     
     
     
            
    def on_checkbox_state_changed(self, state, row):
        row = row + 1
        if state == QtCore.Qt.Checked:
            # Select the corresponding row
            self.ui.tableWidget.selectRow(row)
            print(f"Selected {row}")
            
        else:
            # Deselect the corresponding row
            self.ui.tableWidget.setRangeSelected(QtWidgets.QTableWidgetSelectionRange(row,0,row,self.ui.tableWidget.columnCount()-1), False)
            print(f"deselected {row}")

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

        # Catch errors from user inputs
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
        
        # Executes and sends data after passing Data Validation function
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
    
    window.start_queue_db()

    sys.exit(app.exec())