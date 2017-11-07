#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Main Screen
#
##---------------------------------------------------------------------------------------

from imports import *
import config

class MainScreen(Screen):

    def __init__(self,**kwargs):
        super (MainScreen, self).__init__(**kwargs)

##---------------------------------------------------------------------------------------
#  general
##---------------------------------------------------------------------------------------

        # set background; to have no background, delete or move the background images

        #try:
        #    self.texture = Image(source='resources/bg_main/' + styles.curr_palette["name"].replace (" ", "_") + '_5.png').texture
        #    self.texture.wrap = 'repeat'
        #    self.texture.uvsize = (4, 4)

        #    with self.canvas:
        #        Rectangle(pos=(0,0), size=Window.size, texture=self.texture)
        #except:
        #    pass

        self.mainBox = BoxLayout(orientation="horizontal")
        self.add_widget(self.mainBox)

        # comment this out to return to default text input behavior, ie, enter while focused on main textinput does nothing
        Window.bind(on_key_down=self.key_action)

        #Button.background_down=""

##---------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack
##---------------------------------------------------------------------------------------

        self.leftAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space = config.aiheight)
        self.mainBox.add_widget(self.leftAccordion)

##---------------------------------------------------------------------------------------
#  Center status across top
##---------------------------------------------------------------------------------------

        self.centerBox = BoxLayout(orientation='vertical', padding=(10,10))

        self.statusBox = BoxLayout(orientation='horizontal', size_hint=(1,.10), padding=(10,10))

        self.trackBox = BoxLayout(orientation="horizontal", size_hint=(.25,1))

        self.trackDownButton = Button(text="-", size_hint=(.3,1))
        self.trackDownButton.bind(on_press=self.pressGenericButton)
        self.trackDownButton.bind(on_release=self.releaseTrackerDown)
        self.trackBox.add_widget(self.trackDownButton)

        self.trackLabel = Label(text="0", size_hint=(.3,1))
        self.trackBox.add_widget(self.trackLabel)

        self.trackUpButton = Button(text="+", size_hint=(.3,1))
        self.trackUpButton.bind(on_press=self.pressGenericButton)
        self.trackUpButton.bind(on_release=self.releaseTrackerUp)
        self.trackBox.add_widget(self.trackUpButton)

        self.statusBox.add_widget(self.trackBox)

        self.bookmarkBox = BoxLayout(orientation="horizontal", size_hint=(.75,1))
        for i in range(0,5):
            btn = ToggleButton(text="-", group='bookmarks', font_size=config.basefont, size_hint=(1,1), background_color=neutral, font_name='maintextfont', allow_no_selection=True)
            btn.bind(on_press=self.toggledBookmark)
            btn.value = i
            btn.index = -9
            self.bookmarkBox.add_widget(btn)

        self.clearBookmarkButton = ToggleButton(text="Clear", group='clear', font_size=config.basefont90, size_hint=(1,1), background_color=neutral, font_name='maintextfont', allow_no_selection=True)
        self.bookmarkBox.add_widget(self.clearBookmarkButton)
        self.clearBookmarkButton.bind(on_press=self.pressGenericButton)

        self.statusBox.add_widget(self.bookmarkBox)

        self.mechanicsButton = Button(text="PROSE", font_size=config.basefont90, size_hint=(.15,1), background_color=neutral, font_name='maintextfont')
        self.statusBox.add_widget(self.mechanicsButton)
        self.mechanicsButton.bind(on_press=self.pressGenericButton)
        self.mechanicsButton.bind(on_release=hideMechanicsBlocks)
        self.mechanicsButton.self = self

        try:
            enterBehaviorList = config.formats['status_tags']
        except:
            enterBehaviorList = ['plain', 'aside', 'oracle', 'result', 'query', 'mechanic1', 'mechanic2', 'ephemeral']
        enterBehaviorList = enterBehaviorList + ["None"]

        self.enterSpinner = Spinner(
            # default value shown
            text='plain',
            # available values
            values=enterBehaviorList,
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            font_size=config.basefont90,
            size_hint=(.2, 1),
            )

        self.enterSpinner.bind(text=self.toggleEnterBehavior)
        self.statusBox.add_widget(self.enterSpinner)

        self.centerBox.add_widget(self.statusBox)

##---------------------------------------------------------------------------------------
#  Center text display
##---------------------------------------------------------------------------------------

        #self.centerBox.add_widget(Label(text="---------------------", color=styles.textcolor, size_hint=(1,.04), font_name="maintextfont", font_size=config.basefont ))

        self.threadButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.03), font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyThreadsToMain)
        self.threadButtonBox.add_widget(self.button)

        self.randomThreadButton = Button(text="random thread", halign='center', font_size=config.basefont75)
        self.randomThreadButton.bind(on_press=self.pressGenericButton)
        self.randomThreadButton.bind(on_release=self.releaseRandomThread)
        self.threadButtonBox.add_widget(self.randomThreadButton)

        self.centerBox.add_widget(self.threadButtonBox)

        self.threadDisplay = ScrollView(size_hint=(1,.30))

        self.threadDisplayGrid = GridLayout(cols=2, spacing=10, size_hint_y=None, size_hint_x=1,  padding=(10,10))
        self.threadDisplayGrid.bind(minimum_height = self.threadDisplayGrid.setter('height'))

        self.threadDisplay.add_widget(self.threadDisplayGrid)

        self.centerBox.add_widget(self.threadDisplay)

        #self.centerBox.add_widget(Label(text="---------------------", color=styles.textcolor, size_hint=(1,.04), font_name="maintextfont", font_size=config.basefont ))

        self.titleBarBox = BoxLayout(orientation='horizontal', size_hint=(1,.05))

        self.jumpButton = Button(text="top", size_hint=(1,1), font_size=config.basefont75)
        self.jumpButton.bind(on_press=self.pressGenericButton)
        self.jumpButton.bind(on_release=self.navJump)
        self.titleBarBox.add_widget(self.jumpButton)

        self.findButton = Button(text="find", size_hint=(1,1), font_size=config.basefont75)
        self.findButton.bind(on_press=self.pressGenericButton)
        self.findButton.bind(on_release=self.navFind)
        self.titleBarBox.add_widget(self.findButton)

        self.nextButton = Button(text="next", size_hint=(1,1), font_size=config.basefont75)
        self.nextButton.bind(on_press=self.pressGenericButton)
        self.nextButton.bind(on_release=self.navNext)
        self.titleBarBox.add_widget(self.nextButton)

        self.centerBox.add_widget(self.titleBarBox)

        self.centerDisplay = ScrollView(size_hint=(1,1))

        self.centerDisplayGrid = GridLayout(cols=1, size_hint_y=None, padding=20, spacing="20dp")

        self.centerDisplayGrid.bind(minimum_height = self.centerDisplayGrid.setter('height'))

        self.centerDisplay.add_widget(self.centerDisplayGrid)

        self.centerBox.add_widget(self.centerDisplay)

