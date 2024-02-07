from pywinauto.application import Application
# open notepad
app = Application().start('notepad.exe', timeout=10)

main_dlg = app.UntitledNotepad
main_dlg.wait('visible')

main_dlg = app.window(title='Untitled - Notepad')

main_dlg.Edit.type_keys("Test pywinauto\n\t sample text^A",
                        with_spaces=True,
                        with_newlines=True,
                        pause=0.5,
                        with_tabs=True)