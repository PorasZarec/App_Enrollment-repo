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
        
        
        
        
        self.ui.BSIT_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.BSIT_table_data))
        
        
        self.ui.COMSCI_page_button.clicked.connect(lambda: self.ui.main_body_stackedWidget.setCurrentWidget(self.ui.COMSCI_table_data))
        
        # Approve buttons
        self.ui.btn_approve_BSIT.clicked.connect(lambda: self.approve_to_BSIT_db())
        
        self.ui.btn_approve_COMSCI.clicked.connect(lambda: self.approve_to_COMSCI_db())
        
        
        
        # Connect the save_all_data button to the save_data function
        self.ui.btn_save_all_data.clicked.connect(self.save_Mixtable_execute)

        # Connect the button's clicked signal to the refresh_btn function
        self.ui.btn_refresh_page.clicked.connect(self.refresh_btn)
        
        # filter
        self.ui.searchLineEdit.textChanged.connect(self.filter_all_data)
        
        self.ui.searchLineEdit_BSIT.textChanged.connect(self.filter_BSIT_data)
        
        self.ui.searchLineEdit_COMSCI.textChanged.connect(self.filter_COMSCI_data)
        
        
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
        
        ## Creating for BSIT SQL TABLE
        table_create_query = '''CREATE TABLE IF NOT EXISTS BSIT_Student_Data
            (IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            Registration TEXT,
            Semester INT,
            Course INT
            )
        '''
        conn.execute(table_create_query)
        cursor = conn.cursor()
        conn.commit()
        sqlquery = "SELECT * FROM BSIT_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget_BSIT.setRowCount(len(rows))
        
        self.add_checkbox_BSIT()
       
        # Ittearte through, to add the corresponding data
        row_index = 0
        
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget_BSIT.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        
        ## Creating for COMSCI SQL TABLE
        table_create_query = '''CREATE TABLE IF NOT EXISTS COMSCI_Student_Data
            (IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT,
            lastname TEXT,
            gender TEXT,
            age INT,
            nationality TEXT,
            Registration TEXT,
            Semester INT,
            Course INT
            )
        '''
        conn.execute(table_create_query)
        cursor = conn.cursor()
        conn.commit()
        sqlquery = "SELECT * FROM COMSCI_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget_COMSCI.setRowCount(len(rows))
        
        self.add_checkbox_COMSCI()
       
        # Ittearte through, to add the corresponding data
        row_index = 0
        
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget_COMSCI.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()


    def refresh_data(self):
        
        self.ui.tableWidget.setRowCount(0) #clear the existing data 
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.removeColumn(self.ui.tableWidget.columnCount()-1)
        
        self.ui.tableWidget_BSIT.setRowCount(0) #clear the existing data 
        self.ui.tableWidget_BSIT.clearContents()
        self.ui.tableWidget_BSIT.removeColumn(self.ui.tableWidget_BSIT.columnCount()-1)
        
        self.ui.tableWidget_COMSCI.setRowCount(0) #clear the existing data 
        self.ui.tableWidget_COMSCI.clearContents()
        self.ui.tableWidget_COMSCI.removeColumn(self.ui.tableWidget_COMSCI.columnCount()-1)
        
        self.reset_id_numbers()
        self.load_queue_database()
        self.reset_selection_of_rows()
        self.add_checkbox_COMSCI()
        self.add_checkbox_BSIT()
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
        
        cursor.execute("SELECT * FROM BSIT_Student_Data")
        rows = cursor.fetchall()

        # Start a counter at 1
        counter = 1
        # Iterate through the rows and update the IDnumber
        for row in rows:
            cursor.execute("UPDATE BSIT_Student_Data SET IDnumber = ? WHERE IDnumber = ?", (counter, row[0]))
            counter += 1

        conn.commit()
        
        cursor.execute("SELECT * FROM BSIT_Student_Data")
        rows = cursor.fetchall()

        # Start a counter at 1
        counter = 1
        # Iterate through the rows and update the IDnumber
        for row in rows:
            cursor.execute("UPDATE COMSCI_Student_Data SET IDnumber = ? WHERE IDnumber = ?", (counter, row[0]))
            counter += 1

        conn.commit()
        
        conn.close()

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
        
        conn = sqlite3.connect('queue.db')
        cursor = conn.cursor()
        sqlquery = "SELECT * FROM BSIT_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget_BSIT.setRowCount(len(rows))
        row_index = 0
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget_BSIT.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
            
        conn = sqlite3.connect('queue.db')
        cursor = conn.cursor()
        sqlquery = "SELECT * FROM COMSCI_Student_Data"
        rows = cursor.execute(sqlquery).fetchall()
        self.ui.tableWidget_COMSCI.setRowCount(len(rows))
        row_index = 0
        for row in rows:
            for col, data in enumerate(row):
                self.ui.tableWidget_COMSCI.setItem(row_index, col, QtWidgets.QTableWidgetItem(str(data)))
            row_index += 1
        conn.close()


    def reset_selection_of_rows(self):
        self.selected_rows = []        



    def add_checkbox_BSIT(self):
        
        if "SELECT ROW" not in [self.ui.tableWidget_BSIT.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget_BSIT.columnCount())]:
            if self.checkbox_column_index is None:
                self.checkbox_column_index = self.ui.tableWidget_BSIT.columnCount()
                
            self.ui.tableWidget_BSIT.insertColumn(self.checkbox_column_index)
            self.ui.tableWidget_BSIT.setSelectionMode(QAbstractItemView.MultiSelection)
            # print(self.ui.tableWidget_BSIT.rowCount())
            
            for i in range(self.ui.tableWidget_BSIT.rowCount()):
                check_box = QtWidgets.QCheckBox()
                self.ui.tableWidget_BSIT.setCellWidget(i, self.ui.tableWidget_BSIT.columnCount()-1, check_box)
                check_box.setStyleSheet("QCheckBox {margin-left: 43px;}")
                check_box.stateChanged.connect(lambda state, row=i: self.on_checkbox_state_changed(state, row))

            # Changing header name
            header_labels = [self.ui.tableWidget_BSIT.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget_BSIT.columnCount()-1)]
            # Insert the new label at the correct position
            header_labels.insert(self.checkbox_column_index, "SELECT ROW")
            self.ui.tableWidget_BSIT.setHorizontalHeaderLabels(header_labels)
        else:
            pass

    def add_checkbox(self):
        
        if "SELECT ROW" not in [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount())]:
            if self.checkbox_column_index is None:
                self.checkbox_column_index = self.ui.tableWidget.columnCount()
            self.ui.tableWidget.insertColumn(self.checkbox_column_index)
            self.ui.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)

            # adding checkbox for every row
            for i in range(self.ui.tableWidget.rowCount()):
                check_box = QtWidgets.QCheckBox()
                self.ui.tableWidget.setCellWidget(i, self.ui.tableWidget.columnCount()-1, check_box)
                # self.ui.tableWidget.setCellWidget(i, self.checkbox_column_index, check_box)
                check_box.setStyleSheet("QCheckBox {margin-left: 43px;}")
                check_box.stateChanged.connect(lambda state, row=i: self.on_checkbox_state_changed(state, row))

            # Changing header name
            header_labels = [self.ui.tableWidget.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget.columnCount()-1)]
            # Insert the new label at the end
            header_labels.append("SELECT ROW")
            self.ui.tableWidget.setHorizontalHeaderLabels(header_labels)
        else:
            pass
        
    def add_checkbox_COMSCI(self):
        
        if "SELECT ROW" not in [self.ui.tableWidget_COMSCI.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget_COMSCI.columnCount())]:
            if self.checkbox_column_index is None:
                self.checkbox_column_index = self.ui.tableWidget_COMSCI.columnCount()
            self.ui.tableWidget_COMSCI.insertColumn(self.checkbox_column_index)
            self.ui.tableWidget_COMSCI.setSelectionMode(QAbstractItemView.MultiSelection)

            # adding checkbox for every row
            for i in range(self.ui.tableWidget_COMSCI.rowCount()):
                check_box = QtWidgets.QCheckBox()
                self.ui.tableWidget_COMSCI.setCellWidget(i, self.ui.tableWidget_COMSCI.columnCount()-1, check_box)
                # self.ui.tableWidget.setCellWidget(i, self.checkbox_column_index, check_box)
                check_box.setStyleSheet("QCheckBox {margin-left: 43px;}")
                check_box.stateChanged.connect(lambda state, row=i: self.on_checkbox_state_changed(state, row))

            # Changing header name
            header_labels = [self.ui.tableWidget_COMSCI.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget_COMSCI.columnCount()-1)]
            # Insert the new label at the end
            header_labels.append("SELECT ROW")
            self.ui.tableWidget_COMSCI.setHorizontalHeaderLabels(header_labels)
        else:
            pass
        


    def delete_selected_row(self):
        if self.selected_rows == []:
            QMessageBox.warning(self, "Warning", "There is no selected Data.")
        else:
            result = QMessageBox.question(self, 'Confirm', "Are you sure you want to Delete the selected data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if result == QMessageBox.Yes:
                
                
                if self.ui.main_body_stackedWidget.currentWidget() == self.ui.mixData:
                    
                    conn = sqlite3.connect('queue.db')
                    with conn:
                        cursor = conn.cursor()
                        for row in self.selected_rows:
                            cursor.execute("DELETE FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                    conn.close()
                    self.refresh_data()
                    QMessageBox.information(self, "Info", "Data Deleted Successfully")
                    
                    
                    
                elif self.ui.main_body_stackedWidget.currentWidget() == self.ui.BSIT_table_data:
                    conn = sqlite3.connect('queue.db')
                    with conn:
                        cursor = conn.cursor()
                        for row in self.selected_rows:
                            cursor.execute("DELETE FROM BSIT_Student_Data WHERE IDnumber = ?", (row,))
                    conn.close()
                    self.refresh_data()
                    QMessageBox.information(self, "Info", "Data Deleted Successfully")
                    
                    
                elif self.ui.main_body_stackedWidget.currentWidget() == self.ui.COMSCI_table_data:
                    conn = sqlite3.connect('queue.db')
                    with conn:
                        cursor = conn.cursor()
                        for row in self.selected_rows:
                            cursor.execute("DELETE FROM COMSCI_Student_Data WHERE IDnumber = ?", (row,))
                    conn.close()
                    self.refresh_data()
                    QMessageBox.information(self, "Info", "Data Deleted Successfully")
                    
            else:
                # cancel operation
                pass
        
    def on_checkbox_state_changed(self, state, row):
        
        if state:
            self.selected_rows.append(row+1)
            # print(row+1)
        else:
            # print(row+1)
            self.selected_rows.remove(row+1)



    def save_Mixtable_execute(self):
        
        if self.ui.main_body_stackedWidget.currentWidget() == self.ui.mixData:
        
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
                    Registration = self.ui.tableWidget.item(i, 6).text()
                    Semester = self.ui.tableWidget.item(i, 7).text()
                    Course = self.ui.tableWidget.item(i, 8).text()
                    
                    try:
                        # Update the corresponding row in the database
                        cursor.execute("UPDATE Queue_Student_Data SET firstname=?, lastname=?, gender=?, age=?, nationality=?, Registration=?, Semester=?, Course=? WHERE IDnumber=?", (firstname, lastname, gender, age, nationality, Registration, Semester, Course, IDnumber))
                        connection.commit()
                        QMessageBox.information(self, "Info", "Data Updated Successfully")
                        
                    except Exception as e:
                        QMessageBox.warning(self, "Error", "Error saving data : {}".format(e))
                        print(e)
                        
                connection.close()
                
            else:
                # cancel operation
                pass

        else:
            QMessageBox.information(self, "Info", "Save Changes Unavailable")
            pass
            
        
        self.refresh_data()



    def approve_to_BSIT_db(self):
        if self.selected_rows == []:
            QMessageBox.warning(self, "Warning", "There is no selected Data.")
        else:
            result = QMessageBox.question(self, 'Confirm', "Are you sure you want to move the selected data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if result == QMessageBox.Yes:
                conn = sqlite3.connect('queue.db')
                with conn:
                    cursor = conn.cursor()
                    for row in self.selected_rows:
                            cursor.execute("INSERT INTO BSIT_Student_Data (firstname, lastname, gender, age, nationality, Registration, Semester, Course) SELECT firstname, lastname, gender, age, nationality, Registration, Semester, Course FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                            conn.commit()
                            
                    for row in self.selected_rows:
                        cursor.execute("DELETE FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                conn.close()
                
                self.refresh_data()
                
                QMessageBox.information(self, "Info", "Data Updated Successfully")

            else:
                # cancel operation
                pass
        
    def approve_to_COMSCI_db(self):
        
        if self.selected_rows == []:
            QMessageBox.warning(self, "Warning", "There is no selected Data.")
        else:
            result = QMessageBox.question(self, 'Confirm', "Are you sure you want to move the selected data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if result == QMessageBox.Yes:
                conn = sqlite3.connect('queue.db')
                with conn:
                    cursor = conn.cursor()
                    for row in self.selected_rows:
                            cursor.execute("INSERT INTO COMSCI_Student_Data (firstname, lastname, gender, age, nationality, Registration, Semester, Course) SELECT firstname, lastname, gender, age, nationality, Registration, Semester, Course FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                            conn.commit()
                            
                    for row in self.selected_rows:
                        cursor.execute("DELETE FROM Queue_Student_Data WHERE IDnumber = ?", (row,))
                conn.close()
                
                self.refresh_data()
                
                QMessageBox.information(self, "Info", "Data Updated Successfully")

            else:
                # cancel operation
                pass
            



        # filter data from the table
    def filter_BSIT_data(self):
        search_text = self.ui.tableWidget_BSIT.text().lower()
        for i in range(self.ui.tableWidget.rowCount()):
            match = False
            for j in range(self.ui.tableWidget_BSIT.columnCount()):
                item = self.ui.tableWidget_BSIT.item(i, j)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget_BSIT.setRowHidden(i, not match)

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
    
    def filter_COMSCI_data(self):
        
        search_text = self.ui.searchLineEdit_COMSCI.text().lower()
        for i in range(self.ui.tableWidget_COMSCI.rowCount()):
            match = False
            for j in range(self.ui.tableWidget_COMSCI.columnCount()):
                item = self.ui.tableWidget_COMSCI.item(i, j)
                if item and search_text in item.text().lower():
                    match = True
                    break
            self.ui.tableWidget_COMSCI.setRowHidden(i, not match)
    
    
    
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
            
        # Enter data from the college register page
    def enter_data_college(self):
        first_name = self.ui.lineEdit_firstname.text()
        last_name = self.ui.line_Edit_lastname.text()
        gender = self.ui.cmbbox_title.currentText()
        age = self.ui.spinBox_age.value()
        nationality = self.ui.cmbbox_nationality.currentText()

        if self.ui.cmbbox_course.currentIndex() == 0:
            course = 'BSIT'
        else:
            course = 'COMSCI'
            
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
            Registration TEXT,
            Semester INT,
            Course TEXT
            )
        '''
        conn.execute(table_create_query)
        # Insert Data
        data_insert_query = '''INSERT INTO Queue_Student_Data ( firstname, lastname, gender, age, nationality, Registration, Semester, Course) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''' 
        data_insert_tuple =(
                    first_name,
                    last_name,
                    gender,
                    age,
                    nationality,
                    register_value,
                    completed_semester,
                    course
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
        
        # Clearing the last input of a user
        lineEdits = [self.ui.lineEdit_firstname, self.ui.line_Edit_lastname]
        for lineEdit in lineEdits:
            lineEdit.clear()
        self.ui.cmbbox_title.setCurrentIndex(0)
        self.ui.cmbbox_nationality.setCurrentIndex(0)
        self.ui.cmbbox_course.setCurrentIndex(0)
        self.ui.spinBox_age.setValue(0)
        self.ui.spinBox_semester.setValue(0)
        self.ui.checkBox_registered.setChecked(False)
        self.ui.checkBox_terms.setChecked(False)

# App execution context           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program_Window()
    
    window.setWindowTitle("SQL DATABASE PROJECT")
    
    window.start_queue_db()

    sys.exit(app.exec())