##---------------------------------------------------------------------------------------
#  main text input & control panel
##---------------------------------------------------------------------------------------

        self.controlBox = BoxLayout(orientation='horizontal', size_hint=(1,.45))

        self.textInputMainBox = BoxLayout(orientation='vertical')

        self.textInput = TextInput(text='', hint_text="", size_hint=(1,1), font_size=config.maintextinputfont)
        #self.textInput.bind(on_text_validate=self.text_entered)
        self.textInputMainBox.add_widget(self.textInput)

##---------------------------------------------------------------------------------------
#  center footerself.box
##---------------------------------------------------------------------------------------

        self.footerBox = BoxLayout(orientation="horizontal")

        # flags & toggles
        self.oracleButton = Button(text=config.oracle)
        self.oracleButton.bind(on_release=self.cycleOracle)


        self.qualitiesButton = ToggleButton(text="DQ")
        self.qualitiesButton.bind(on_release=self.toggleResolutionMode)

        self.saveButton = Button(text="Save")
        self.saveButton.bind(on_press=self.pressGenericButton)
        self.saveButton.bind(on_release=self.releaseSave)

        #self.box for adding threads & actors
        self.threadSubmitButton = Button(text="Add\nThread", halign='center', size_hint=(1,1), font_size=config.basefont80)
        self.threadSubmitButton.bind(on_press=self.pressGenericButton)
        self.threadSubmitButton.bind(on_release=self.releaseThread)

        self.addActorButton = Button(text="Add\nActor", halign='center', size_hint=(1,1), font_size=config.basefont80)
        self.addActorButton.bind(on_press=self.pressGenericButton)
        self.addActorButton.bind(on_release=self.releaseAddActor)

        # pick one from a list
        self.listButton1 = Button(text="Pick\nOne", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton1.bind(on_press=self.pressGenericButton)
        self.listButton1.bind(on_release=self.chooseFromList)
        self.listButton1.value = 0

        self.listButton2 = Button(text="Pick\n2d4", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton2.bind(on_press=self.pressGenericButton)
        self.listButton2.bind(on_release=self.chooseFromList)
        self.listButton2.value = 1

        self.listButton3 = Button(text="Pick\n2d6", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton3.bind(on_press=self.pressGenericButton)
        self.listButton3.bind(on_release=self.chooseFromList)
        self.listButton3.value = 2

        self.listButton4 = Button(text="Pick\n3:2:1", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton4.bind(on_press=self.pressGenericButton)
        self.listButton4.bind(on_release=self.chooseFromList)
        self.listButton4.value = 3

        self.listButton5 = Button(text="Pick\nTwo", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton5.bind(on_press=self.pressGenericButton)
        self.listButton5.bind(on_release=self.chooseFromList)
        self.listButton5.value = 4

        self.listButton6 = Button(text="Pick\nThree", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton6.bind(on_press=self.pressGenericButton)
        self.listButton6.bind(on_release=self.chooseFromList)
        self.listButton6.value = 5

        self.listButton7 = Button(text="Pick\nFour", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton7.bind(on_press=self.pressGenericButton)
        self.listButton7.bind(on_release=self.chooseFromList)
        self.listButton7.value = 6

        self.listButton8 = Button(text="Pick\nFive", halign="center", font_size=config.basefont75, size_hint=(1,1), )
        self.listButton8.bind(on_press=self.pressGenericButton)
        self.listButton8.bind(on_release=self.chooseFromList)
        self.listButton8.value = 7

        # dice presets
        self.diceButtonsList = []

        for preset in config.dice_presets:

            if len(preset) > 4:
                self.button = Button(text=preset, font_size=config.basefont80)
            else:
                self.button = Button(text=preset)

            self.button.bind(on_press=self.pressGenericButton)
            self.button.bind(on_release=self.releasePresetDice)
            self.diceButtonsList.append(self.button)

        #diceList = ["4", "6", "8", "10", "12", "20", "30", "100"]
        diceSpinnersList = []

        for item in config.dice_spinner_list:
            diceValueList = []
            for i in range(1,11):
                diceValueList.append( str(i) + "d" + item )

            self.spinner = Spinner(
                # default value shown
                text=diceValueList[0],
                # available values
                values=diceValueList,
                background_normal='',
                background_color=neutral,
                background_down='',
                background_color_down=accent2,
                font_size=config.basefont90,
                )

            self.spinner.bind(text=self.releasePresetDice)
            diceSpinnersList.append(self.spinner)

        diceAltButtonsList = []
        self.button = Button(text="ORE")
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releaseORERoll)
        diceAltButtonsList.append(self.button)

        self.button = Button(text="FATE")
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.releaseFateRoll)
        diceAltButtonsList.append(self.button)

        self.flagsBox = BoxLayout(orientation='vertical', size_hint=(.1,1))
        self.flagsBox.add_widget(self.oracleButton)
        self.flagsBox.add_widget(self.qualitiesButton)
        self.flagsBox.add_widget(self.saveButton)

        self.threadBox = BoxLayout(orientation='vertical', size_hint=(.1,1))
        self.threadBox.add_widget(self.threadSubmitButton)
        self.threadBox.add_widget(self.addActorButton)

        self.weightedBox = GridLayout(cols=4, size_hint=(.3,1))
        self.weightedBox.add_widget(self.listButton1)
        self.weightedBox.add_widget(self.listButton5)
        self.weightedBox.add_widget(self.listButton6)
        self.weightedBox.add_widget(self.listButton7)
        self.weightedBox.add_widget(self.listButton8)
        self.weightedBox.add_widget(self.listButton2)
        self.weightedBox.add_widget(self.listButton3)
        self.weightedBox.add_widget(self.listButton4)

        self.dicePresetsBox = GridLayout(cols=4, size_hint=(.3,1))

        for dice in self.diceButtonsList:
            self.dicePresetsBox.add_widget(dice)

        self.diceSpinnersBox = GridLayout(cols=1, size_hint=(.1,1))

        for spinner in diceSpinnersList:
            self.diceSpinnersBox.add_widget(spinner)

        self.diceAltBox = GridLayout(cols=1, size_hint=(.1,1))
        for alt in diceAltButtonsList:
            self.diceAltBox.add_widget(alt)

        self.footerBox.add_widget(self.flagsBox)
        self.footerBox.add_widget(self.weightedBox)
        self.footerBox.add_widget(self.dicePresetsBox)
        self.footerBox.add_widget(self.diceSpinnersBox)
        self.footerBox.add_widget(self.diceAltBox)

        self.footerBox.add_widget(self.threadBox)
        self.textInputMainBox.add_widget(self.footerBox)

        self.controlBox.add_widget(self.textInputMainBox)

##---------------------------------------------------------------------------------------
#  Center text submit buttons
##---------------------------------------------------------------------------------------

        self.submitButtonsBox = BoxLayout(orientation='vertical', size_hint=(.23,1))

        self.questionSubmitButton = Button(text="???")
        self.questionSubmitButton.bind(on_press=self.pressGenericButton)
        self.questionSubmitButton.bind(on_release=self.releaseQuestion)
        self.submitButtonsBox.add_widget(self.questionSubmitButton)

        self.playerSubmitButton = Button(text="Direct")
        self.playerSubmitButton.bind(on_press=self.pressGenericButton)
        self.playerSubmitButton.bind(on_release=self.releasePlayer)
        self.submitButtonsBox.add_widget(self.playerSubmitButton)

        self.dmSubmitButton = Button(text="Aside")
        self.dmSubmitButton.bind(on_press=self.pressGenericButton)
        self.dmSubmitButton.bind(on_release=self.releaseDM)
        self.submitButtonsBox.add_widget(self.dmSubmitButton)

        self.rollSubmitButton = Button(text="Roll Dice")
        self.rollSubmitButton.bind(on_press=self.pressGenericButton)
        self.rollSubmitButton.bind(on_release=self.releaseRoll)
        self.submitButtonsBox.add_widget(self.rollSubmitButton)

        self.seedButtonsBox = BoxLayout(orientation='vertical', size_hint_y=2)

        self.seedButton = Button(text="Seed")
        self.seedButton.bind(on_press=self.pressGenericButton)
        self.seedButton.bind(on_release=self.getSeed)
        self.seedButtonsBox.add_widget(self.seedButton)

        self.seedAlternateButton = Button(text="Action")
        self.seedAlternateButton.bind(on_press=self.pressGenericButton)
        self.seedAlternateButton.bind(on_release=self.getSeedAlternate)
        self.seedButtonsBox.add_widget(self.seedAlternateButton)

        self.submitButtonsBox.add_widget(self.seedButtonsBox)

        # scenario buttons go here, if a scenario is loaded
        self.scenarioButtonList = []
        button = Button(text="show scene")
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=self.showBlock)
        self.scenarioButtonList.append(button)

        button = Button(text="show exits")
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=self.showExits)
        self.scenarioButtonList.append(button)

        self.controlBox.add_widget(self.submitButtonsBox)

        self.centerBox.add_widget(self.controlBox)

        self.mainBox.add_widget(self.centerBox)

##---------------------------------------------------------------------------------------
#  SIDE PANEL - right horizontal stack for trackers
##---------------------------------------------------------------------------------------

        self.rightAccordion = Accordion(orientation='horizontal', size_hint=(.6, 1), min_space = config.aiheight)
        self.mainBox.add_widget(self.rightAccordion)

##---------------------------------------------------------------------------------------
#  PC panel
##---------------------------------------------------------------------------------------

        self.pcAccordionItem = AccordionItem(title='Character Sheets', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.pcStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.pcAccordionItem.add_widget(self.pcStackAccordion)

        self.rightAccordion.add_widget(self.pcAccordionItem)

        # let's not get too fancy/custom with this; just add fixed panels
        self.pcPanelsList = []
        self.topgrid = []
        self.halfgrid = []
        self.bottomgrid = []

        for i in range(config.general['max_character_sheets']):

            config.pcKeyLabelArray.append([])
            config.pcValueLabelArray.append([])

            self.pcPanelsList.append(AccordionItem(title='Character ' + str(i), background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight))

            self.box = BoxLayout(orientation='vertical')

            self.buttonbox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

            self.button = Button(text="copy to main window", font_size=config.basefont75)
            self.button.bind(on_press=self.pressGenericButton)
            self.button.bind(on_release=self.copyPCsToMain)
            self.button.sheet = i
            self.buttonbox.add_widget(self.button)

            self.button = Button(text="random major", halign='center', font_size=config.basefont75)
            self.button.bind(on_press=self.pressGenericButton)
            self.button.bind(on_release=self.releaseRandomPC)
            self.buttonbox.add_widget(self.button)

            self.box.add_widget(self.buttonbox)

            self.display = ScrollView(size_hint=(1, 1))
            self.displaygrid = GridLayout(cols=1, spacing=5, size_hint_y=None, size_hint_x=1)
            self.displaygrid.bind(minimum_height = self.displaygrid.setter('height'))
            self.display.add_widget(self.displaygrid)

            self.topgrid.append(GridLayout(cols=2, size_hint_y=None))
            self.topgrid[-1].bind(minimum_height = self.topgrid[-1].setter('height'))
            self.halfgrid.append(GridLayout(cols=4, size_hint_y=None))
            self.halfgrid[-1].bind(minimum_height = self.halfgrid[-1].setter('height'))
            self.bottomgrid.append(GridLayout(cols=2, size_hint_y=None))
            self.bottomgrid[-1].bind(minimum_height = self.bottomgrid[-1].setter('height'))

            for x in range(0,39):

                if x <= 26:
                    ml = False
                    ht = config.tallheight
                    fs = config.basefont90
                else:
                    ml = True
                    ht = config.doubleheight
                    fs = config.basefont90

                if x >= 4 and x <= 26:
                    xhint = .25
                else:
                    xhint = .15

                label = TextInput(text="", multiline=ml, size_hint_y=None, size_hint_x=xhint, height=ht, font_size=fs, font_name='maintextfont', background_color=neutral, foreground_color=styles.textcolor)
                label.self = self
                label.value = x
                config.pcKeyLabelArray[i].append(label)
                label.bind(focus=focusChangePC)

                label = TextInput(text="", multiline=ml, size_hint_y=None, size_hint_x=1.0-xhint, height=ht, font_size=fs, font_name='maintextfont', background_color=neutral, foreground_color=styles.textcolor)
                label.text_size = (self.displaygrid.width, None)
                label.self = self
                label.value = x
                config.pcValueLabelArray[i].append(label)
                label.bind(focus=focusChangePC)

                if x >= 4 and x <= 26:
                    self.halfgrid[-1].add_widget(config.pcKeyLabelArray[i][-1])
                    self.halfgrid[-1].add_widget(config.pcValueLabelArray[i][-1])
                elif x <= 3:
                    self.topgrid[-1].add_widget(config.pcKeyLabelArray[i][-1])
                    self.topgrid[-1].add_widget(config.pcValueLabelArray[i][-1])
                else:
                    self.bottomgrid[-1].add_widget(config.pcKeyLabelArray[i][-1])
                    self.bottomgrid[-1].add_widget(config.pcValueLabelArray[i][-1])

            self.displaygrid.add_widget(self.topgrid[-1])
            self.displaygrid.add_widget(self.halfgrid[-1])
            self.displaygrid.add_widget(self.bottomgrid[-1])

            self.box.add_widget(self.display)

            self.pcPanelsList[-1].add_widget(self.box)

            # add the actual PC panels later

##---------------------------------------------------------------------------------------
#  actor panel
##---------------------------------------------------------------------------------------

        self.actorAItem = AccordionItem(title='Actor Tracker', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.actorMainBox = BoxLayout(orientation='vertical')

        self.actorButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.05), font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyActorToMain)
        self.actorButtonBox.add_widget(self.button)

        self.randomActorButton = Button(text="random actor", halign='center', font_size=config.basefont75)
        self.randomActorButton.bind(on_press=self.pressGenericButton)
        self.randomActorButton.bind(on_release=self.releaseRandomActor)
        self.actorButtonBox.add_widget(self.randomActorButton)

        self.actorMainBox.add_widget(self.actorButtonBox)

        self.actorMainBox.add_widget(Label(text="Actors", halign="center", size_hint=(1,.05), font_size=config.basefont90))
        self.actorDisplay = ScrollView(size_hint=(1, .80))
        self.actorDisplayGrid = GridLayout(cols=1, spacing=5, size_hint_y=None, size_hint_x=1)
        self.actorDisplayGrid.bind(minimum_height = self.actorDisplayGrid.setter('height'))
        self.actorDisplay.add_widget(self.actorDisplayGrid)

        self.actorMainBox.add_widget(self.actorDisplay)

        self.actorIndexToggle = Button(text="Actor Index", halign="center", height=config.tallheight, size_hint=(1,None), font_size=config.basefont90)
        self.actorIndexToggle.value = config.general['actor_index_state']
        self.actorIndexToggle.bind(on_press=self.pressGenericButton)
        self.actorIndexToggle.bind(on_release=self.toggleActorIndexSize)
        self.actorMainBox.add_widget(self.actorIndexToggle)

        self.actorIndexDisplay = ScrollView(size_hint=(1,.20))
        self.actorIndexDisplayGrid = GridLayout(cols=1, spacing=5, size_hint_y=None, size_hint_x=1)
        self.actorIndexDisplayGrid.bind(minimum_height = self.actorIndexDisplayGrid.setter('height'))
        self.actorIndexDisplay.add_widget(self.actorIndexDisplayGrid)

        self.actorMainBox.add_widget(self.actorIndexDisplay)

        self.actorAItem.add_widget(self.actorMainBox)

        self.rightAccordion.add_widget(self.actorAItem)

#---------------------------------------------------------------------------------------
# tracks & scratchpad panel
#---------------------------------------------------------------------------------------

        self.tracksAItem = AccordionItem(title='Tracks, Status, Notes', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.tracksMainBox = BoxLayout(orientation='vertical')

        self.trackButtonBox = GridLayout(cols=2, spacing=5, size_hint=(1,.05))

        self.button = Button(text="copy to main window", size_hint=(1,.05), font_size=config.basefont75)
        self.button.bind(on_press=self.pressGenericButton)
        self.button.bind(on_release=self.copyTracksToMain)
        self.trackButtonBox.add_widget(self.button)

        self.randomTrackButton = Button(text="random track", halign='center', font_size=config.basefont75)
        self.randomTrackButton.bind(on_press=self.pressGenericButton)
        self.randomTrackButton.bind(on_release=self.releaseRandomTrack)
        self.trackButtonBox.add_widget(self.randomTrackButton)

        self.tracksMainBox.add_widget(self.trackButtonBox)

        self.trackTitleGrid = GridLayout(cols=2, spacing=5, size_hint=(1,.10))

        label = Label(text="Status/Condition/Track", size_hint_x=.90, font_size=config.basefont90, font_name='maintextfont', background_color=neutral, foreground_color=styles.textcolor)
        label.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.trackTitleGrid.add_widget(label)
        label = Label(text="On?", size_hint_x=.10, font_size=config.basefont90, font_name='maintextfont', background_color=neutral, foreground_color=styles.textcolor)
        self.trackTitleGrid.add_widget(label)

        self.tracksMainBox.add_widget(self.trackTitleGrid)

        self.trackDisplay = ScrollView(size_hint=(1, 1))
        self.trackDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
        self.trackDisplayGrid.bind(minimum_height = self.trackDisplayGrid.setter('height'))

        for i in range(1,30):

            label = TextInput(text="", multiline=False, size_hint_y=None, size_hint_x=.90, height=config.tallheight, font_size=config.basefont90, font_name='maintextfont', background_color=neutral, foreground_color=styles.textcolor)
            config.trackLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackLabelArray[-1])

            label = CheckBox(size_hint_y=None, size_hint_x=.10, color=[1, 1, 1, 4], height=config.baseheight)
            label.background_checkbox_normal="." + os.sep + "resources" + os.sep + "ui_images" + os.sep + "checkbox_off.png"
            label.background_checkbox_down="." + os.sep + "resources" + os.sep + "ui_images" + os.sep + "checkbox_on.png"
            config.trackStatusLabelArray.append(label)

            self.trackDisplayGrid.add_widget(config.trackStatusLabelArray[-1])

        self.trackDisplay.add_widget(self.trackDisplayGrid)

        self.tracksMainBox.add_widget(self.trackDisplay)

        self.tracksAItem.add_widget(self.tracksMainBox)

        self.rightAccordion.add_widget(self.tracksAItem)

##---------------------------------------------------------------------------------------
#  holder panel for maps
##---------------------------------------------------------------------------------------

        self.mapAccordionItem = AccordionItem(title='Maps', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.mapStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.mapAccordionItem.add_widget(self.mapStackAccordion)

        self.leftAccordion.add_widget(self.mapAccordionItem)

##---------------------------------------------------------------------------------------
#  holder panel for generators
##---------------------------------------------------------------------------------------

        self.generatorAccordionItem = AccordionItem(title='Generators', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.generatorStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.generatorAccordionItem.add_widget(self.generatorStackAccordion)

        self.leftAccordion.add_widget(self.generatorAccordionItem)

##---------------------------------------------------------------------------------------
#  holder panel for oracles
##---------------------------------------------------------------------------------------

        self.oracleAccordionItem = AccordionItem(title='Oracles', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

        self.oracleStackAccordion = Accordion(orientation='vertical', size_hint=(1,1), min_space = config.aiheight)

        self.oracleAccordionItem.add_widget(self.oracleStackAccordion)

        self.leftAccordion.add_widget(self.oracleAccordionItem)

##---------------------------------------------------------------------------------------
#  custom generator panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in gen_module:
            methodToCall = getattr( i, 'initPanel' )
            self.generatorStackAccordion.add_widget(methodToCall(self), 1)


##---------------------------------------------------------------------------------------
#  custom oracle panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in oracle_module:
            methodToCall = getattr( i, 'initPanel' )
            self.oracleStackAccordion.add_widget(methodToCall(self), 1)

##---------------------------------------------------------------------------------------
#  custom maps panels
##---------------------------------------------------------------------------------------

        #self.panelsBox = BoxLayout(orientation="vertical")
        for i in map_module:
            methodToCall = getattr( i, 'initPanel' )
            self.mapStackAccordion.add_widget(methodToCall(self))

#-----------------------------------------
### Functions
#-----------------------------------------

# testing
    def text_entered(self, *args):
        for arg in args:
            print(arg)

#---------------------------------------------------------------------------------------
# miscellaneous functions
#---------------------------------------------------------------------------------------

# trap on main textinput so hitting 'enter' submits text instead of a line break
    def key_action(self, *args):
        #print "got a key event: %s" % list(args)
        #print(self.textInput.text, self.textInput.focus)
        if self.textInput.focus == True and args[1] == 32:
            # trap for pythy
            if config.general['use_pythy_auto_complete'] == True:

                for i in range(len(oracle_module)):
                    if oracle_module[i].__name__ == "pythy":
                        methodToCall = getattr( oracle_module[i], "autoPredict" )
                        answer = methodToCall(self)

        if args[1] == 13 and self.textInput.focus == True:
            #print("Defocus and send text.")
            if len(self.textInput.text) > 0:

                new_text = self.textInput.text

                if config.general['enter_behavior'] != "None":

                    passthrough = True
                    is_roll = False
                    roll_result = False
                    answer = False

                    blocktag = config.general['enter_behavior']

                    matchList = [ [ new_text.startswith("-a"), 'aside', new_text[2:] ], [ new_text.startswith("-p"), 'plain', new_text[2:] ], [ new_text.endswith("-a"), 'aside', new_text[:-2] ], [ new_text.endswith("-p"), 'plain', new_text[:-2] ] ]


                    for test in matchList:
                        if test[0]:
                            blocktag = test[1]
                            new_text = test[2].strip()

                    try:
                        is_roll = int(new_text[0])
                    except:
                        is_roll = False

                    if is_roll or "roll" in new_text or "Roll" in new_text:
                        roll_result = parseTextForDice(new_text)

                    if "??" in new_text:
                        new_text = new_text.replace('??', '?')

                        index = 99
                        for i in range(len(oracle_module)):
                            if oracle_module[i].__name__ == config.oracle:
                                index = i

                        if index < 99:
                            methodToCall = getattr( oracle_module[index], config.oracle_func )
                            answer = methodToCall()
                        else:
                            answer = "No oracle found."

                    if answer or (roll_result and not is_roll):
                        updateCenterDisplay(self, new_text, 'query')
                        passthrough = False

                    if answer:
                        updateCenterDisplay(self, answer, 'oracle')
                        passthrough = False

                    if roll_result:
                        updateCenterDisplay(self, roll_result, 'result')
                        passthrough = False

                    if passthrough == True:
                        updateCenterDisplay(self, new_text, blocktag)

                    quicksave(self, config.curr_game_dir)
                    self.textInput.text = ""
                    if config.general['enter_behavior'] == 'plain':
                        checkForTrigger(self)

                    return True

        elif args[1] == 96 and config.debug == True:   # really sloppy, takes a screenshot on tilde
            timestamp =  '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())
            Window.screenshot(name=config.curr_game_dir + 'screenshot_' + timestamp + '.png')

    def pressGenericButton(self, button):
        button.background_color = accent2

    def releaseSave(self, *args):
        args[0].background_color = neutral
        quicksave(self, config.curr_game_dir)
        saveconfig(self, config.curr_game_dir)
        # make logs
        for i in imports.log_template:
            methodToCall = getattr( i, 'makeLogFile' )
            methodToCall(self)
        updateCenterDisplay(self, "Content and configuration saved.", 'ephemeral')
        clearActor(self, *args)
        clearThread(self, *args)

    # generic function calls
    def miscChartRoll(self, *args):
        args[0].background_color = neutral
        result = eval(args[0].function)()
        updateCenterDisplay(self, result)

    # scenario
    def showBlock(self, *args):
        args[0].background_color = neutral
        showCurrentBlock(self)

    def showExits(self, *args):
        args[0].background_color = neutral
        showCurrentExits(self)

#---------------------------------------------------------------------------------------
# PC, threads, tracks, & actor panel copy functions
#---------------------------------------------------------------------------------------

    def copyTracksToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.trackLabelArray)):
            if len(config.trackLabelArray[i].text) > 0:
                result = result + "\n" + config.trackLabelArray[i].text
                if config.trackStatusLabelArray[i].active:
                    result = result + " [X]"
        result = "[Tracked] " + result
        updateCenterDisplay(self, result, "mechanic1")

    def copyActorToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.actorArray)):
            result = result + "\n" + config.actorArray[i] + " [" + config.actorStatusArray[i] + "]"
        result = "[Actors] " + result
        updateCenterDisplay(self, result, "mechanic1")

    def jumpToActor(self, button):

        button.background_color = neutral
        value = button.value

        self.actorDisplay.scroll_to(config.actorLabelArray[value], padding=40)

    def toggleActorIndexSize(self, button):

        button.background_color = neutral

        if button.value == 0:
            self.actorDisplay.size_hint=(1,.80)
            self.actorIndexDisplay.size_hint=(1,.20)
            button.value = 1
        elif button.value == 1:
            self.actorDisplay.size_hint=(1,.30)
            self.actorIndexDisplay.size_hint=(1,.70)
            button.value = 2
        elif button.value == 2:
            self.actorDisplay.size_hint=(1,.70)
            self.actorIndexDisplay.size_hint=(1,.30)
            button.value = 0

        config.general['actor_index_state'] = button.value

    def copyPCsToMain(self, button):
        button.background_color = neutral
        result = ""
        sheet = button.sheet
        for i in range(len(config.pcKeyLabelArray[sheet])):
            #if len(config.pcKeyLabelArray[sheet][i].text) > 0:
            result = result + " | " + config.pcKeyLabelArray[sheet][i].text + ": " + config.pcValueLabelArray[sheet][i].text
        result = "[PC " + str(sheet) + "] " + result
        updateCenterDisplay(self, result, "mechanic1")

    def copyThreadsToMain(self, *args):
        args[0].background_color = neutral
        result = ""
        for i in range(len(config.threadArray)):
            result = result + "\n" + config.threadArray[i] + " [" + config.threadStatusArray[i] + "]"
        result = "[Threads] " + result
        updateCenterDisplay(self, result, "mechanic1")

#---------------------------------------------------------------------------------------
# submit text input buttons
#---------------------------------------------------------------------------------------

    def releaseQuestion(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')

        index = 99
        for i in range(len(oracle_module)):
            if oracle_module[i].__name__ == config.oracle:
                index = i

        if index < 99:
            methodToCall = getattr( oracle_module[index], config.oracle_func )
            answer = methodToCall()
        else:
            answer = "No oracle found."

        updateCenterDisplay(self, answer, 'oracle')
        self.textInput.text = ""
        quicksave(self, config.curr_game_dir)

    def getSeed(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')

        index=-9
        match = 'seeds'
        if config.general['seed_func'] == 'useMythicComplex':
            match = 'mythic'
        for i in range(len(oracle_module)):
            #print(oracle_module[i].__name__)
            if oracle_module[i].__name__ == match:
                index = i

        try:
            methodToCall = getattr( oracle_module[index], config.general['seed_func'] )
            if config.general['seed_func'] == 'useThreePartSeed':
                methodToCall(self, config.general['seed_type'], config.general['seed_subtype'])
            else:
                methodToCall(self, config.general['seed_type'])
        except:
            updateCenterDisplay(self,  "[Seed] " + seed_action() + " " + seed_subject(), 'oracle')

        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def getSeedAlternate(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, self.textInput.text, 'query')

        index=-9
        for i in range(len(oracle_module)):
            if oracle_module[i].__name__ == 'seeds':
                index = i
        try:
            methodToCall = getattr( oracle_module[index], config.general['seed_alt_func'] )
            if config.general['seed_alt_func'] == 'useThreePartSeed':
                methodToCall(self, config.general['seed_alt_type'], config.general['seed_alt_subtype'])
            else:
                methodToCall(self, config.general['seed_alt_type'])
        except:
            updateCenterDisplay(self,  "[Seed] " + seed_action() + " " + seed_subject(), 'oracle')

        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseRoll(self, *args):
        self.rollSubmitButton.background_color = neutral
        result = rollDice(self.textInput.text)
        updateCenterDisplay(self, result, 'result')
        quicksave(self, config.curr_game_dir)
        if result != "Please use standard dice notation, ie, 1d10 or 2d6x3.":
            self.textInput.text = ""

    def releasePlayer(self, *args):
        self.playerSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateCenterDisplay(self, new_text, 'plain')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

        checkForTrigger(self)

    def releaseDM(self, *args):
        self.dmSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateCenterDisplay(self, new_text, "aside")
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseThread(self, *args):
        self.threadSubmitButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = "" + self.textInput.text + ""
            updateThreadDisplay(self, new_text, "Current")
            updateCenterDisplay(self, "[New Thread] " + new_text, 'aside')
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def releaseAddActor(self, *args):
        self.addActorButton.background_color = neutral
        if len(self.textInput.text) > 0:
            new_text = self.textInput.text
            updateActorDisplay(self, new_text, 'Current')
            updateCenterDisplay(self, "[New Actor] " + new_text, 'aside')
            updateActorIndex(self)
            quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

#---------------------------------------------------------------------------------------
# center status bar
#---------------------------------------------------------------------------------------

    def releaseTrackerUp(self, *args):
        args[0].background_color = neutral
        config.general['tracker'] = config.general['tracker'] + 1
        if config.general['use_main_tracker_for_mythic'] == True:
            for i in range(len(oracle_module)):
                if oracle_module[i].__name__ == 'mythic':
                    methodToCall = getattr( oracle_module[i], 'setChaosFactor' )
                    result = methodToCall("up")
                    config.general['tracker'] = config.general['mythic_chaos_factor']
                    updateCenterDisplay(self, result, 'result')

        self.trackLabel.text = str(config.general['tracker'])

    def releaseTrackerDown(self, *args):
        args[0].background_color = neutral
        config.general['tracker'] = config.general['tracker'] - 1
        if config.general['use_main_tracker_for_mythic'] == True:
            for i in range(len(oracle_module)):
                if oracle_module[i].__name__ == 'mythic':
                    methodToCall = getattr( oracle_module[i], 'setChaosFactor' )
                    result = methodToCall("down")
                    config.general['tracker'] = config.general['mythic_chaos_factor']
                    updateCenterDisplay(self, result, 'result')

        self.trackLabel.text = str(config.general['tracker'])

    def toggleEnterBehavior(self, spinner, text):
        config.general['enter_behavior'] = text


    def toggledBookmark(self, button):
        if self.clearBookmarkButton.state == 'down':
            button.index = -9
            config.general['bookmarks'][button.value] = -9
            button.text = '-'
            button.state = 'normal'
            self.clearBookmarkButton.state = 'normal'
            self.clearBookmarkButton.background_color = neutral
        else:
            if button.index >= 0:
                jumpToIndex(self, button.index)
                button.state = 'normal'

    def navJump(self, button):
        button.background_color = neutral
        if button.text == "top":
            button.text = "bottom"
            jumpToIndex(self, 0)
        else:
            button.text = "top"
            jumpToIndex(self, -1)

    def navFind(self, button):
        button.background_color = neutral
        #print(len(self.textInput.text))
        if len(self.textInput.text) > 0:
            findText(self, self.textInput.text)
            self.textInput.text = ""

    def navNext(self, button):
        button.background_color = neutral
        if len(config.general['findList']) > 0:
            jumpToNext(self)

#---------------------------------------------------------------------------------------
# center footer bar
#---------------------------------------------------------------------------------------

    def cycleOracle(self, button):

        if button.text == "mythic":
            button.text = "fu"
            config.oracle = "fu"
            config.oracle_func = "fu"
            config.general['seed_func'] = 'useTwoPartSeed'
            config.general['seed_alt_func'] = ''
            config.general['seed_subtype_pretty'] = 'Seed'
            config.general['use_main_tracker_for_mythic'] = False
        else:
            button.text = "mythic"
            config.oracle = "mythic"
            config.oracle_func = "mythic"
            config.general['seed_func'] = 'useMythicComplex'
            config.general['seed_alt_func'] = ''
            config.general['seed_subtype_pretty'] = 'Complex'
            config.general['use_main_tracker_for_mythic'] = True

        try:
            self.seedButtonsBox.remove_widget(self.seedAlternateButton)
            self.seedButtonsBox.size_hint_y=1
            self.seedButton.text = config.general['seed_subtype_pretty'].capitalize()
        except:
            pass

    def toggleResolutionMode(self, button):
        if button.state == "down":
            button.background_color = (neutral[0]*.50, neutral[1]*.50, neutral[2]*.50,1)
            config.general['use_dice_qualities'] = True
        else:
            button.background_color = neutral
            config.general['use_dice_qualities'] = False

    def releaseRandomThread(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Major", "Minor", "Past", "Resolved", "Abandoned", "Don't Show", "Current"]
        if text in filterList:
            curr_index = filterList.index(text)
            updateCenterDisplay(self, getRandomThread(filterList[curr_index]))
        else:
            updateCenterDisplay(self, getRandomThread("All"))
        self.textInput.text = ""

    def releaseRandomActor(self, *args):
        args[0].background_color = neutral
        text = self.textInput.text.capitalize()
        filterList = ["Past", "In party", "Retired", "Deceased", "Remote", "Don't Show", "Current"]
        if text in filterList:
            curr_index = filterList.index(text)
            updateCenterDisplay(self, getRandomActor(filterList[curr_index]))
        else:
            updateCenterDisplay(self, getRandomActor("All"))
        self.textInput.text = ""

    def releaseRandomPC(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, getRandomPC(self.textInput.text))
        else:
            updateCenterDisplay(self, getRandomPC())
        self.textInput.text = ""

    def releaseRandomTrack(self, *args):
        args[0].background_color = neutral
        if len(self.textInput.text) > 0:
            updateCenterDisplay(self, getRandomTrack(self.textInput.text))
        else:
            updateCenterDisplay(self, getRandomTrack())
        self.textInput.text = ""

    def releasePresetDice(self, *args):
        args[0].background_color = neutral
        result = rollDice(args[0].text)
        updateCenterDisplay(self, result, 'result')
        quicksave(self, config.curr_game_dir)
        self.textInput.text = ""

    def chooseFromList(self, *args):
        args[0].background_color = neutral
        value = args[0].value
        pick = args[0].text.split('\n')
        pick = pick[1]
        if len(self.textInput.text) > 0:
            result_string, result, form, roll = chooseWeighted(value, self.textInput.text, "result")
            if len(result_string) > 0:
                updateCenterDisplay(self, "[" + pick + " Options] " + result_string, 'query')
                updateCenterDisplay(self, "[" + roll + "] " + result, form)
            else:
                updateCenterDisplay(self, "Please enter a comma-separated list in one line that has at least as many options as needed.", 'ephemeral')
        self.textInput.text = ""

    def releaseORERoll(self, *args):
        args[0].background_color = neutral
        result = rollOREDice(self.textInput.text)
        updateCenterDisplay(self, result, 'result')
        quicksave(self, config.curr_game_dir)
        if result != "Please enter a number in the main text input for your dice pool.":
            self.textInput.text = ""

    def releaseFateRoll(self, *args):
        args[0].background_color = neutral
        result = rollFateDice(self.textInput.text)
        updateCenterDisplay(self, result, 'result')
        quicksave(self, config.curr_game_dir)
        if result != "Please enter a number in the main text input for your dice pool.":
            self.textInput.text = ""

#---------------------------------------------------------------------------------------
# heartbeat functions
#---------------------------------------------------------------------------------------

    def on_enter(self):

        # populate all the fields that pull from save game files
        loadconfig(self, config.curr_game_dir)
        quickload(self, config.curr_game_dir)

        # now update variable widgets; general miscellanous first
        try:
            self.enterSpinner.text = str(config.general["enter_behavior"])
            self.editSpinner.text = str(config.general["edit_behavior"])

        except:
            pass

        try:
            l = ToggleButtonBehavior.get_widgets('bookmarks')
            for i in range(len(l)):
                if config.general['bookmarks'][i] >= 0:
                    l[i].index = config.general['bookmarks'][i]
                    l[i].text = str(config.general['bookmarks'][i])
                else:
                    l[i].text = '-'
            del l
        except:
            pass

        try:
            if config.general['use_main_tracker_for_mythic'] == True:
                config.general['tracker'] = config.general['mythic_chaos_factor']
        except:
            pass

        try:
            self.trackLabel.text = str(config.general['tracker'])
        except:
            pass

        try:
            if config.general['use_dice_qualities'] == True:
                self.qualitiesButton.background_color = (neutral[0]*.50, neutral[1]*.50, neutral[2]*.50,1)
            else:
                self.qualitiesButton.background_color = neutral
        except:
            pass

        try:
            self.oracleButton.text = config.oracle
        except:
            pass

        # pc panel
        del self.pcPanelsList[config.general['total_pcs_to_show']:]

        for i in range(len(self.pcPanelsList)):
            self.pcStackAccordion.add_widget(self.pcPanelsList[i], len(self.pcPanelsList))

        try:
            nameList = []
            for pc in range(len(config.pcKeyLabelArray)):
                name = [i for i in config.pcKeyLabelArray[pc] if i.text=="Name"]
                nick = [i for i in config.pcKeyLabelArray[pc] if i.text=="Nick"]
                nn = [i for i in config.pcKeyLabelArray[pc] if i.text=="NN"]

                if nick:
                    index = config.pcKeyLabelArray[pc].index(nick[0])
                    nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
                elif nn:
                    index = config.pcKeyLabelArray[pc].index(nn[0])
                    nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
                elif name:
                    index = config.pcKeyLabelArray[pc].index(name[0])
                    nameList.append(config.pcValueLabelArray[pc][index].text.strip("\""))
                else:
                    nameList.append("")

            for i in range(len(self.pcPanelsList)):
                if len(nameList[i]) > 0:
                    self.pcPanelsList[i].title = nameList[i]
        except:
            if config.debug == True:
                print("[Main on enter pc names] Unexpected error:", sys.exc_info())

        # now update PC panel to the right sizes
        try:

            for i in range(config.general['max_character_sheets']):

                self.halfgrid[i].clear_widgets()
                self.topgrid[i].clear_widgets()
                self.bottomgrid[i].clear_widgets()

                limiter = config.general['half_size_rows']

                for x in range(0,39):

                    if config.general['character_sheet_style'] == 0:
                        if x <= limiter:
                            ml = False
                            ht = config.tallheight
                            fs = config.basefont90
                        else:
                            ml = True
                            ht = config.quadrupleheight
                            fs = config.basefont90

                        if x >= 4 and x <= limiter:
                            xhint = .25
                        else:
                            xhint = .15

                        config.pcKeyLabelArray[i][x].multiline = ml
                        config.pcKeyLabelArray[i][x].size_hint_x = xhint
                        config.pcKeyLabelArray[i][x].height = ht
                        config.pcKeyLabelArray[i][x].font_size = fs

                        config.pcValueLabelArray[i][x].multiline = ml
                        config.pcValueLabelArray[i][x].size_hint_x = 1.0-xhint
                        config.pcValueLabelArray[i][x].height = ht
                        config.pcValueLabelArray[i][x].font_size = fs

                        if x <= 1:
                            self.topgrid[i].add_widget(config.pcKeyLabelArray[i][x])
                            self.topgrid[i].add_widget(config.pcValueLabelArray[i][x])
                        elif x <= limiter:
                            self.halfgrid[i].add_widget(config.pcKeyLabelArray[i][x])
                            self.halfgrid[i].add_widget(config.pcValueLabelArray[i][x])
                        else:
                            self.bottomgrid[i].add_widget(config.pcKeyLabelArray[i][x])
                            self.bottomgrid[i].add_widget(config.pcValueLabelArray[i][x])

                    else:

                        self.topgrid[i].cols = 1
                        #self.halfgrid[i].parent.remove_widget(self.halfgrid[i])
                        #self.bottomgrid[i].parent.remove_widget(self.bottomgrid[i])

                        if x == 1:                  # description block
                            ml = True
                            fs = config.basefont80
                            ht = config.quintupleheight
                        elif x == 0 or x % 2 == 0:    # one line row
                            ml = False
                            ht = config.tallheight
                            fs = config.basefont90
                        else:                       # everything else is taller
                            ml = True
                            fs = config.basefont80
                            ht = config.quadrupleheight

                        config.pcValueLabelArray[i][x].multiline = ml
                        config.pcValueLabelArray[i][x].height = ht
                        config.pcValueLabelArray[i][x].font_size = fs

                        self.topgrid[i].add_widget(config.pcValueLabelArray[i][x])

        except:
            pass

        # now actor index
        try:
            updateActorIndex(self)
        except:
            pass

        # update which seed scheme to use
        try:
            if config.general['seed_alt_func'] == '':
                self.seedButtonsBox.remove_widget(self.seedAlternateButton)
                self.seedButtonsBox.size_hint_y=1
                self.seedButton.text = config.general['seed_subtype_pretty'].capitalize()
            else:
                self.seedButton.text = config.general['seed_subtype_pretty'].capitalize()
                self.seedAlternateButton.text = config.general['seed_alt_subtype_pretty'].capitalize()
        except:
            pass

        # one function is called per active panel; use to update panel widgets
        try:
            for i in gen_module:
                methodToCall = getattr( i, 'onEnter' )
                methodToCall(self)

            for i in oracle_module:
                methodToCall = getattr( i, 'onEnter' )
                methodToCall(self)

            for i in map_module:
                methodToCall = getattr( i, 'onEnter' )
                methodToCall(self)
        except:
            if config.debug == True:
                print("[OnEnter calls] Unexpected error:", sys.exc_info())

        try:
            Window.set_title("Pythia-Oracle -- " + os.path.basename(os.path.normpath(config.curr_game_dir)) + " -- " + str(len(config.textArray)) + " blocks")
        except:
            pass

        # SCENARIO STUFF
        if config.scenario['active'] == True:

            if config.scenario['use_core'] == False:
                self.generatorStackAccordion.remove_widget(self.actorsAItem)
                self.generatorStackAccordion.remove_widget(self.hexAItem)
                self.mapStackAccordion.remove_widget(self.mapAItem)

            if config.scenario['use_oracle'] == False:
                self.oracleStackAccordion.remove_widget(self.fuAItem)
                self.oracleStackAccordion.remove_widget(self.seedsAItem)
                self.submitButtonsBox.remove_widget(self.questionSubmitButton)
                self.submitButtonsBox.remove_widget(self.seedButton)
                self.submitButtonsBox.remove_widget(self.seedAlternateButton)

            # scenario logic - required
            mod = config.curr_game_dir + "scenlogic.py"
            filename = mod.split('/')[-1]
            pyfile = filename.split('.')[0]
            scenlogic = imp.load_source( pyfile, mod)

            # scenario oracle/info panel - required
            mod = config.curr_game_dir + "scenpanel.py"
            filename = mod.split('/')[-1]
            pyfile = filename.split('.')[0]
            scenpanel = imp.load_source( pyfile, mod)

            self.oracleStackAccordion.add_widget(scenpanel.initPanel(self))

            # scenario map panel - optional
            try:
                mod = config.curr_game_dir + "scenmap.py"
                filename = mod.split('/')[-1]
                pyfile = filename.split('.')[0]
                scenmap = imp.load_source( pyfile, mod)

                self.mapStackAccordion.add_widget(scenmap.initPanel(self))
            except:
                pass

            # scenario generator panel - optional
            try:
                mod = config.curr_game_dir + "scengen.py"
                filename = mod.split('/')[-1]
                pyfile = filename.split('.')[0]
                scengen = imp.load_source( pyfile, mod)

                self.generatorStackAccordion.add_widget(scengen.initPanel(self))
            except:
                pass

            with open(config.curr_game_dir + "scenario.txt", "r") as f:
                config.advDict = json.load(f)

            for button in self.scenarioButtonList:
                self.submitButtonsBox.add_widget(button)

            block = config.scenario['block']

            self.scenarioTitleLabel = Button(text=config.advDict[block]['title'], size_hint=(1,1), font_size=config.basefont75)
            self.titleBarBox.add_widget(self.scenarioTitleLabel)

            if len(config.textLabelArray) == 1:
                config.advDict[block]['shown'] == 99
                showCurrentBlock(self)
                saveconfig(self, config.curr_game_dir)
