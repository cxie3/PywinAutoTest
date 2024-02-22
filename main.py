from pywinauto.application import Application
from pywinauto import Desktop
#-------------------------- Open Calculator ---------------------
app = Application(backend="uia").start('calc.exe').connect(title='Calculator', timeout=10)

calc = app.window(title='Calculator', class_name='ApplicationFrameWindow')
calc.print_control_identifiers()

button_1 = calc.child_window(title="One", auto_id="num1Button", control_type="Button")
button_2 = calc.child_window(title="Two", auto_id="num2Button", control_type="Button")
button_3 = calc.child_window(title="Three", auto_id="num3Button", control_type="Button")
button_4 = calc.child_window(title="Four", auto_id="num4Button", control_type="Button")
button_5 = calc.child_window(title="Five", auto_id="num5Button", control_type="Button")
button_6 = calc.child_window(title="Six", auto_id="num6Button", control_type="Button")
button_7 = calc.child_window(title="Seven", auto_id="num7Button", control_type="Button")
button_8 = calc.child_window(title="Eight", auto_id="num8Button", control_type="Button")
button_9 = calc.child_window(title="Nine", auto_id="num9Button", control_type="Button")
button_0 = calc.child_window(title="Zero", auto_id="num0Button", control_type="Button")
button_Divide = calc.child_window(title="Divide by", auto_id="divideButton", control_type="Button")
button_Multiply = calc.child_window(title="Multiply by", auto_id="multiplyButton", control_type="Button")
button_Minus = calc.child_window(title="Minus", auto_id="minusButton", control_type="Button")
button_Plus = calc.child_window(title="Plus", auto_id="plusButton", control_type="Button")
button_Equals = calc.child_window(title="Equals", auto_id="equalButton", control_type="Button")

button_1.click_input()
button_Plus.click_input()
button_2.click_input()
button_Equals.click_input()

close = calc.child_window(title="Close Calculator", auto_id="Close", control_type="Button")
#close.click_input()


#-------------------------- Open Notepad ---------------------
# app = Application(backend="uia").start('notepad.exe').connect(title='Untitled - Notepad', timeout=10)
# app.UntitledNotepad.print_control_identifiers()
# # Access the main edit control and type "Test"
# textEditor = app.UntitledNotepad.edit
# textEditor.type_keys("Test", with_spaces=True)
#
# # Access the "File" menu and click it
# fileMenu = app.UntitledNotepad.child_window(title="File", control_type="MenuItem")
# fileMenu.click_input()
#
# maxMenu = app.UntitledNotepad.child_window(title="Maximize", control_type="Button")
# maxMenu.click_input()
