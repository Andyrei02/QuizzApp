import os
import sys
import ast
import json
import shutil
import webbrowser
from tkinter import filedialog


from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QFile, QTextStream
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel

import file_w_r as f_manage
from game_ui import Ui_MainWindow


class Config:
	quiz_folder = "quiz_list"
	loc_scenario = lambda folder, name: os.path.join(folder, f"{name}.json")
	list_quiz = ""
	dict_scenario = {}
	current_level = 0

	def conf_btn_answer(btn=None):
		#btn.setMinimumSize(QtCore.QSize(200, 80))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setStrikeOut(False)
		font.setKerning(True)
		btn.setFont(font)
		btn.setMouseTracking(False)
		btn.setTabletTracking(False)
		btn.setAcceptDrops(False)
		btn.setAutoFillBackground(False)
		btn.setCheckable(False)
		btn.setAutoRepeat(False)
		btn.setAutoExclusive(False)
		btn.setAutoDefault(False)
		btn.setDefault(False)
		btn.setFlat(False)

	style_combobox = "QComboBox {\
		background-color: rgb(50, 50, 50);\
		border-color: rgb(252, 135, 72);\
		border-width: 2px;\
		border-style: solid;\
		padding: 4px;\
	}\
	QComboBox::drop-down {\
		border: none;\
	}\
	QComboBox::drop-down:pressed {\
		background-color: rgb(50, 50, 50);\
	}\
	QComboBox::down-arrow {\
		image: url(icons/drop_down.png);\
	}\
	QComboBox::down-arrow:pressed {\
		position: relative;\
		top: 1px; left: 1px;\
		QComboBox::drop-down {}\
	}"

	style_scrollbar = ""

	style_default_btn = "QPushButton {\
		background-color: rgb(252, 110, 32);\
		margin: 10px 0;\
		border-radius: 15px;\
		border-style: solid;\
		border-width: 2px;\
		border-color: rgb(252, 135, 72);\
	}\
	QPushButton:pressed {\
		color: rgb(254, 232, 208);\
		background-color: rgb(50, 50, 50);\
	}"

	style_functional_btn = "QPushButton {\
		border-style: solid;\
		border-width: 2px;\
		border-radius: 10px;\
		padding: 6px;\
		border-color: rgb(252, 135, 72);\
	}\
	QPushButton:pressed {\
		background-color: rgb(50, 50, 50);\
		border-style: inset;\
	}"


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlag(Qt.FramelessWindowHint)


		icon_exclamation = QtGui.QIcon()
		icon_exclamation.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_settings.setIcon(icon_exclamation)
		

		icon_back = QtGui.QIcon()
		icon_back.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_back_to_main.setIcon(icon_back)
		self.ui.btn_back_to_main.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_2.setIcon(icon_back)
		self.ui.btn_back_to_main_2.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_3.setIcon(icon_back)
		self.ui.btn_back_to_main_3.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_4.setIcon(icon_back)
		self.ui.btn_back_to_main_4.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_5.setIcon(icon_back)
		self.ui.btn_back_to_main_5.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_6.setIcon(icon_back)
		self.ui.btn_back_to_main_6.setStyleSheet(Config.style_functional_btn)
		self.ui.btn_back_to_main_7.setIcon(icon_back)
		self.ui.btn_back_to_main_7.setStyleSheet(Config.style_functional_btn)


		self.list_btn = []

		self.file_wr = f_manage.FileWR()
		self.level = Config.current_level
		self.name_quiz = ""
		self.editing_quiz = {"name_quiz": "", "question": []}

		#   Settings frame
		self.ui.btn_back_to_main.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_frame))

		#   Exclamation frame
		self.ui.btn_back_to_main_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_frame))
		icon_gmail = QtGui.QIcon()
		icon_gmail.addPixmap(QtGui.QPixmap("icons/gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_link_gmail.setIcon(icon_gmail)
		icon_instagram = QtGui.QIcon()
		icon_instagram.addPixmap(QtGui.QPixmap("icons/instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_link_instagram.setIcon(icon_instagram)
		icon_telegram = QtGui.QIcon()
		icon_telegram.addPixmap(QtGui.QPixmap("icons/telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_link_telegram.setIcon(icon_telegram)
		icon_github = QtGui.QIcon()
		icon_github.addPixmap(QtGui.QPixmap("icons/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_link_github.setIcon(icon_github)

		self.ui.btn_link_gmail.clicked.connect(lambda: webbrowser.open("mailto:acenusa58@gmail.com"))
		self.ui.btn_link_telegram.clicked.connect(lambda: webbrowser.open("https://t.me/andyrei"))
		self.ui.btn_link_instagram.clicked.connect(lambda: webbrowser.open("https://www.instagram.com/andr.ei57/"))
		self.ui.btn_link_github.clicked.connect(lambda: webbrowser.open("https://github.com/Andyrei02"))


		#   Main frame
		self.ui.stackedWidget.setCurrentWidget(self.ui.main_frame)
		self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_frame))
		self.ui.btn_manage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame))
		self.ui.btn_start.clicked.connect(self.draw_start_frame)

		icon_exclamation = QtGui.QIcon()
		icon_exclamation.addPixmap(QtGui.QPixmap("icons/exclamation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.ui.btn_exclamation.setIcon(icon_exclamation)
		self.ui.btn_exclamation.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.frame_exclamation))

		#   Start game
		self.ui.btn_back_to_main_3.clicked.connect(lambda: (self.go_back_to_main(), self.remove_btn()))

		#   Manage quiz frame
		self.ui.btn_back_to_main_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_frame))
		self.ui.btn_new_quiz.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_quiz_frame))
		self.ui.btn_edit_quiz.clicked.connect(self.edit_quiz_frame)
		self.ui.btn_import_quiz.clicked.connect(self.import_quiz_function)

		#   Import exist file frame
		self.ui.btn_rename.clicked.connect(self.rename_file)
		self.ui.btn_replace.clicked.connect(self.replace_file)
		self.ui.btn_cancel_import_quiz.clicked.connect(self.cancel_import_file)

		#   New quiz frame
		self.ui.btn_add_question.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_question_frame))
		self.ui.btn_save_quiz.clicked.connect(lambda: self.save_quiz_frame(self.ui.lineEdit_name_quiz.text()))
		self.ui.btn_cancel_quiz.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame), self.cancel_quiz_frame()))

		#   New question
		self.ui.btn_add_answer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.new_answer_frame))
		self.ui.btn_save_question.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.new_quiz_frame), self.save_question_frame(self.ui.lineEdit_question.text())))
		self.ui.btn_cancel_question.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.new_quiz_frame), self.cancel_question_frame()))

		#  New answer
		self.ui.btn_save_answer.clicked.connect(lambda: self.save_answer_frame(self.ui.lineEdit_answer.text()))
		self.ui.btn_cancel_answer.clicked.connect(self.cancel_answer_frame)

		self.ui.btn_back_to_main_4.clicked.connect(self.back_to_start_frame)


		#   Win frame
		self.ui.btn_back_to_main_5.clicked.connect(self.draw_start_frame)

		#   Error quiz frame
		self.ui.btn_back_to_main_6.clicked.connect(self.draw_start_frame)

		self.check_language_box()
		#self.check_theme_box()
		self.check_bg_sound_box()


		self.custom_titlebar()

		self.show()

	def custom_titlebar(self):
		self.icon_maximize = QtGui.QIcon()
		self.icon_maximize.addPixmap(QtGui.QPixmap("icons/maximize_window_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.icon_restore = QtGui.QIcon()
		self.icon_restore.addPixmap(QtGui.QPixmap("icons/restore_down_window_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		def btn_close_clicked():
			self.window().close()

		def btn_max_clicked():
			if int(self.windowState()) == Qt.WindowNoState:
				self.setWindowState(Qt.WindowMaximized)
				self.ui.btn_maximize_restore_window.setIcon(self.icon_restore)
			elif int(self.windowState()) == Qt.WindowMaximized:
				self.setWindowState(Qt.WindowNoState)
				self.ui.btn_maximize_restore_window.setIcon(self.icon_maximize)

		def btn_min_clicked():
			self.setWindowState(Qt.WindowMinimized)

		self.ui.btn_close_window.clicked.connect(btn_close_clicked)
		self.ui.btn_maximize_restore_window.clicked.connect(btn_max_clicked)
		self.ui.btn_minimize_window.clicked.connect(btn_min_clicked)

		self.pressing = False
		self.dragPosition = QPoint()

	def mousePressEvent(self, event):
		if 0 < event.localPos().x() < self.frameGeometry().width() and 0 < event.localPos().y() < 45:
				if int(self.windowState()) == Qt.WindowMaximized:
					self.setWindowState(Qt.WindowNoState)
					self.ui.btn_maximize_restore_window.setIcon(self.icon_maximize)

				self.start = event.globalPos()
				self.pressing = True

	def mouseMoveEvent(self, event):
		if self.pressing:
			self.end = event.globalPos()
			delta = self.end - self.start
			self.window().move(self.window().pos() + delta)
			self.start = self.end

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False


	def check_theme_box(self):
		def toggle_stylesheet(path):
			'''
			Toggle the stylesheet to use the desired path in the Qt resource
			system (prefixed by `:/`) or generically (a path to a file on
			system).

			:path:      A full path to a resource or file on system
			'''

			# get the QApplication instance,  or crash if not set
			app = QApplication.instance()
			if app is None:
				raise RuntimeError("No Qt Application found.")

			file = QFile(path)
			file.open(QFile.ReadOnly | QFile.Text)
			stream = QTextStream(file)
			app.setStyleSheet(stream.readAll())

		toggle_stylesheet(":/dark.qss")
		self.ui.comboBox_theme.setStyleSheet(Config.style_combobox)

	def check_bg_sound_box(self):
		self.ui.comboBox_sound.setStyleSheet(Config.style_combobox)

	@QtCore.pyqtSlot(int)
	def change_func(self, index):
		data = self.ui.comboBox_language.itemData(index)
		if data:
			self.trans.load(data)
			QtWidgets.QApplication.instance().installTranslator(self.trans)
		else:
			QtWidgets.QApplication.instance().removeTranslator(self.trans)

	def changeEvent(self, event):
		if event.type() == QtCore.QEvent.LanguageChange:
			self.ui.retranslateUi(self)
			super(MainWindow, self).changeEvent(event)

	def check_language_box(self):
		self.ui.comboBox_language.currentIndexChanged.connect(self.change_func)

		self.trans = QtCore.QTranslator(self)
		options = [("English", ""), ("русский", "languages/ru"), ("romana", "languages/ro"),]

		for i, (text, lang) in enumerate(options):
			self.ui.comboBox_language.addItem(text)
			self.ui.comboBox_language.setItemData(i, lang)

		self.ui.comboBox_language.setStyleSheet(Config.style_combobox)
		self.ui.retranslateUi(self)
		# print(self.ui.comboBox_language.itemData(0))

	def go_back_to_main(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.main_frame)
		print("back")

	def save_quiz_frame(self, text):
		print("Save Quiz", text)
		# print(self.ui.listWidget_questions.currentItem().text())
		if int(self.ui.listWidget_questions.count()) > 0:
			self.ui.listWidget_quiz.addItem(text)
			self.ui.lineEdit_name_quiz.setText("")

			self.editing_quiz["name_quiz"] = text
			self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame)

			print(self.editing_quiz)

	def cancel_quiz_frame(self):
		print("Cancel Quiz")
		self.ui.lineEdit_name_quiz.setText("")

	def edit_quiz_frame(self):
		current_item_text = self.ui.listWidget_quiz.currentItem().text()
		self.editing_quiz["name_quiz"] = current_item_text

	def save_question_frame(self, text):
		self.editing_quiz["question"].append(text)

		self.ui.listWidget_questions.addItem(text)
		self.ui.lineEdit_question.setText("")

	def cancel_question_frame(self):
		print("Cancel question")
		self.ui.lineEdit_question.setText("")

	def save_answer_frame(self, text):
		# self.editing_quiz["answer"] = 
		print(text, "save")

	def cancel_answer_frame(self):
		print("cancel")

	def import_quiz_function(self):
		self.ui.lineEdit_rename_quiz.setStyleSheet( "QLineEdit{\n"
"border-width: 1px;\n" 
"border-style: solid;\n" 
"border-color: black;\n" 
"}" );
		print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "quiz_list"))
		filename = filedialog.askopenfilename(title="import quiz", filetypes=(("json files","*.json"), ("all files","*.*")))
		if not os.path.exists(filename):
			try:
				shutil.copy(filename, os.path.join(os.path.dirname(os.path.abspath(__file__)), "quiz_list"))
			except FileNotFoundError:
				pass
		else:
			self.rename_quiz_masagebox(filename)

	def draw_start_frame(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.start_frame)

		Config.list_quiz = os.listdir(Config.quiz_folder)
		Config.list_quiz.sort()

		for name_quiz in Config.list_quiz:
			self.draw_btn(text=name_quiz[:-5], function=self.draw_running_game, surface=self.ui.scrollAreaWidgetContents, layout=self.ui.verticalLayout_16)
			#list_btn_quiz.append()

	def back_to_start_frame(self):
		self.level = 0
		self.draw_start_frame()

	def check_quiz_scenario(self, name_quiz):
		Config.dict_scenario = self.file_wr.read_json(Config.loc_scenario(Config.quiz_folder, name_quiz))

		self.dict_scenario = Config.dict_scenario

	def draw_running_game(self, name_quiz):
		self.name_quiz = name_quiz
		try:
			self.check_quiz_scenario(name_quiz)
		except json.decoder.JSONDecodeError:
			self.ui.stackedWidget.setCurrentWidget(self.ui.quiz_error_frame)
		else:

			self.ui.stackedWidget.setCurrentWidget(self.ui.game_running_frame)

			self.list_question =  list(self.dict_scenario.keys())

			self.draw_question(self.dict_scenario[self.list_question[self.level]][0])
			for answer in self.dict_scenario[self.list_question[self.level]][1]:
				self.draw_btn(text=answer, function=self.answers_func, surface=self.ui.frame_buttons, layout=self.ui.verticalLayout_18, config=Config.conf_btn_answer)

	def draw_question(self, text):
		self.ui.label_question.setText(text)

	def draw_btn(self, text="btn", function=None, surface=None, layout=None, config=None):
		btn = QtWidgets.QPushButton(surface)
		btn.setObjectName(text)
		layout.addWidget(btn, 0, QtCore.Qt.AlignTop)
		btn.setText(text)
		btn.setMinimumSize(QtCore.QSize(150, 60))
		btn.setStyleSheet(Config.style_default_btn)

		if config:
			config(btn)

		btn.clicked.connect(lambda: (self.remove_btn(), function(text) if function else _))
		
		self.list_btn.append(btn)
		return btn

	def answers_func(self, data):
		if str(self.dict_scenario[self.list_question[self.level]][1].index(data)) == str(self.dict_scenario[self.list_question[self.level]][2]):
			self.next_level()
		else:
			self.draw_running_game(self.name_quiz)

	def next_level(self):
		self.level += 1
		self.remove_question()
		if self.level == len(self.list_question):
			self.ui.stackedWidget.setCurrentWidget(self.ui.win_frame)
			self.level = 0
			self.remove_btn()
		else:
			self.draw_running_game(self.name_quiz)


	def remove_btn(self):
		for btn in self.list_btn:
			btn.deleteLater()
		self.list_btn = []

	def remove_question(self):
		self.ui.label_question.setText('')


	def rename_quiz_masagebox(self, filename):
		self.last_filename = filename
		self.ui.stackedWidget.setCurrentWidget(self.ui.rename_exist_file_frame)
		self.ui.label_quiz_name.setText(os.path.basename(filename)[:-5])

	def rename_file(self):
		new_filename = self.ui.lineEdit_rename_quiz.text()
		if len(new_filename.strip()) > 0:
			shutil.copy(self.last_filename, os.path.join(os.path.dirname(os.path.abspath(__file__)), f"quiz_list\\{new_filename}.json"))
			self.ui.lineEdit_rename_quiz.setText('')
			self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame)
		elif not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"quiz_list\\{new_filename}.json")):
			self.ui.lineEdit_rename_quiz.setStyleSheet( "QLineEdit{\n"
"border-width: 1px;\n" 
"border-style: solid;\n" 
"border-color: red;\n" 
"}" );
		else:
			self.ui.lineEdit_rename_quiz.setStyleSheet( "QLineEdit{\n"
"border-width: 1px;\n" 
"border-style: solid;\n" 
"border-color: red;\n" 
"}" );

	def replace_file(self):
		shutil.copy(self.last_filename, os.path.join(os.path.dirname(os.path.abspath(__file__)), f"quiz_list\\{os.path.basename(self.last_filename)}"))
		self.ui.lineEdit_rename_quiz.setText('')
		self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame)

	def cancel_import_file(self):
		self.ui.lineEdit_rename_quiz.setText('')
		self.ui.stackedWidget.setCurrentWidget(self.ui.manage_quiz_frame)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
