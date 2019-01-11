import sublime
import sublime_plugin
import datetime

# Sublime Text supports multiple cursors in a single file, so we use 
# self.view.sel()[0].begin() to get the location of the first cursor.

class DateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.replace(edit, self.view.sel()[0], 
                         str(datetime.datetime.now().date()) + ' ')

class TimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.replace(edit, self.view.sel()[0],
                         str(datetime.datetime.now().time())[0:5] + ' ')