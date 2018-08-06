# coding=utf-8
import wx  # Import wxPython GUI toolkit


class GUI(wx.Panel):  # Subclass wxPython Panel
    def __init__(self, parent):  # Initialize super class
        wx.Panel.__init__(self, parent)
        parent.CreateStatusBar()  # Create Status Bar

        menu = wx.Menu()  # Create the Menu
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")  # Add Menu Items to the Menu
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", "Exit the GUI")

        menu_bar = wx.MenuBar()  # Create the MenuBar
        menu_bar.Append(menu, "File")  # Give the Menu a Title
        parent.SetMenuBar(menu_bar)  # Connect the MenuBar to the frame

        self.textBox = wx.TextCtrl(self, size=(280, 50), style=wx.TE_MULTILINE)  # Create a Text Control widget

        button = wx.Button(self, label="Print", pos=(0, 60))  # Create a Print Button
        self.Bind(wx.EVT_BUTTON, self.print_button, button)  # Connect Button to Click Event method

    def print_button(self, event):  # callback event handler
        self.textBox.AppendText("\nThe Print Button has been clicked!")  # Click Event method


app = wx.App()  # Create instance of wxPython application
frame = wx.Frame(None, title="Python GUI using wxPython", size=(300, 180))  # Create frame
GUI(frame)  # Pass frame into GUI
frame.Show()  # Display the frame
app.MainLoop()  # Run the main GUI event loop
