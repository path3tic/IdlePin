import pyautogui
import datetime
import os
import time

#Setup environment
ImageFolder = os.getcwd() + os.sep + 'img' + os.sep
Width, Height = pyautogui.size()
Screen = (0, 0, Width-1, Height-1)

#Pause time global variable
waiting = .2

#Define functions

def wait_for(img, region = Screen, time_out = waiting):
    img_path = ImageFolder + img
    location = None
    start_time = time.time()

    while (location == None):
        try:
            elapsed = time.time() - start_time
            if elapsed > time_out:
                return location

            location = pyautogui.locateOnScreen(img_path)
        except Exception as e:
            print(e)
    return location

def click_on(img, region = Screen):
    img_path = ImageFolder + img
    location = None

    try:
        location = pyautogui.locateCenterOnScreen(img_path)
        pyautogui.click(location)
        print("clicked on " + img)
    except Exception as e:
        print(e)
    return location


#Support procedures
def doubleclick_on_Pin(img, region = Screen):
    img_path = ImageFolder + "Upper_Left_Gear.png"
    location = None

    #crop screen
    Screen2 = pyautogui.locateOnScreen(img_path)

    location = None
    img_path = ImageFolder + img
    try:
        location = pyautogui.locateOnScreen(img_path, region = (Screen2.left, Screen2.top + 25, Screen[2]- Screen2.left, Screen[3] - Screen2.top))
        if location is not None:
            pyautogui.click(location, clicks=2, interval=0.2)
            print("clicked on " + img)
    except Exception as e:
        print(e)
    return location

def Craft(img):
    img_path = ImageFolder + img
    location = None

    try:
        location = pyautogui.locateOnScreen(img_path)
        if location is not None:
            pyautogui.click((location.left - 55, location.top + 25))
            print("clicked left of " + img)
    except Exception as e:
        print(e)
    return location


def Crafting(img):

    location = None
    location = wait_for("Craft.png")
    if location is not None:
        location = click_on("Craft.png")

    location = None
    location = wait_for("Craft_Ready.png")
    if location is not None:
        location = click_on("Craft_Ready.png")

    time.sleep(waiting)

    #check if in crafting window
    location = None
    location = wait_for("Craft_Window.png")
    if location is not None:

        location = wait_for("Get.png")
        if location is not None:
            location = click_on("Get.png")

        time.sleep(waiting)

        location = wait_for(img)
        if location is not None:
            location = Craft(img)

        time.sleep(waiting)

        location = wait_for('Exit.png')
        if location is not None:
            location = click_on('Exit.png')

    Reset()

    return

def Bar():

    location = wait_for('Progress_Bar.png')

    if location is not None:
        location = click_on('Progress_Bar.png')
    return

def Reset():

    location = wait_for('Icon.png')

    if location is not None:
        coordinates = (location.left + 450, location.top + 170)
        pyautogui.click(coordinates)
        print("clicked on" + "Icon.png")

    return

def Fight():

    location = wait_for('Boss.png')

    if location is not None:
        location = click_on('Boss.png')

        time.sleep(1)

        location = wait_for('Fight.png')

        if location is not None:
            location = click_on('Fight.png')
            time.sleep(5)
        else:
            location = wait_for('Exit.png')

            if location is not None:
                location = click_on('Exit.png')

    Reset()
    return

def DragDrop(img1, img2):

    location1 = wait_for(img1)
    location2 = wait_for(img2)

    if (location1  is not None and location2 is not None):
        pyautogui.moveTo(location1.left, location1.top)
        pyautogui.dragTo(location2.left, location2.top, 3, button='left')


def Fuse1():
    #Particle 1
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Alpha.png"))) > 1:
        doubleclick_on_Pin("Pin_Alpha.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Beta.png"))) > 1:
        doubleclick_on_Pin("Pin_Beta.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Gamma.png"))) > 1:
        doubleclick_on_Pin("Pin_Gamma.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Delta.png"))) > 1:
        doubleclick_on_Pin("Pin_Delta.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Epsilon.png"))) > 1:
        doubleclick_on_Pin("Pin_Epsilon.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Zeta.png"))) > 1:
        doubleclick_on_Pin("Pin_Zeta.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Eta.png"))) > 1:
        doubleclick_on_Pin("Pin_Eta.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Theta.png"))) > 1:
        doubleclick_on_Pin("Pin_Theta.png")
    return

def Fuse2():
    # Particle 2
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Iota.png"))) > 1:
        doubleclick_on_Pin("Pin_Iota.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Kappa.png"))) > 1:
        doubleclick_on_Pin("Pin_Kappa.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Lambda.png"))) > 1:
        doubleclick_on_Pin("Pin_Lambda.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Mu.png"))) > 1:
        doubleclick_on_Pin("Pin_Mu.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Nu.png"))) > 1:
        doubleclick_on_Pin("Pin_Nu.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Xi.png"))) > 1:
        doubleclick_on_Pin("Pin_Xi.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Omicron.png"))) > 1:
        doubleclick_on_Pin("Pin_Omicron.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Pi.png"))) > 1:
        doubleclick_on_Pin("Pin_Pi.png")
    return

