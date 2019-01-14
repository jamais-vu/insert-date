# insert-date

A Sublime Text 3 plugin to insert the current date and time at the cursor. 

# Installation
To install the plugin, clone this repository to your Sublime Text `Packages`
directory. The plugin will then be active. There is no need to restart 
Sublime.

If you have trouble locating your Packages directory, open Sublime, and in the 
menu bar select `Preferences` then `Browse Packages...` to open the Packages 
directory. Here are the usual locations for each operating system:

**Windows**  
Installed: `C:\Users\<your username>\AppData\Roaming\Sublime Text 3\Packages`  
Portable: `<path>\Sublime Text 3\Data\Packages`
 
**OS X**  
`~/Library/Application Support/Sublime Text 3/Packages`
 
**Linux**  
`~/.config/sublime-text-3/Packages/`

### Uninstall

Delete the directory `<path>\Packages\insert-date`.

# Usage
Use the key bindings to insert the current local date or time at the cursor. 
This will replace any selected text. If there are multiple cursors, the 
insert is done at the location of the first cursor.

**Date**: `alt+shift+d`. Date is formatted `YYYY-MM-DD `.  
**Time**: `alt+shift+t`. Time is formatted `HH:MM `, using the 24 hr clock.  

Both the date and the time have a space at the end.

The inserted text remains selected; you will have to manually deselect it to
continue typing. [This inconvenience will be fixed](
https://github.com/jamais-vu/insert-date/issues/1#issue-398226790).

# Notes and Acknowledgement
My first Sublime plugin. I wanted a simple way to insert the time or date when
I am writing in my journal. The Sublime Package Control website was experiencing
an unknown error so I chose to make my own plugin. 
[This tutorial](https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/
 "Creating Sublime Text 3 Plugins, by Sam Mello") helped me get started.
