import kivy
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.label import Label

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import webbrowser

Builder.load_string("""
<Calc>:
#:import NoTransition kivy.uix.screenmanager.NoTransition

    mainScore: _mainScore
    isActive: _isActive
    startButton: _startButton
    startButton2: _startButton2
    startButton3: _startButton3
    
    clockOne: _clockOne
    clockTwo: _clockTwo
    clockThree: _clockThree
    
    parts: 0
    parts2: 0
    parts3: 0
    mainScore: 0
    isActive: False
    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        
        canvas.before:
            Color:
                rgb: 0,0,.4
            Rectangle:
                pos:self.pos
                size:self.size
                

        ScreenManager:
            size_hint: .9, .65
            id: _screen_manager
            transition: NoTransition()
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:3
                    spacing:'2dp'
                    height: self.minimum_height
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                    Label:
                        text: 'AUTONOMOUS'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, 0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                        
                    Label:
                        text: 'GLYPH?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,0.3
                            Rectangle:
                                pos:self.pos
                                size:self.size

                    ToggleButton:
                        id: glyph
                        size_hint_y: None
                        text: 'SCORED'
                        height: '30dp'
                        group: 'g11'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive1(*args))
                    
                        
                    ToggleButton:
                        id: usedKey
                        size_hint_y: None
                        height: '30dp'
                        text: 'USED KEY'
                        group: 'g1'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive2(*args))
                    
                    Label:
                        text: 'ALLIANCE?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.3
                            Rectangle:
                                pos:self.pos
                                size:self.size
                        
                    ToggleButton:
                        id: glyph2
                        size_hint_y: None
                        text: 'SCORED'
                        height: '30dp'
                        group: 'g12'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive1(*args))
                    
                    ToggleButton:
                        id: usedKey2
                        size_hint_y: None
                        height: '30dp'
                        text: 'USED KEY'
                        group: 'g88'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive2(*args))
                        
                    
                    Label:
                        text: 'JEWEL?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.6
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    ToggleButton:
                        id: scoredYes
                        size_hint_y: None
                        text: 'TEAM'
                        height: '30dp'
                        group: 'g2'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive2(*args))
                    
                    ToggleButton:
                        id: scoredYes2
                        size_hint_y: None
                        text: 'ALLIANCE'
                        height: '30dp'
                        group: 'g9'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive2(*args))
                    
                
                    
                    Label:
                        text: 'PARKED?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.9
                            Rectangle:
                                pos:self.pos
                                size:self.size

                    ToggleButton:
                        id: parked
                        size_hint_y: None
                        text: 'TEAM'
                        height: '30dp'
                        group: 'g4'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive3(*args))
                    
                    ToggleButton:
                        id: parked2
                        size_hint_y: None
                        text: 'ALLIANCE'
                        height: '30dp'
                        group: 'g10'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive3(*args))

                        
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        size_hint: 1,None
                        height: '15dp'
                    Label:
                        size_hint: 1,None
                        height: '15dp'

                    Label:
                        text: 'TIMER (sec)'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    
                    Button:
                        id: _startButton
                        text: 'START'
                        background_color: (.8,0,0,1) 
                        size_hint: 1,None
                        height: '30dp'
                        on_release: 
                            _clockOne.start()
                            _startButton.text = str(root.timerStatus(*args))
                                           
                    IncrediblyCrudeClock:
                        id: _clockOne
                        size_hint: 1, None
                        height: '30dp'
                        text: '30'
                    
            Screen:
                name: 'screen2'                
                GridLayout:
                    cols:3
                    spacing:'0dp'
                    height: self.minimum_height
                    size_hint: 1, 1 
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    Label:
                        text: 'TELE-OP'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, 0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                                
                    Label:
                        text: 'GLYPHS SCORED'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'        

                    Button:
                        text: '-'
                        background_color: (.1, 1, 1, 0.7)
                        height: '30dp'
                        on_release: _glyphs.text = str(root.subtractParticle(*args))
                        on_release: _mainScore.text = str(root.subtractMain2(*args))
                                
                    Label:
                        id: _glyphs
                        text: '0'
                        color: 1,1,1,1
                                
                    Button:
                        text: '+'
                        background_color: (.1, 1, 1, 0.7)
                        on_release: _glyphs.text = str(root.addParticle(*args))
                        on_release: _mainScore.text = str(root.addMain2(*args))
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                                
                    Label:
                        text: 'ROWS COMPLETED'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                    Button:
                        text: '-'
                        background_color: (.1, 1, 1, .7)
                        on_release: _rowscompleted.text = str(root.subtractParticle2(*args))
                        on_release: _mainScore.text = str(root.subtractMain10(*args))
                        
                              
                    Label:
                        id: _rowscompleted
                        text: '0'
                        color: 1,1,1,1
                        
                    Button:
                        text: '+'
                        background_color: (.1, 1, 1, 0.7)
                        on_release: _rowscompleted.text = str(root.addParticle2(*args))
                        on_release: _mainScore.text = str(root.addMain10(*args))
                        
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                                
                    Label:
                        text: 'COLUMNS COMPLETED'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        
                    Button:
                        text: '-'
                        background_color: (.1, 1, 1, 0.7)
                        on_release: _colscompleted.text = str(root.subtractParticle3(*args))
                        on_release: _mainScore.text = str(root.subtractMain20(*args))

                    Label:
                        id: _colscompleted
                        text: '0'
                        color: 1,1,1,1
                                
                    Button:
                        text: '+'
                        background_color: (.1, 1, 1, 0.7)
                        on_release: _colscompleted.text = str(root.addParticle3(*args))
                        on_release: _mainScore.text = str(root.addMain20(*args))
                                
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,.5
                        height: '20dp'
                        
                    Label:
                        size_hint: 1,.5
                        height: '20dp'
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,.5
                        height: '20dp'

                    Label:
                        text: 'TIMER (sec):'

                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    Button:
                        id: _startButton2
                        text: 'START'
                        background_color: (.8,0,0,1) 
                        size_hint: 1,None
                        height: '30dp'
                        on_release: 
                            _clockTwo.start2()
                            _startButton2.text = str(root.timerStatus(*args))
                    
                    IncrediblyCrudeClock:
                        id: _clockTwo
                        size_hint: 1, None
                        height: '30dp'
                        text: '120'

                        
            Screen:
                name: 'screen3'
                GridLayout:
                    cols:3
                    spacing:'2dp'
                    height: self.minimum_height
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    Label:
                        text: 'ENDGAME'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, 0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        text: 'RELIC?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.3
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    
                    ToggleButton:
                        id: relicOne
                        size_hint_y: None
                        text: 'ZONE 1'
                        height: '30dp'
                        group: 'g7'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive3(*args))
                    
                    ToggleButton:
                        id: relicTwo
                        size_hint_y: None
                        text: 'ZONE 2'
                        height: '30dp'
                        group: 'g7'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive6(*args))
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                    ToggleButton:
                        id: relicThree
                        size_hint_y: None
                        text: 'ZONE 3'
                        height: '30dp'
                        group: 'g7'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive7(*args))
                    
                    ToggleButton:
                        id: upRight
                        size_hint_y: None
                        text: 'UPRIGHT'
                        height: '30dp'
                        group: 'g8'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive4(*args))
                    
                    Label:
                        text: 'ALLIANCE?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.3
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    
                    ToggleButton:
                        id: relicOne2
                        size_hint_y: None
                        text: 'ZONE 1'
                        height: '30dp'
                        group: 'g17'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive3(*args))
                    
                    ToggleButton:
                        id: relicTwo2
                        size_hint_y: None
                        text: 'ZONE 2'
                        height: '30dp'
                        group: 'g17'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive6(*args))
                        
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    ToggleButton:
                        id: relicThree2
                        size_hint_y: None
                        text: 'ZONE 3'
                        height: '30dp'
                        group: 'g17'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive7(*args))
                    
                    ToggleButton:
                        id: upRight2
                        size_hint_y: None
                        text: 'UPRIGHT'
                        height: '30dp'
                        group: 'g18'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive4(*args))
                        
                    Label:
                        text: 'CIPHER?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, .6
                            Rectangle:
                                pos:self.pos
                                size:self.size

                    ToggleButton:
                        id: completeOne
                        size_hint_y: None
                        text: '1 COMPLETE'
                        height: '30dp'
                        group: 'g6'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive2(*args))
                        
                    ToggleButton:
                        id: completeTwo
                        size_hint_y: None
                        height: '30dp'
                        text: '2 COMPLETE'
                        group: 'g6'
                        background_color: (.1, 1, 1, 0.7)
                        on_state: _mainScore.text = str(root.checkActive5(*args))

                        
                    Label:
                        text: 'BALANCED?'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8,.9
                            Rectangle:
                                pos:self.pos
                                size:self.size

                    ToggleButton:
                        id: balanced
                        size_hint_y: None
                        text: 'TEAM'
                        height: '30dp'
                        group: 'g3'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive6(*args))
                    
                    ToggleButton:
                        id: balanced2
                        size_hint_y: None
                        text: 'ALLIANCE'
                        height: '30dp'
                        group: 'g13'
                        background_color: (.1, 1, 1, .7)
                        on_state: _mainScore.text = str(root.checkActive6(*args))
                                            
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                        
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '30dp'
                    
                    Label:
                        size_hint: 1,None
                        height: '15dp'
                    Label:
                        size_hint: 1,None
                        height: '15dp'
                    Label:
                        text: 'TIMER (sec)'
                        size_hint: 1,None
                        height: '30dp'

                    Button:
                        id: _startButton3
                        text: 'START'
                        background_color: (.8,0,0,1) 
                        size_hint: 1,None
                        height: '30dp'
                        on_release: 
                            _clockThree.start()
                            _startButton3.text = str(root.timerStatus(*args))
                    
                    IncrediblyCrudeClock:
                        id: _clockThree
                        size_hint: 1, None
                        height: '30dp'
                        text: '30'

                        
            Screen:
                name: 'screen4'                
                GridLayout:
                    cols:1
                    spacing:'2dp'
                    height: self.minimum_height
                    
                    Label:
                        text: 'BROUGHT TO YOU BY'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '15dp'
                    
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, 0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    
                    Label:
                        text: 'FTC TEAM #6325 THE ALUMINATI'
                        color: 1,1,1,1
                        size_hint: 1,None
                        height: '15dp'
                    
                        canvas.before:
                            Color:
                                rgba: 0,0.4,.8, 0
                            Rectangle:
                                pos:self.pos
                                size:self.size
                    Label:
                        text: ''
                        color: 1,1,1,1
                        size_hint: 1, None
                        height: '10dp'

                    Button:
                        text: 'FACEBOOK'
                        background_color: (.1, .8, 1, 0.7)
                        on_release: 
                            import webbrowser
                            webbrowser.open('https://www.facebook.com/walnutrobotics/')

                    Button:
                        text: 'WORDPRESS'
                        background_color: (.1, .8, 1, 0.7)
                        on_release: 
                            import webbrowser
                            webbrowser.open('https://walnutrobotics.wordpress.com/')
  
                    Button:
                        text: 'TWITTER'
                        background_color: (.1, .8, 1, 0.7)
                        on_release: 
                            import webbrowser
                            webbrowser.open('https://twitter.com/walnutrobotics')
                        
                    Button:
                        text: 'INSTAGRAM'
                        background_color: (.1, .8, 1, 0.7)
                        on_release: 
                            import webbrowser
                            webbrowser.open('www.instagram.com/walnutrobotics')
                                 
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
                        
        GridLayout:
            #orientation: 'horizontal'
            size_hint: 1, .15
            cols: 3
            
            Button:
                text: 'AUTONOMOUS'
                background_color: (0, .1, 1, 0.5)
                on_release: 
                    _screen_manager.current = 'screen1'
                    _clockTwo.stop()
                    _clockThree.stop()
                    _startButton.text = 'START'
                
            Button:
                text: 'TELE-OP'
                background_color: (0, .1, 1, 0.5)
                on_release: 
                    _screen_manager.current = 'screen2'
                    _clockOne.stop()
                    _clockThree.stop()
                    _startButton2.text = 'START'
            Button:
                text: 'ENDGAME'
                background_color: (0, .1, 1, 0.5)
                on_release: 
                    _screen_manager.current = 'screen3'
                    _clockOne.stop()
                    _clockTwo.stop()
                    _startButton3.text = 'START'
                         
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        GridLayout:
            cols: 3
            size_hint: 1, .15
            
            Label:
                text: 'FTC RELIC RECOVERY'
                color: 1,1,1,1
                size_hint: 6,1
                
                canvas.before:
                    Color:
                        rgb: 0,0.4,.8
                    Rectangle:
                        pos:self.pos
                        size:self.size
            Button:
                text: 'CLEAR'
                size_hint: 2,1
                background_color: (1,0,0,1) 
                on_release: 
                    _mainScore.text = str(root.clear(*args))
                    _rowscompleted.text = str(root.clear(*args))
                    _colscompleted.text = str(root.clear(*args))
                    _glyphs.text = str(root.clear(*args))
                    scoredYes.state = 'normal'
                    scoredYes2.state = 'normal'
                    glyph.state = 'normal'
                    glyph2.state = 'normal'
                    usedKey.state = 'normal'
                    usedKey2.state = 'normal'
                    parked.state = 'normal'
                    parked2.state = 'normal'
                    balanced.state = 'normal'
                    balanced2.state = 'normal'
                    completeOne.state = 'normal'
                    completeTwo.state = 'normal'
                    relicOne.state = 'normal'
                    relicOne2.state = 'normal'
                    relicTwo.state = 'normal'
                    relicTwo2.state = 'normal'
                    relicThree.state = 'normal'
                    relicThree2.state = 'normal'
                    upRight.state = 'normal'
                    upRight2.state = 'normal'
                
                canvas.before:
                    Color:
                        rgb: .7,0,0,1
                    Rectangle:
                        pos:self.pos
                        size:self.size
                        
            Button:
                text: 'ABOUT'
                background_color: (1,0,0,1) 
                size_hint: 2,1
                on_release: _screen_manager.current = 'screen4'
                
                canvas.before:
                    Color:
                        rgb: .7,0,0,1
                    Rectangle:
                        pos:self.pos
                        size:self.size
                
            
            Label:
                text: 'SCORE KEEPER'
                size_hint: 1,1
                
                color: 1,1,1,1
                
                canvas.before:
                    Color:
                        rgb: 0,.4,.8
                    Rectangle:
                        pos:self.pos
                        size:self.size

            Label:
                text: 'SCORE: '
                size_hint: 1,1
                
                color: 1,1,1,1
                
                canvas.before:
                    Color:
                        rgb: 0,.4,.51
                    Rectangle:
                        pos:self.pos
                        size:self.size

            Label:
                id: _mainScore
                text: '0'
                size_hint: 1,1
                
                color: 1,1,1,1
                
                canvas.before:
                    Color:
                        rgb: 0,.4,.51
                    Rectangle:
                        pos:self.pos
                        size:self.size
                   
            """)


