import wx
import wx.lib.agw.cubecolourdialog as CCD
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "File and Folder Dialogs Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        self.colourData = None
 
        colorDlgBtn = wx.Button(panel, label="Open ColorDialog")
        colorDlgBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        colorCubeBtn = wx.Button(panel, label="Open ColorCubeDialog")
        colorCubeBtn.Bind(wx.EVT_BUTTON, self.onCubeColorDialog)
 
        # put the buttons in a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(colorDlgBtn, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(colorCubeBtn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onColorDlg(self, event):
        """
        This is mostly from the wxPython Demo!
        """
        dlg = wx.ColourDialog(self)
 
        # Ensure the full colour dialog is displayed, 
        # not the abbreviated version.
        dlg.GetColourData().SetChooseFull(True)
 
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print 'You selected: %s\n' % str(data.GetColour().Get())
 
        dlg.Destroy()
 
    #----------------------------------------------------------------------
    def onCubeColorDialog(self, event):
        """
        This is mostly from the wxPython Demo!
        """
        # self.colourData.SetColour(self.GetBackgroundColour())
 
        dlg = CCD.CubeColourDialog(self, self.colourData)
 
        if dlg.ShowModal() == wx.ID_OK:
 
            # If the user selected OK, then the dialog's wx.ColourData will
            # contain valid information. Fetch the data ...
            self.colourData = dlg.GetColourData()
            h, s, v, a = dlg.GetHSVAColour()
 
            # ... then do something with it. The actual colour data will be
            # returned as a three-tuple (r, g, b) in this particular case.
            colour = self.colourData.GetColour()
            self.SetBackgroundColour(self.colourData.GetColour())
            self.Refresh()
 
        dlg.Destroy()
 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()