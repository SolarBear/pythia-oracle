'''

==============

Pythia-Oracle 1.4.0

The MIT License (MIT)
Copyright (c) 2016 exposit

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

import kivy
#from kivy.properties import NumericProperty, ListProperty
kivy.require('1.8.0')

import config

if config.debug == False:
    kivy.config.Config.set('kivy', 'log_level', 'critical' )

# override kivy config values -- graphics
kivy.config.Config.set ( 'graphics', 'width', 1280 )
kivy.config.Config.set ( 'graphics', 'height', 725 )
kivy.config.Config.set ( 'graphics', 'resizable', 0)
kivy.config.Config.set ( 'graphics', 'multisamples', 4)

# uncomment the next line and comment out the previous four if you want fullscreen
#kivy.config.Config.set ( 'graphics', 'fullscreen', 'auto')

# override kivy config values -- misc
kivy.config.Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
kivy.config.Config.set('kivy', 'exit_on_escape', '1')


from imports import *
from main import MainScreen

# and a font register for any user defined fonts
for font in config.fonts:
    LabelBase.register(**font)

# and set the clock iterations high because we're making a LOT of widgets
Clock.max_iteration = 80

class TitleScreen(Screen):

    def __init__ (self,**kwargs):
        super (TitleScreen, self).__init__(**kwargs)

        # super().__init__(**kwargs)

        Builder.load_file('style.kv')

        Window.clearcolor = (neutral[0]*.75, neutral[1]*.75, neutral[2]*.75,1)
        #Window.clearcolor = neutral

        #texture = ObjectProperty()

        self.texture = Image(source='resources' + os.sep + 'bg_title' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_1.png').texture
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (4, 4)

        with self.canvas:
            Rectangle(pos=(0,0), size=Window.size, texture=self.texture)

        self.mainAnchor = AnchorLayout(anchor_x='center', anchor_y='center')

        # first thing, try to open styles
        try:
            with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_game.txt", "r") as curr_file:
                gamename = curr_file.read()
                config.curr_game_dir = "." + os.sep + "saves" + os.sep + gamename.strip() + os.sep
        except:
            pass

        # why is this even being opened?
        try:
            with open(config.curr_game_dir + "config.txt", "r") as config_file:
                tempDict = json.load(config_file)
                config.general['pretitle'] = tempDict['general']['pretitle']
                config.general['posttitle'] = tempDict['general']['posttitle']
        except:
            pass

        self.mainBox = BoxLayout(orientation='vertical', size_hint_x=.8, size_hint_y=.6, spacing=20)

        #self.preTitleLabel = TextInput(text=config.general['pretitle'], font_size=22, font_name='titlefancyfont', background_color=(0,0,0,0), foreground_color=(1,1,1,1),  padding=(300,0))

        self.preTitleLabel = Label(text=config.general['pretitle'], font_size="36dp", font_name='titlefont', halign="center")

        self.currentLabel = Label(text=string.capwords(config.curr_game_dir.split(os.sep)[-2]), font_size="36dp", font_name='titlefont', halign="center")

        self.postTitleLabel = Label(text=config.general['posttitle'], font_size="36dp", font_name='titlefont', halign="center")

        #self.postTitleLabel = TextInput(text=config.general['posttitle'], font_size="22dp", font_name='titlefancyfont', background_color=(0,0,0,0), foreground_color=(1,1,1,1), padding=(300,0))

        self.startButton = Button(text="Start", font_name='titlefont', font_size="20dp")
        self.startButton.bind(on_press=self.pressGenericButton)
        self.startButton.bind(on_release=self.releaseStart)

        palettes = []

        for item in styles.palette:
            palettes.append(styles.palette[item]['name'])

        self.paletteSpinner = Spinner(
            text=styles.curr_palette['name'],
            values=palettes,
            background_normal='',
            background_color=neutral,
            background_down='',
            background_color_down=accent2,
            size_hint=(.5, 1),
            font_name='titlefont',
            font_size="14dp",
            )

        self.paletteSpinner.bind(text=self.changePalette)

        self.loadButton = Button(text="Load", font_name='titlefont', font_size="16dp")
        self.loadButton.bind(on_press=self.pressGenericButton)
        self.loadButton.bind(on_release=self.releaseLoad)

        self.newButton = Button(text="New Game", font_name='titlefont', font_size="16dp")
        self.newButton.bind(on_press=self.pressGenericButton)
        self.newButton.bind(on_release=self.newGame)

        self.newScenarioButton = Button(text="New Game", font_name='titlefont', font_size="16dp")
        self.newScenarioButton.bind(on_press=self.pressGenericButton)
        self.newScenarioButton.bind(on_release=self.newGameScenario)

        self.aboutButton = Button(text="About", font_name='titlefont', font_size="16dp")
        self.aboutButton.bind(on_press=self.pressGenericButton)
        self.aboutButton.bind(on_release=self.showAbout)

        self.mainBox.add_widget(self.preTitleLabel)
        self.mainBox.add_widget(self.currentLabel)
        self.mainBox.add_widget(self.postTitleLabel)
        self.mainBox.add_widget(Label(text=""))
        self.mainBox.add_widget(self.startButton)
        self.mainBox.add_widget(self.loadButton)
        self.mainBox.add_widget(self.newScenarioButton)
        self.mainBox.add_widget(self.aboutButton)

        self.paletteBox = BoxLayout(orientation='horizontal')
        self.paletteBox.add_widget(self.paletteSpinner)
        self.paletteSample = Image(source="." + os.sep + "resources" + os.sep + "bg_sample" + os.sep + str(styles.curr_palette['name']).replace (" ", "_") + ".png", allow_stretch=True, keep_ratio=False, size_hint=(.5,1))
        self.paletteBox.add_widget(self.paletteSample)

        self.mainBox.add_widget(self.paletteBox)

        self.mainAnchor.add_widget(self.mainBox)

        self.add_widget(self.mainAnchor)

        #--- Under this is popups

        saves = glob.glob("." + os.sep + "saves" + os.sep + "*" + os.sep)

        self.savesBox = BoxLayout(orientation="vertical")
        for savefolder in saves:
            timestamp = " (%s)" % time.ctime(os.path.getmtime(savefolder + "main.txt"))
            title = savefolder.split(os.sep)[-2]
            if title == "quicksave":
                gamename = title + " " + timestamp
            else:
                try:
                    with open(savefolder + "config.txt", "r") as config_file:
                        tempDict = json.load(config_file)
                        pre = tempDict['general']['pretitle'].replace('\n', ' ')
                        post = tempDict['general']['posttitle'].replace('\n', ' ')
                except:
                    pre = ""
                    post = ""
                gamename = pre + " " + title + " " + post + timestamp
            btn = Button(text=gamename, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='maintextfont')
            btn.game = savefolder
            self.savesBox.add_widget(btn)
            btn.bind(on_release=self.choseGameToLoad)
            btn.bind(on_press=self.pressGenericButton)

        self.savesPopup = Popup(title='Saves',
            content=self.savesBox,
            size_hint=(.5, .5),
            auto_dismiss=True)

        self.newGameBox = BoxLayout(orientation="vertical")
        self.newGameNameInput = TextInput(text="", multiline=False)
        self.newGameBox.add_widget(self.newGameNameInput)

        self.newGameStatus = Label(text="Enter a new name.")
        self.newGameBox.add_widget(self.newGameStatus)

        btn = Button(text="Confirm", size_hint=(1,1), font_name='titlefont')
        self.newGameBox.add_widget(btn)
        btn.bind(on_release=self.makeNewGame)
        btn.bind(on_press=self.pressGenericButton)

        self.newGamePopup = Popup(title='New Game',
            content=self.newGameBox,
            size_hint=(None, None), size=("400dp", "400dp"),
            auto_dismiss=True)

        # make a new game with a scenario
        available_scenarios = glob.glob("." + os.sep + "resources" + os.sep + "scenarios" + os.sep + "*" + os.sep)

        self.scenariosBox = BoxLayout(orientation="vertical")
        for modfolder in available_scenarios:
            modname = modfolder.split(os.sep)[-2]
            btn = Button(text=modname, size_hint=(1,1))
            btn.scenario = modfolder
            self.scenariosBox.add_widget(btn)
            btn.bind(on_release=self.choseScenarioToLoad)
            btn.bind(on_press=self.pressGenericButton)

        btn = Button(text="Blank Template (No Scenario)", size_hint=(1,1))
        btn.scenario = "None"
        self.scenariosBox.add_widget(btn)
        btn.bind(on_release=self.choseNoScenarioToLoad)
        btn.bind(on_press=self.pressGenericButton)

        self.scenariosPopup = Popup(title='Scenarios',
            content=self.scenariosBox,
            size_hint=(.5, .5),
            auto_dismiss=False)

        self.newModGameBox = BoxLayout(orientation="vertical")
        self.newModGameNameInput = TextInput(text="", multiline=False)
        self.newModGameBox.add_widget(self.newModGameNameInput)

        self.newModGameStatus = Label(text="Enter a new name.")
        self.newModGameBox.add_widget(self.newModGameStatus)

        btn = Button(text="Confirm", size_hint=(1,1))
        self.newModGameBox.add_widget(btn)
        btn.bind(on_release=self.makeNewModGame)
        btn.bind(on_press=self.pressGenericButton)

        self.newModGamePopup = Popup(title='New Game with Scenario',
            content=self.newModGameBox,
            size_hint=(.3, .3),
            auto_dismiss=True)

        # aboutBox popup
        self.aboutBox = GridLayout(cols=1, padding=(10,10))

        self.AboutPopup = Popup(title='About',
            content=self.aboutBox,
            size_hint=(.5, .7),
            auto_dismiss=True)

        text = []
        text.append("Make a new game, push buttons, enter text, push more buttons, let me know if anything crashes. Back up your save folder frequently in case of boom. Have fun!")
        text.append("")
        text.append("Drama chart & How's It Going rolls from Joel Priddy @ http://abominablefancy.blogspot.com; go there for more neat stuff!")
        text.append("")
        text.append("The FU oracle is based on FU: The Freeform/Universal RPG (found at http://nathanrussell.net/fu), by Nathan Russell, and licensed for our use under the Creative Commons Attribution 3.0 Unported license (http://creativecommons.org/licenses/by/3.0/).")
        text.append("")
        text.append("The Mythic GM Emulator is used with permission of the author under a non-commercial clause.")
        text.append("")
        text.append("The Conundrum and And/But Clarifier generators are from Abulafia (found at http://www.random-generator.com/) and licensed under the Creative Commons Attribution 2.5 Generic license (http://creativecommons.org/licenses/by/2.5/).")
        text.append("")
        text.append("Pythia (this program) is licensed under MIT.\nGithub (user name exposit, repo pythia-oracle) for more information.")
        for entry in text:
            label = Label(text=entry)
            label.size = label.texture_size
            label.text_size = (self.aboutBox.width,None)
            self.aboutBox.add_widget(label)
            label.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))

    def showAbout(self, *args):
        self.aboutButton.background_color = neutral
        self.AboutPopup.open()

    def releaseStart(self, *args):
        self.startButton.background_color = accent1
        if os.path.exists(config.curr_game_dir):
            self.manager.transition = SlideTransition(duration=1,clearcolor=(primary[0], primary[1], primary[2], 1), direction="up")
            self.manager.current = 'mainscn'
            # now update so the last opened game will be opened again next time
            config.curr_game_dir = config.curr_game_dir.strip()
            try:
                with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_game.txt", "w") as config_file:
                    gamename = config.curr_game_dir.split(os.sep)[-2]
                    config_file.write(gamename)
                    EventLoop.window.title = "Pythia-Oracle -- " + gamename
            except:
                pass
        else:
            self.newGamePopup.open()
            self.newGameStatus.text = "no game loaded"

    def changePalette(self, *args):
        args[0].background_color = accent1
        self.paletteSample.source = "." + os.sep + "resources" + os.sep + "bg_sample" + os.sep + str(args[1]).replace (" ", "_") + ".png"
        for item in styles.palette:
            if styles.palette[item]['name'] == args[1]:
                try:
                    with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_palette.txt", "w") as config_file:
                        config_file.write(item)
                except:
                    pass

    def releaseLoad(self, *args):
         self.savesPopup.open()
         args[0].background_color = accent1

    def choseGameToLoad(self, *args):
        args[0].background_color = accent1
        title = args[0].game
        config.curr_game_dir = title
        self.savesPopup.dismiss()
        self.releaseStart()

    def choseNoScenarioToLoad(self, *args):
        args[0].background_color = accent1
        self.scenariosPopup.dismiss()
        self.newGamePopup.open()

    def choseScenarioToLoad(self, *args):
        args[0].background_color = accent1
        title = args[0].scenario
        config.curr_scenario = title
        self.scenariosPopup.dismiss()
        self.newModGamePopup.open()

    def newGame(self, *args):
        args[0].background_color = accent1
        self.newGamePopup.open()

    def makeNewGame(self, *args):
        args[0].background_color = accent1
        folder_name = self.newGameNameInput.text
        if folder_name == "":
            self.newGamePopup.dismiss()

        try:
            newpath = '.' + os.sep + 'saves' + os.sep + folder_name + os.sep
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                os.makedirs(newpath + "logs")
            else:
                self.newGameStatus.text = "Folder exists."
                return

            f = file(newpath + "main.txt", "w")
            #f = file(newpath + "main_status.txt", "w")
            f = file(newpath + "threads.txt", "w")
            #f = file(newpath + "threads_status.txt", "w")
            f = file(newpath + "actors.txt", "w")
            #f = file(newpath + "actors_status.txt", "w")
            f = file(newpath + "config.txt", "w")
            f = file(newpath + "tracks.txt", "w")
            f = file(newpath + "pcs.txt", "w")
            f = file(newpath + "maps.txt", "w")

            config.curr_game_dir = newpath

            config.general['pretitle'] = ' '
            config.general['posttitle'] = ' '

            saveconfig(self, config.curr_game_dir)

        except:

            print("[makeNewGame] Couldn't make a new directory for some reason.")

        self.newGamePopup.dismiss()
        self.releaseStart()

    def newGameScenario(self, *args):
        args[0].background_color = accent1
        self.scenariosPopup.open()

    def makeNewModGame(self, *args):

        args[0].background_color = accent1
        folder_name = self.newModGameNameInput.text
        if folder_name == "":
            self.newModGamePopup.dismiss()

        #try:
        newpath = '.' + os.sep + 'saves' + os.sep + folder_name + os.sep
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            os.makedirs(newpath + "logs")
        else:
            self.newModGameStatus.text = "Folder exists."
            return

        #fileList = [ "main.txt", "main_status.txt", "threads.txt", "threads_status.txt", "actors.txt", "actors_status.txt", "tracks.txt", "pcs.txt", "maps.txt", "scenario.txt", "scenlogic.py", "scenpanel.py" ]

        fileList = [ "main.txt", "threads.txt", "actors.txt", "tracks.txt", "pcs.txt", "maps.txt", "scenario.txt", "scenlogic.py", "scenpanel.py" ]

        config.curr_game_dir = newpath

        for item in fileList:
            f = file(newpath + item, "w")
            try:
                with open(config.curr_scenario + item) as fi:
                    lines = fi.readlines()
                    with open(newpath + item, "w") as fum:
                        fum.writelines(lines)
            except:
                pass

        # now parse the config and save as a config
        mod = config.curr_scenario + "scenconfig.py"
        filename = mod.split('/')[-1]
        pyfile = filename.split('.')[0]
        modconfig = imp.load_source( pyfile, mod)

        tempDict = {}
        # this should likely be switched over to entirely pull from the scenario
        tempDict['general'] = config.general
        tempDict['user'] = config.user
        tempDict['formats'] = config.formats
        tempDict['scenario'] = modconfig.scenario
        with open(newpath + 'config.txt', "w") as fum:
            json.dump(tempDict, fum)

        loadconfig(self, config.curr_game_dir)

        #except:
        #    print("[makeNewModGame] Couldn't make a new directory for some reason.")

        self.newModGamePopup.dismiss()
        self.releaseStart()

    def pressGenericButton(self, *args):
        args[0].background_color = accent2


class PythiaOracleApp(App):

    def build(self):

        self.title = 'Pythia-Oracle'

        #Window.clearcolor = (1, 1, 1, 1)

        global root
        root = self

        # define colors used in style.kv here; is there a way to change this without restart?
        #self.accent1_r = accent1[0]
        #self.accent1_g = accent1[1]
        #self.accent1_b = accent1[2]
        self.basefont = config.basefont
        self.neutral = styles.neutral
        self.accent1 = styles.accent1
        self.accent2 = styles.accent2
        self.textcolor = styles.textcolor

        self.screenmanager = ScreenManager()
        self.screenmanager.transition = SlideTransition(duration=1, clearcolor=(primary[0], primary[1], primary[2], 1), direction="left")
        titlescn = TitleScreen(name='titlescn')
        mainscn = MainScreen(name='mainscn')
        self.screenmanager.add_widget(titlescn)
        self.screenmanager.add_widget(mainscn)

        #return Builder.load_string(kv)

        return self.screenmanager

    def on_start(self):
        #print("APP STARTING")
        if "app_start" in config.backup_behavior:
            makeBackup("s")

    def on_stop(self):
        #print("APP STOPPING")
        if self.screenmanager.current == 'mainscn':
            # save things
            quicksave(self, config.curr_game_dir)
            # make logs
            for i in imports.log_template:
                methodToCall = getattr( i, 'makeLogFile' )
                methodToCall(self)
        if "app_exit" in config.backup_behavior:
            makeBackup("e")

if __name__ == '__main__':
    PythiaOracleApp().run()