class IncrediblyCrudeClock(Label):
    a = NumericProperty(30)  # seconds
    b = NumericProperty(120)

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)
        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "FINISHED"
        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def start2(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(b=0, duration=self.b)
        def finish_callback(animation, incr_crude_clock):
                incr_crude_clock.text = "FINISHED"

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def stop(self):
        Animation.cancel_all(self)

    def reset(self):
        def finish_reset(animation, incr_crude_clock,progression):
            self.a = 30
            self.b = 120
        self.anim.bind(on_progress=finish_reset)

    def resetTime(self):
        def finish_reset(animation, incr_crude_clock):
            self.a = 30
            self.b = 120
        self.anim.bind(on_complete=finish_reset)


    def on_a(self, instance, value):
        self.text = str(round(value, 1))

    def on_b(self, instance, value):
        self.text = str(round(value, 1))

class Calc(FloatLayout):

    def addParticle(self, instance):
        try:
            score = (int(self.parts) + 1)
            self.parts = score
            return score

        except ValueError:
            return "Error"

    def subtractParticle(self, instance):
        try:
            if (int(self.parts) > 0):
                particles = (int(self.parts) - 1)
                self.parts = particles
                return particles
            else:
                self.parts = 0
                particles = 0
                return particles

        except ValueError:
            return "Error"

    def addParticle2(self, instance):
        try:
            particles = (int(self.parts2) + 1)
            self.parts2 = particles
            return particles

        except ValueError:
            return "Error"

    def addParticle3(self, instance):
        try:
            particles = (int(self.parts3) + 1)
            self.parts3 = particles
            return particles

        except ValueError:
            return "Error"

    def subtractParticle2(self, instance):
        try:
            if (int(self.parts2) > 0):
                particles = (int(self.parts2) - 1)
                self.parts2 = particles
                return particles
            else:
                self.parts2 = 0
                particles = 0
                return particles

        except ValueError:
            return "Error"

    def subtractParticle2(self, instance):
        try:
            if (int(self.parts2) > 0):
                particles = (int(self.parts2) - 1)
                self.parts2 = particles
                return particles
            else:
                self.parts2 = 0
                particles = 0
                return particles

        except ValueError:
            return "Error"

    def subtractParticle3(self, instance):
        try:
            if (int(self.parts3) > 0):
                particles = (int(self.parts3) - 1)
                self.parts3 = particles
                return particles
            else:
                self.parts3 = 0
                particles = 0
                return particles

        except ValueError:
            return "Error"

    def addMain20(self, instance):
        try:
            score = (int(self.mainScore) + 20)
            self.mainScore = score
            return score

        except ValueError:
            return "Error"


    def addMain10(self, instance):
        try:
            score = (int(self.mainScore) + 10)
            self.mainScore = score
            return score

        except ValueError:
            return "Error"

    def addMain2(self, instance):
        try:
            score = (int(self.mainScore) + 2)
            self.mainScore = score
            return score

        except ValueError:
            return "Error"

    def subtractMain2(self,instance):
        try:
            if int(self.mainScore) > 0 and int(self.parts) > 0:
                score = (int(self.mainScore) - 2)
                self.mainScore = score
                return score
            else:
                if self.parts <= 0 and self.parts2 <= 0:
                    score = 0
                    return score

        except ValueError:
            return "Error"

    def subtractMain10(self,instance):
        try:
            if int(self.mainScore) > 0 and int(self.parts2) > 0:
                score = (int(self.mainScore) - 10)
                self.mainScore = score
                return score
            else:
                if self.parts <= 0 and self.parts2 <= 0:
                    score = 0
                    return score

        except ValueError:
            return "Error"

    def subtractMain20(self,instance):
        try:
            if int(self.mainScore) > 0 and int(self.parts2) > 0:
                score = (int(self.mainScore) - 20)
                self.mainScore = score
                return score
            else:
                if self.parts <= 0 and self.parts2 <= 0:
                    score = 0
                    return score

        except ValueError:
            return "Error"

    def checkActive1(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 15)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 15)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore


    def checkActive2(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 30)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 30)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def checkActive3(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 10)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 10)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def checkActive4(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 15)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 15)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def checkActive5(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 60)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 60)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def checkActive6(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 20)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 20)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def checkActive7(self, widget, value):
        if value == 'down':
            score = (int(self.mainScore) + 40)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        if value == 'normal' and self.mainScore != 0:
            score = (int(self.mainScore) - 40)
            self.mainScore = score
            if score < 0:
                self.mainScore = 0
        return self.mainScore

    def clear(self, instance):
        self.clockOne.start()
        self.clockTwo.start2()
        self.clockThree.start()
        self.startButton.text = 'START'
        self.startButton2.text = 'START'
        self.startButton3.text = 'START'
        self.clockOne.reset()
        self.clockTwo.reset()
        self.clockThree.reset()
        self.clockOne.resetTime()
        self.clockTwo.resetTime()
        self.clockThree.resetTime()
        self.mainScore = 0
        self.parts = 0
        self.parts2 = 0
        self.parts3 = 0
        self.isActive = False

        return self.mainScore

    def timerStatus(self,instance):
        buttonLabel = 'START'
        if (self.isActive == True):
            buttonLabel = 'START'
            self.isActive = False
            self.clockOne.stop()
            self.clockTwo.stop()
            self.clockThree.stop()
        else:
            if (self.isActive == False):
                buttonLabel = 'STOP'
                self.isActive = True
        return buttonLabel





class Project(App):
    def build(self):
        return Calc()


if __name__ == "__main__":
    Project().run()