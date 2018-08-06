# coding=utf-8
import wx


class GUI(wx.Frame):  # Subclass wxPython frame
    def __init__(self, parent, title, size=(200, 100)):  # Initialize super class
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.SetBackgroundColour('white')  # Change the frame color
        self.CreateStatusBar()  # Create Status Bar

        menu = wx.Menu()  # Create the Menu
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")  # Add Menu Items to the Menu
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", " Exit the GUI")

        menu_bar = wx.MenuBar()  # Create the MenuBar
        menu_bar.Append(menu, "File")  # Give the Menu a Title
        self.SetMenuBar(menu_bar)  # Connect the Menu to the frame

        self.Show()  # Display the frame


app = wx.App()  # Create instance of wxPython application
GUI(None, "Python GUI using wxPython", (300, 150))  # Call sub-classed wxPython GUI
app.MainLoop()  # Run the main GUI event loop
