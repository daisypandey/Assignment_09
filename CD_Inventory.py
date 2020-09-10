#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# Daisy Pandey, September 6, 2020, Created File
# Daisy Pandey, September 8, 2020, Extended functionality to add tracks
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    
    # Process load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Process add a CD
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Process display current inventory
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    # Handle tracks on an individual CD
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)

        while True: 
            IO.ScreenIO.print_CD_menu() 
            strChoice = IO.ScreenIO.menu_CD_choice() 
            if strChoice == 'x': 
                break
            
            # Add track
            if strChoice == 'a':
                tplTrkInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrkInfo, cd)
                IO.ScreenIO.show_tracks(cd)
                continue  # start loop back at top.
            
            # Display CD/Album details
            elif strChoice == 'd': 
                IO.ScreenIO.show_tracks(cd) 
                continue  # start loop back at top.
            
            # Remove track
            elif strChoice == 'r': 
                IO.ScreenIO.show_tracks(cd) 
                trk_idx = input('Select the Track index: ') 
                cd.rmv_track(trk_idx)
                IO.ScreenIO.show_tracks(cd) 
                continue  # start loop back at top.
            else: 
                print('General Error')
                
    # Process save inventory to file            
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
            print('Data saved to file.')
            print()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')