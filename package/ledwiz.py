import win32com.client

class LedWiz:
    def __init__(self):

        self.ledwiz=win32com.client.Dispatch("LEDWiz_Control.LED_Wiz") # setup ledwiz OCX
        self.ledwiz.DeviceNumber = 1
        print "LedWiz: " , self.ledwiz.detected
        self.ledwiz.command="GPS:1"
        self.offleds()
        self.channel1 = "0,0,0,"
        self.channel2 = "0,0,0,"
        self.channel3 = "0,0,0,0,"
        self.channel4 = "0,0,0,"
        
        
    def __del__(self):
        self.offleds()
        
    def setleds(self, r, g, b, c = None): 

        r=self.convert48(r) # convert 0-255 to 0-48
        g=self.convert48(g) # convert 0-255 to 0-48
        b=self.convert48(b) # convert 0-255 to 0-48
        
        if (r == 0):
            if ( c == 1 ):
                self.ledwiz.command="S01:0"
            elif ( c == 2 ):
                self.ledwiz.command="S04:0"
            elif ( c == 3 ):
                self.ledwiz.command="S07:0"
            elif ( c == 4 ):
                self.ledwiz.command="S11:0"
            else:
                self.ledwiz.command="S01:0"
                self.ledwiz.command="S04:0"
                self.ledwiz.command="S07:0"
                self.ledwiz.command="S11:0"
        else:
            if ( c == 1 ):
                self.ledwiz.command="S01:1"
            elif ( c == 2 ):
                self.ledwiz.command="S04:1"
            elif ( c == 3 ):
                self.ledwiz.command="S07:1"
            elif ( c == 4 ):
                self.ledwiz.command="S11:1"
            else:
                self.ledwiz.command="S01:1"
                self.ledwiz.command="S04:1"
                self.ledwiz.command="S07:1"
                self.ledwiz.command="S11:1"
            
        if (g == 0):
            if ( c == 1 ):
                self.ledwiz.command="S02:0"
            elif ( c == 2 ):
                self.ledwiz.command="S05:0"
            elif ( c == 3 ):
                self.ledwiz.command="S08:0"
            elif ( c == 4 ):
                self.ledwiz.command="S12:0"
            else:
                self.ledwiz.command="S02:0"
                self.ledwiz.command="S05:0"
                self.ledwiz.command="S08:0"
                self.ledwiz.command="S12:0"
        else:
            if ( c == 1 ):
                self.ledwiz.command="S02:1"
            elif ( c == 2 ):
                self.ledwiz.command="S05:1"
            elif ( c == 3 ):
                self.ledwiz.command="S08:1"
            elif ( c == 4 ):
                self.ledwiz.command="S12:1"
            else:
                self.ledwiz.command="S02:1"
                self.ledwiz.command="S05:1"
                self.ledwiz.command="S08:1"
                self.ledwiz.command="S12:1"
            
        if (b == 0):
            if ( c == 1 ):
                self.ledwiz.command="S03:0"
            elif ( c == 2 ):
                self.ledwiz.command="S06:0"
            elif ( c == 3 ):
                self.ledwiz.command="S10:0"
            elif ( c == 4 ):
                self.ledwiz.command="S13:0"
            else:
                self.ledwiz.command="S03:0"
                self.ledwiz.command="S06:0"
                self.ledwiz.command="S10:0"
                self.ledwiz.command="S13:0"
        else:
            if ( c == 1 ):
                self.ledwiz.command="S03:1"
            elif ( c == 2 ):
                self.ledwiz.command="S06:1"
            elif ( c == 3 ):
                self.ledwiz.command="S10:1"
            elif ( c == 4 ):
                self.ledwiz.command="S13:1"
            else:
                self.ledwiz.command="S03:1"
                self.ledwiz.command="S06:1"
                self.ledwiz.command="S10:1"
                self.ledwiz.command="S13:1"
            
        r = str(r)
        g = str(g)
        b = str(b)
        

        
        if ( c == 1 ):
            self.channel1 = "%s, %s, %s," % (r,g,b)
        elif ( c == 2):
            self.channel2 = "%s, %s, %s," % (r,g,b)
        elif (c == 3):
            self.channel3 = "%s, %s, 0, %s," % (r,g,b)
        elif (c == 4):
            self.channel4 = "%s, %s, %s," % (r,g,b)
        else:
            self.channel1 = "%s, %s, %s," % (r,g,b)
            self.channel2 = "%s, %s, %s," % (r,g,b)
            self.channel3 = "%s, %s, 0, %s," % (r,g,b)
            self.channel4 = "%s, %s, %s," % (r,g,b)
        
        self.ledwiz.command="PBA:" + self.channel1 + self.channel2 + self.channel3 + self.channel4 + "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        
    def onleds(self):
        print "Leds On!"
        self.ledwiz.command="SBA:255,255,255,255,1" # all leds off
    def offleds(self):
        print "Leds Off!"
        self.ledwiz.command="SBA:0,0,0,0,1" # all leds off
        
    def convert48(self, color):
        return ((color*48)/255)