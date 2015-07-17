import pywintypes
import ctypes
import win32gui
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []
def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append((hwnd, buff.value))

        class_name = "notepad"
        window_name = None
        if buff.value.find("Notepad") >= 0:
            print "###################################bringing window to front"
            print "hwnd=", repr(hwnd)

            handle = win32gui.FindWindow(class_name, window_name) #find a window using the class name
            print "handle=", repr(handle)
            print win32gui.GetWindowText(handle)

            ##http://stackoverflow.com/questions/2090464/python-window-activation
            ##http://stackoverflow.com/questions/14653168/get-hwnd-of-each-window-python
            #ctypes.windll.user32.MoveWindow(titles[5][0], 0, 0, 760, 500, True)
            ctypes.windll.user32.SetForegroundWindow(hwnd, 0, 0, 760, 500, True)
            #win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)#####<----TypeError: The object is not a PyHANDLE object


            ##works:
            #win32gui.SetForegroundWindow(handle) #bring most recent window of type class to the front
            print "###################################--------------"

    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)

for i in range(len(titles)):
    print(titles)[i]

#win32gui.MoveWindow((titles)[5][0], 0, 0, 760, 500, True)


##handle = win32gui.FindWindow(0, "PyScripter - C:\\NatLink\\NatLink\\MacroSystem\\_testEnumerateWindows.py")  #paassing 0 as I dont know classname
##if handle:
##    print "handle=", handle
##    win32gui.SetForegroundWindow(handle)  #put the window in foreground
##    print "###################################bringing window to front"

##
###http://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
##def windowEnumerationHandler(hwnd, top_windows):
##    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
##
##if __name__ == "__main__":
##    results = []
##    top_windows = []
##    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
##    for i in top_windows:
##        if "notepad" in i[1].lower():
##            print i
##            win32gui.ShowWindow(i[0],5)
##            win32gui.SetForegroundWindow(i[0])
##            break







#create a handle
            #handle = pywintypes.HANDLE()
            #handle = hwnd