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
        self.selected_rows = []
        
        #show the window fullscreen
        self.showMaximized()
        
        # show the screen
        self.show()
        
        ################################
        # ELEMENTARY REGISTRATION PAGE #
        ################################
        
        # Back button locaed at Elemetary registration page
        self.ui.button_back_reg_pg_2.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.register_page))
        self.ui.btn_goto_elem_reg.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.elem_reg_page))
        
        # Submit Button located at registration page    
        self.ui.button_submit_data_elem.clicked.connect(self.data_validation_register)
        
        
        ###############################
        #  COLLEGE REGISTRATION PAGE  #
        ###############################
        
        # Back Button located at registration page
        self.ui.button_back_reg_pg.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.front_page))
        
        # Submit Button located at registration page    
        self.ui.button_submit_data.clicked.connect(self.data_validation_register)
        
        
        ################
        #  FRONT PAGE  #
        ################
        
        # Front Page View button
        self.ui.view_button.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.second_page))
        self.ui.view_button.clicked.connect(self.refresh_data)
        
        # Front Page Register button
        self.ui.register_button.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.register_page))
        
        ##########################
        #  DATA MANAGEMENT PAGE  #
        ##########################
        
        # Back Button located at second page
        self.ui.btn_back_second_page.clicked.connect(lambda: self.ui.stackedWidgetfront.setCurrentWidget(self.ui.front_page))
        
        # Left menu toggle button located at second_page (show hide menu panel)
        self.ui.open_close_side_bar_button.clicked.connect(lambda: self.slideLeftMenu())  
        
        # Buttons located at Second page
        self.ui.queue_data.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.mixData))
        self.ui.elementary_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.elementary_data))
        self.ui.college_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.college_data))
        
        # Connect the save_all_data button to the save_data function
        self.ui.btn_save_all_data.clicked.connect(self.save_table_execute)

        # Connect the button's clicked signal to the refresh_btn function
        self.ui.btn_refresh_page.clicked.connect(self.refresh_btn)
        
        # filter
        self.ui.searchLineEdit.textChanged.connect(self.filter_all_data)
        
        # Delete Selected button
        self.ui.btn_delete_selected.clicked.connect(self.delete_selected_row)

    def start_queue_db(self):
        conn = sqlite3.connect('queue.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Queue_Student_Data
            (IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            grade INT,
            Registration TEXT,
            Semester INT,
            Course INT
            )
        '''
        conn.execute(table_create_query)
        cursor = conn.cursor()
        conn.commit()
        sqlquery = "SELECT * FROM Queue_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        self.add_checkbox()
        row_index = 0
        
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()

    def refresh_data(self):
        self.ui.tableWidget.setRowCount(0) #clear the existing data 
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.columnCount()-1)
        self.reset_id_numbers()
        self.load_queue_database()
        self.reset_selection_of_rows()
        self.add_checkbox()

    def refresh_btn(self):
        
        self.refresh_data()
        QMessageBox.information(self, "Info", "Refreshed", QMessageBox.Ok)
        
        



    def reset_id_numbers(self):
        conn = sqlite3.connect('queue.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Queue_Student_Data")
        rows = cursor.fetchall()

        # Start a counter at 1
        counter = 1
        # Iterate through the rows and update the IDnumber
        for row in rows:
            cursor.execute("UPDATE Queue_Student_Data SET IDnumber = ? WHERE IDnumber = ?", (counter, row[0]))
            counter += 1

        conn.commit()

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

    def reset_selection_of_rows(self):
        self.selected_rows = []        

    def add_checkbox(self):
        if "SELECT ROW" not in [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount())]:
            if self.checkbox_column_index is None:
                self.checkbox_column_index = self.ui.tableWidget.columnCount()
            self.ui.tableWidget.insertColumn(self.checkbox_column_index)
            self.ui.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)

            # adding checkbox for every row
            for i in range(self.ui.tableWidget.rowCount()):
                check_box = QtWidgets.QCheckBox()
                self.ui.tableWidget.setCellWidget(i, self.checkbox_column_index, check_box)
                check_box.setStyleSheet("QCheckBox {margin-left: 43px;}")
                check_box.stateChanged.connect(lambda state, row=i: self.on_checkbox_state_changed(state, row))

            # Changing header name
            header_labels = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount()-1)]
            # Insert the new label at the end
            header_labels.append("SELECT ROW")
            self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)
        else:
            pass


    def delete_selected_row(self):
        if self.selected_rows == []:
            QMessageBox.warning(self, "Warning", "There is no selected Data.")
        else:
            result = QMessageBox.question(self, 'Confirm', "Are you sure you want to Delete the selected data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if result == QMessageBox.Yes:
                conn = sqlite3.connect('queue.db')
                with conn:
                    cursor = conn.cursor()
                    for row in self.selected_rows:
                        cursor.execute("DELETE FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                
                QMessageBox.information(self, "Info", "Data Deleted Successfully")
                self.refresh_data()
                
            else:
                # cancel operation
                pass
        
        
    def on_checkbox_state_changed(self, state, row):
        
        if state:
            self.selected_rows.append(row+1)
            print(row+1)
        else:
            self.selected_rows.remove(row+1)
            print(row+1)

    def save_table_execute(self):
        result = QMessageBox.question(self, 'Confirm', "Are you sure you want to Update the data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if result == QMessageBox.Yes:
            # code to update data in database
            connection = sqlite3.connect("queue.db")
            cursor = connection.cursor()

            # Iterate through the rows of the tableWidget
            for i in range(self.ui.tableWidget.rowCount()):
                IDnumber = self.ui.tableWidget.item(i, 0).text()
                firstname = self.ui.tableWidget.item(i, 1).text()
                lastname = self.ui.tableWidget.item(i, 2).text()
                gender = self.ui.tableWidget.item(i, 3).text()
                age = self.ui.tableWidget.item(i, 4).text()
                nationality = self.ui.tableWidget.item(i, 5).text()
                grade = self.ui.tableWidget.item(i, 6).text()
                Registration = self.ui.tableWidget.item(i, 7).text()
                Semester = self.ui.tableWidget.item(i, 8).text()
                Course = self.ui.tableWidget.item(i, 9).text()
                
                try:
                    # Update the corresponding row in the database
                    cursor.execute("UPDATE Queue_Student_Data SET firstname=?, lastname=?, gender=?, age=?, nationality=?, grade=?, Registration=?, Semester=?, Course=? WHERE IDnumber=?", (firstname, lastname, gender, age, nationality, grade, Registration, Semester, Course, IDnumber))
                    connection.commit()
                    
                except Exception as e:
                    QMessageBox.warning(self, "Error", "Error saving data : {}".format(e))
                    print(e)
                    
            QMessageBox.information(self, "Info", "Data Updated Successfully")
        else:
            # cancel operation
            pass
        connection.close()
        self.refresh_data()
        















        # filter data from the table
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


        # Catch Empty data from user inputs
    def data_validation_register(self):
        
        if self.ui.stackedWidgetfront.currentWidget() == self.ui.elem_reg_page:
            if self.ui.checkBox_terms_elem.isChecked():
                # Checking if Firsname and lastname are not empty
                if self.ui.lineEdit_firstname_elem.text() == "" or self.ui.line_Edit_lastname_elem.text() == "":
                    QMessageBox.warning(self, "Warning", "Firstname and Lastname are required.")
                    return
                else:
                    self.enter_data_elementary()
            else:
                QMessageBox.warning(self, "Warning", "Accepting the terms are required.")
                return

        else:
        # self.ui.stackedWidgetfront.currentWidget() == self.ui.register_page:
        
            # Terms and Conditions Checking
            if self.ui.checkBox_terms.isChecked():
                # Checking if Firsname and lastname are not empty
                if self.ui.lineEdit_firstname.text() == "" or self.ui.line_Edit_lastname.text() == "":
                    QMessageBox.warning(self, "Warning", "Firstname and Lastname are required.")
                    return
                else:
                    self.enter_data_college()
            else:
                QMessageBox.warning(self, "Warning", "Accepting the terms are required.")
                return
            
        
    def enter_data_elementary(self):
        first_name = self.ui.lineEdit_firstname_elem.text()
        last_name = self.ui.line_Edit_lastname_elem.text()
        gender = self.ui.cmbbox_gender_elem.currentText()
        age = self.ui.spinBox_age_elem.value()
        nationality = self.ui.cmbbox_nationality_elem.currentText()
        grade_level = self.ui.cmbbox_grade_lvl_elem.currentText()
        
        
        
        if self.ui.checkBox_registered_elem.isChecked():
            register_value = "Registered"
        else:
            register_value = "Unregistered"
            
        conn = sqlite3.connect('queue.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Queue_Student_Data
            (IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            grade INT,
            Registration TEXT,
            Semester INT,
            Course INT
            )
        '''
        conn.execute(table_create_query)
        # Insert Data
        data_insert_query = '''INSERT INTO Queue_Student_Data (firstname, lastname, gender, age, nationality, grade, Registration,Semester,Course) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''' 
        data_insert_tuple =(
                    first_name,
                    last_name,
                    gender,
                    age,
                    nationality,
                    grade_level,
                    register_value,
                    None,
                    None
                )
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        
        self.clear_reg_inputs()
        
        sqlquery = "SELECT * FROM Queue_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget.setRowCount(len(rows))

        self.reset_id_numbers()

        cursor.execute("SELECT MAX(IDnumber) FROM Queue_Student_Data")
        last_id = cursor.fetchone()[0]
        
        if last_id is None:
            row_index = 1
        else:
            row_index = last_id
            
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
            
        conn.close()
        
        QMessageBox.information(self, "Info", "Data inserted successfully")
        
        # Executes and sends data after passing Data Validation function
    def enter_data_college(self):
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
        conn = sqlite3.connect('queue.db')
        table_create_query = '''CREATE TABLE IF NOT EXISTS Queue_Student_Data
            (IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            grade INT,
            Registration TEXT,
            Semester INT,
            Course INT
            )
        '''
        conn.execute(table_create_query)
        # Insert Data
        data_insert_query = '''INSERT INTO Queue_Student_Data (firstname, lastname, gender, age, nationality, grade, Registration,Semester,Course) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''' 
        data_insert_tuple =(
                    first_name,
                    last_name,
                    gender,
                    age,
                    nationality,
                    None,
                    register_value,
                    completed_course,
                    completed_semester
                )
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        
        self.clear_reg_inputs()
        
        sqlquery = "SELECT * FROM Queue_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget.setRowCount(len(rows))

        self.reset_id_numbers()

        cursor.execute("SELECT MAX(IDnumber) FROM Queue_Student_Data")
        last_id = cursor.fetchone()[0]
        
        if last_id is None:
            row_index = 1
        else:
            row_index = last_id
            
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
            
        conn.close()
        
        QMessageBox.information(self, "Info", "Data inserted successfully")

    def clear_reg_inputs(self):
        
        if self.ui.stackedWidgetfront.currentWidget() == self.ui.elem_reg_page:
            lineEdits = [self.ui.lineEdit_firstname_elem, self.ui.line_Edit_lastname_elem]
            for lineEdit in lineEdits:
                lineEdit.clear()
            self.ui.cmbbox_gender_elem.setCurrentIndex(0)
            self.ui.cmbbox_nationality_elem.setCurrentIndex(0)
            self.ui.spinBox_age_elem.setValue(0)
            self.ui.cmbbox_grade_lvl_elem.setCurrentIndex(0)
            self.ui.checkBox_registered_elem.setChecked(False)
            self.ui.checkBox_terms_elem.setChecked(False)
        else:
            # Clearing the last input of a user
            lineEdits = [self.ui.lineEdit_firstname, self.ui.line_Edit_lastname]
            for lineEdit in lineEdits:
                lineEdit.clear()
            self.ui.cmbbox_title.setCurrentIndex(0)
            self.ui.cmbbox_nationality.setCurrentIndex(0)
            self.ui.spinBox_age.setValue(0)
            self.ui.spinBox_course.setValue(0)
            self.ui.spinBox_semester.setValue(0)
            self.ui.checkBox_registered.setChecked(False)
            self.ui.checkBox_terms.setChecked(False)

# App execution context           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program_Window()
    
    window.setWindowTitle("Dominican College")
    
    window.start_queue_db()

    sys.exit(app.exec())