def Fuse3():
    # Swords
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_1.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_1.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_2.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_2.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_3.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_3.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_4.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_4.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_5.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_5.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_6.png"))) > 1:
        doubleclick_on_Pin("Pin_Sword_6.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Sword_7.png"))) > 1:
        #doubleclick_on_Pin("Pin_Sword_7.png")
    return

def Fuse4():
    #Bubbles
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_1.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_1.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_2.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_2.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_3.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_3.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_4.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_4.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_5.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_5.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_6.png"))) > 1:
        doubleclick_on_Pin("Pin_Bubbles_6.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Bubbles_7.png"))) > 1:
        #doubleclick_on_Pin("Pin_Bubbles_7.png")
    return

def Fuse5():
    #Leaf
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_1.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_1.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_2.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_2.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_3.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_3.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_4.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_4.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_5.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_5.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_6.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_6.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_7.png"))) > 1:
        doubleclick_on_Pin("Pin_Leaf_7.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_8.png"))) > 1:
        #doubleclick_on_Pin("Pin_Leaf_8.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_9.png"))) > 1:
        #doubleclick_on_Pin("Pin_Leaf_9.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Leaf_10.png"))) > 1:
        #doubleclick_on_Pin("Pin_Leaf_10.png")
    return

def Fuse6():
    #Core
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_1.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_1.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_2.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_2.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_3.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_3.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_4.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_4.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_5.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_5.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_6.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_6.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_7.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_7.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_8.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_8.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Core_9.png"))) > 1:
        doubleclick_on_Pin("Pin_Core_9.png")
    return

def Fuse7():
    #Alchemy
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_1.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_1.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_2.png"))) > 1:
        doubleclick_on_Pin("Pin_Re_2.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_3.png"))) > 1:
        doubleclick_on_Pin("Pin_Re_3.png")
    if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_4.png"))) > 1:
        doubleclick_on_Pin("Pin_Re_4.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_5.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_5.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_6.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_6.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_7.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_7.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_8.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_8.png")
    #if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_9.png"))) > 1:
        #doubleclick_on_Pin("Pin_Re_9.png")
    return


