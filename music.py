import wx
import wx.html2

class MusicApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(MusicApp, self).__init__(*args, **kw)
        self.setup_ui()

    def setup_ui(self):
        self.SetMinSize((600, 400))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.browser = wx.html2.WebView.New(self.panel)
        self.load_youtube_music()

        self.setup_layout()
        self.setup_menu()

        self.Bind(wx.EVT_CLOSE, self.on_close)

    def setup_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.panel.SetSizer(sizer)

    def setup_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()

        open_youtube_music_item = file_menu.Append(wx.ID_ANY, "Open YouTube Music", "Open YouTube Music Website")
        self.Bind(wx.EVT_MENU, self.load_youtube_music, open_youtube_music_item)

        exit_item = file_menu.Append(wx.ID_EXIT, "Exit", "Exit the application")
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

    def load_youtube_music(self, event=None):
        self.browser.LoadURL("https://music.youtube.com")

    def on_close(self, event):
        if self.browser:
            self.browser.Destroy()
        self.Destroy()

    def on_exit(self, event):
        self.Close()

def main():
    app = wx.App(False)
    frame = MusicApp(None, title="YouTube Music App")
    frame.Center()
    frame.Show()

    app.MainLoop()

if __name__ == "__main__":
    main()
