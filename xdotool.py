#xdotool.py:
"""
This module was updated 171207 by C. Andrews Lavarre www.privustech.com
It implements a number of xdotool functions:
    xdo_find    A function to find the ID of the window whose title contains a string
    xdo_get     A function to set the focus to a specified window
    xdo_key     A function to send keystrokes to a specified window
    xdo_write   A function to type a string
"""
import subprocess


def xdo_find(wtitle):
    """
    This function was updated 171207 by C. Andrews Lavarre www.privustech.com
    It returns the numeric window ID of the window whose title contains wtitle.
        It returns a decimal number, e.g., 178271574. Other programs use hexadecimal.

    Keyword arguments:
    wtitle  a portion of the title of the window to be found.
        Multiple word titles must be enclosed in quotes.
        Example:
            result = xdotool.xdo_find("AutoKey")
            result = xdotool.xdo_find("\"Google Earth\"")

    """
    # Get all the windows of this name
    cmd_string = "xdotool search --name " + wtitle
    try:
        fwindows = subprocess.check_output(cmd_string, shell=True)
    # Some windows (Konsole) are a class:
    except:
        cmd_string = "xdotool search --class " + wtitle
        try:
            fwindows = subprocess.check_output(cmd_string, shell=True)
        except:
            # Neither name nor class, does not exist
            print(wtitle + " not found")
            return
    # fwindows is a space-delimited list: Parse it
    lwindows = fwindows.split()
    #print(lwindows)
    # Get the particular one
    for window in lwindows:
        windownumber = str(window)
        #fix the string
        windownumber = windownumber("'")
        windownumber = windownumber[1]
        windownumber = windownumber.split('\\')
        windownumber = windownumber[0]
        cmd_string = "xdotool getwindowname " + windownumber
        win_name = subprocess.check_output(cmd_string, shell=True)
        if wtitle in win_name:
            return window


def xdo_get(windowID):
    """
    This function was updated 171207 by C. Andrews Lavarre www.privustech.com
    It sets the focus to the specified window ID. (windowfocus does not work.)

    Keyword argument:
        windowID    The numerical ID of the desired window
        :param windowID:
        :rtype: object
    """
    try:
        cmd_string = 'xdotool windowactivate ' + windowID
        result = subprocess.call(cmd_string, shell=True)
    except:
        pass

def xdo_key(kstroke):
    """
    This function was updated 171207 by C. Andrews Lavarre www.privustech.com
    It outputs a series of keystrokes to the active window.

    Keyword arguments:
    kstroke  A string (enclosed in quotes) that the function will output

    Example:
        "ctrl+v"
        "ctrl+shift+v"
        "Up", "Down", "Left", "Right, Home, End"
    See
        https://www.linux.org/threads/xdotool-keyboard.10528/
        for a full list
    """
    # Build the command
    #cmd_string = "xdotool key --window " + fwindow + " " + kstroke
    cmd_string = "xdotool key " + kstroke
    print(cmd_string)
    # Send the keystroke to the specified window
    subprocess.call(cmd_string, shell=True)


def xdo_write(wstring):
    """
    This function was updated 171207 by C. Andrews Lavarre www.privustech.com
    It provides a string writing infrastructure function

    Keyword arguments:
    string  A string enclosed in quotes that the function will type
    Example:
        "Hello World!"
            If writing to a terminal the string must be double  quoted:
    Example:
        "\"geany -i &\""
    """

    cmd_string = "xdotool type " + wstring
    print(cmd_string)
    # Send the keystroke to the specified window
    subprocess.call(cmd_string, shell=True)