def Season():

    location = wait_for('Season.png')

    if location is not None:
        location = click_on('Season.png')
        location = wait_for('New_Season.png')

        im1 = pyautogui.screenshot()
        im1.save(r"C:\Users\zajic\PycharmProjects\IdlePin\Season screens\screenshot_1 " + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png")

        if location is not None:
            location = click_on('New_Season.png')

            im1 = pyautogui.screenshot()
            im1.save(r"C:\Users\zajic\PycharmProjects\IdlePin\Season screens\screenshot_2 " + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png")

            location = wait_for('Start_New_Season.png')

            if location is not None:
                location = click_on('Start_New_Season.png')


    return

def SetPin(pin, slot):
    location = wait_for(pin)

    if location is not None:
        location = click_on(pin)
        location = wait_for(slot)
        if location is not None:
            location = click_on(slot)

def Lab():

    start_time = datetime.datetime.now()

    #Enter Lab
    location = wait_for('Lab.png')

    if location is not None:
        pyautogui.click((location.left, location.top))
    else:
        end_time = datetime.datetime.now()
        print("Lab failed in %", end_time - start_time)
        return

    #Gett All
    LabLocation = wait_for('Lab_Get_All.png')
    if LabLocation is not None:
        pyautogui.click((LabLocation.left, LabLocation.top))

        #Set Custom (25, 75)
        #pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
        #pyautogui.typewrite('555')

    #Scroll up
    #pyautogui.moveTo(location.left + 25, location.top + 375)
    #for i in range(30):
    #    pyautogui.scroll(1)

        # Set Alpha
        location = wait_for('Lab_Resistance_60.png')
        if location is not None:
            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            time.sleep(.2)
            pyautogui.typewrite('3667')
            pyautogui.click((location.left + 135, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('3250')
            pyautogui.click((location.left + 328, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2800')
            pyautogui.click((location.left + 521, location.top - 26))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('3000')
            pyautogui.click((location.left + 135, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2489')
            pyautogui.click((location.left + 328, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2644')
            pyautogui.click((location.left + 521, location.top + 87))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2100')
            pyautogui.click((location.left + 135, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2217')
            pyautogui.click((location.left + 328, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2333')
            pyautogui.click((location.left + 521, location.top + 200))

        for i in range(5):
            pyautogui.scroll(-1)

        # Set Kappa
        location = wait_for('Lab_Resistance_105.png')
        if location is not None:
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1750')
            pyautogui.click((location.left + 135, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1833')
            pyautogui.click((location.left + 328, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2000')
            pyautogui.click((location.left + 521, location.top - 26))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1444')
            pyautogui.click((location.left + 135, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1556')
            pyautogui.click((location.left + 328, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1067')
            pyautogui.click((location.left + 521, location.top + 87))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1067')
            pyautogui.click((location.left + 135, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1133')
            pyautogui.click((location.left + 328, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1200')
            pyautogui.click((location.left + 521, location.top + 200))

            for i in range(6):
                pyautogui.scroll(-1)

        # Set Banana
        location = wait_for('Lab_Resistance_100.png')
        if location is not None:
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2333')
            pyautogui.click((location.left + 135, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('2000')
            pyautogui.click((location.left + 328, location.top - 26))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1667')
            pyautogui.click((location.left + 521, location.top - 26))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1000')
            pyautogui.click((location.left + 135, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('444')
            pyautogui.click((location.left + 328, location.top + 87))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('556')
            pyautogui.click((location.left + 521, location.top + 87))

            # Set Custom (25, 75)
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1333')
            pyautogui.click((location.left + 135, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('833')
            pyautogui.click((location.left + 328, location.top + 200))
            pyautogui.click((LabLocation.left + 25, LabLocation.top + 75))
            pyautogui.typewrite('1000')
            pyautogui.click((location.left + 521, location.top + 200))

            for i in range(17):
                pyautogui.scroll(1)

    #Exit
    location = wait_for('Exit.png')
    if location is not None:
        pyautogui.click(location.left, location.top)
        end_time = datetime.datetime.now()
        print("Lab executed in", end_time - start_time)

    return

def GoToMap(img):
    location = wait_for('Map.png')
    if location is not None:
        pyautogui.click(location.left, location.top)

        location = wait_for(img)
        if location is not None:
            pyautogui.click(location.left, location.top)


def GoToTower(img):
    location = wait_for('Tower.png')
    if location is not None:
        pyautogui.click(location.left, location.top)


        location = wait_for(img)
        if location is not None:
            time.sleep(1)
            pyautogui.moveTo(location.left, location.top)
            time.sleep(1)
            pyautogui.click(location.left, location.top)

def PushMap():
    while True:
        location = wait_for('Map_1_5.png')
        if location is not None:
            GoToMap("Map_2.png")
        location = wait_for('Map_2_10.png')
        if location is not None:
            GoToMap("Map_3.png")
        location = wait_for('Map_3_10.png')
        if location is not None:
            GoToMap("Map_4.png")
        location = wait_for('Map_4_10.png')
        if location is not None:
            return
            #GoToMap("Map_5.png")

        time.sleep(3)
        Bar()
        Fuse1()


#Main program
if __name__ == '__main__':
    print('#' * 50)
    print(f'Image Folder: {ImageFolder}')
    print(f'Screen Region: {Screen}')
    print('#' * 50)

    time.sleep(3)





    #DragDrop('Pin_Zeta.png', 'Pin_Gamma.png')
    #exit(1)

    #Season()
    #exit(1)

    #Fast Seasons below

    while True:
        #red backpack, auto progress maps, bb cupid formation, scroll lab and season
        start_time = datetime.datetime.now()
        print('starting new season ', start_time)
        Season()
        SetPin("Pin_Sonic_3.png", "Slot_Support.png")
        SetPin("Pin_Transformer_1.png", "Slot_Free.png")
        SetPin("Pin_Transformer_2.png", "Slot_Free.png")
        SetPin("Pin_Bob_4.png", "Slot_Free.png")
        Lab()
        PushMap()
        #exit(1)
        end_time = datetime.datetime.now()
        print('finishing season in ', end_time - start_time)
        #exit(1)


    #Normal Farming Below

    #Craft('Pin_Core_1.png')
    WhatWeCraft = 'Pin_Gamma.png'


    while True:

        #Farm Libras
        FarmLibras = False
        if FarmLibras:
            time.sleep(waiting)
            if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Re_2.png"))) >= 2:
                if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Pot_2.png"))) == 0:

                    location = wait_for('Map_tower_x.png')
                    if location is None:
                        GoToTower("Tower_Pot.png")

            if len(list(pyautogui.locateAllOnScreen(ImageFolder + "Pin_Pot_2.png"))) >= 3:

                location = wait_for('Map_11_x.png')
                if location is None:
                    GoToMap("Map_11.png")

        time.sleep(waiting)
        Fight()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse1()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse2()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse3()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse4()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse5()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        time.sleep(waiting)
        Fuse6()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        if not FarmLibras:
            time.sleep(waiting)
            Fuse7()

        time.sleep(waiting)
        Crafting(WhatWeCraft)
        time.sleep(waiting)
        Bar()

        DragDrop('Pin_Re_3.png', 'Pin_Pot_2.png')
        DragDrop('Pin_Re_2.png', 'Pin_Pot_2.png')

        time.sleep(1)
        Reset()

