import wx, ledwiz

class ZeroLight(wx.Frame):
  
    def __init__(self, *args, **kwargs):
        super(ZeroLight, self).__init__(*args, **kwargs)
        self.tempsliderR1 = 0
        self.tempsliderG1 = 0
        self.tempsliderB1 = 0

        self.tempsliderR2 = 0
        self.tempsliderG2 = 0
        self.tempsliderB2 = 0
        
        self.tempsliderR3 = 0
        self.tempsliderG3 = 0
        self.tempsliderB3 = 0

        self.tempsliderR4 = 0
        self.tempsliderG4 = 0
        self.tempsliderB4 = 0
        
        
        self.InitUI()
        
    def InitUI(self):
        # build window
        self.SetSize((300, 550))
        self.SetTitle('ZeroLight')
        self.Centre()
        # build menu
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', '&Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)
        # build button
        pnl = wx.Panel(self)
        onButton = wx.Button(pnl, wx.ID_ANY, 'On!', (10, 10))
        self.Bind(wx.EVT_BUTTON,  self.Onled, id=onButton.GetId())
        
        offButton = wx.Button(pnl, wx.ID_ANY, 'Off!', (10, 40))
        self.Bind(wx.EVT_BUTTON,  self.Offled, id=offButton.GetId())
        
        # build slider1
        self.sliderR1 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,80), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderG1 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,130), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderB1 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,180), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderR1.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderG1.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderB1.GetId())
        
        # build slider2
        self.sliderR2 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,80), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderG2 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,130), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderB2 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,180), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderR2.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderG2.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderB2.GetId())

        # build slider3
        self.sliderR3 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,230), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderG3 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,280), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderB3 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (10,330), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderR3.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderG3.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderB3.GetId())

        # build slider3
        self.sliderR4 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,230), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderG4 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,280), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        self.sliderB4 = wx.Slider(pnl, wx.ID_ANY, 0, 0,255, (140,330), (125, -1), wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS )
        
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderR4.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderG4.GetId())
        self.Bind(wx.EVT_SLIDER, self.sliderUpdate, id=self.sliderB4.GetId())
        
        self.Show(True)
    
    def OnQuit(self, e):
        self.Close()
        
    def Onled(self, e):
        led.onleds()

    def Offled(self, e):
        led.offleds()
        
    def sliderUpdate(self, e):
        if ((led.convert48(self.sliderR1.GetValue()) != self.tempsliderR1) or (led.convert48(self.sliderG1.GetValue()) != self.tempsliderG1) or (led.convert48(self.sliderB1.GetValue()) != self.tempsliderB1)):
            led.setleds(self.sliderR1.GetValue(), self.sliderG1.GetValue(), self.sliderB1.GetValue(), 1)
            self.tempsliderR1 = led.convert48(self.sliderR1.GetValue())
            self.tempsliderG1 = led.convert48(self.sliderG1.GetValue())
            self.tempsliderB1 = led.convert48(self.sliderB1.GetValue())
            print self.tempsliderR1 , self.tempsliderG1 , self.tempsliderB1

        if ((led.convert48(self.sliderR2.GetValue()) != self.tempsliderR2) or (led.convert48(self.sliderG2.GetValue()) != self.tempsliderG2) or (led.convert48(self.sliderB2.GetValue()) != self.tempsliderB2)):
            led.setleds(self.sliderR2.GetValue(), self.sliderG2.GetValue(), self.sliderB2.GetValue(), 2)
            self.tempsliderR2 = led.convert48(self.sliderR2.GetValue())
            self.tempsliderG2 = led.convert48(self.sliderG2.GetValue())
            self.tempsliderB2 = led.convert48(self.sliderB2.GetValue())
            print self.tempsliderR2 , self.tempsliderG2 , self.tempsliderB2
            
        if ((led.convert48(self.sliderR3.GetValue()) != self.tempsliderR3) or (led.convert48(self.sliderG3.GetValue()) != self.tempsliderG3) or (led.convert48(self.sliderB3.GetValue()) != self.tempsliderB3)):
            led.setleds(self.sliderR3.GetValue(), self.sliderG3.GetValue(), self.sliderB3.GetValue(), 3)
            self.tempsliderR3 = led.convert48(self.sliderR3.GetValue())
            self.tempsliderG3 = led.convert48(self.sliderG3.GetValue())
            self.tempsliderB3 = led.convert48(self.sliderB3.GetValue())
            print self.tempsliderR3 , self.tempsliderG3 , self.tempsliderB3 
            
        if ((led.convert48(self.sliderR4.GetValue()) != self.tempsliderR4) or (led.convert48(self.sliderG4.GetValue()) != self.tempsliderG4) or (led.convert48(self.sliderB4.GetValue()) != self.tempsliderB4)):
            led.setleds(self.sliderR4.GetValue(), self.sliderG4.GetValue(), self.sliderB4.GetValue(), 4)
            self.tempsliderR4 = led.convert48(self.sliderR4.GetValue())
            self.tempsliderG4 = led.convert48(self.sliderG4.GetValue())
            self.tempsliderB4 = led.convert48(self.sliderB4.GetValue())
            print self.tempsliderR4 , self.tempsliderG4 , self.tempsliderB4

if __name__ == '__main__':
    print ""
    print "Please use ZeroLight.py or ZeroLight.pyw instead."
    exit()
else:
    app = wx.App(False) # set to true for output of stuff.
    ZeroLight(None, title='ZeroLight')
    led=ledwiz.LedWiz()
    app.MainLoop()