#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# Daisy Pandey, September 6, 2020, Created File
# Daisy Pandey, September 8, 2020, Added code to add CD, select CD, add track
# Daisy Pandey, September 9, 2020, Added structured error handling
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.

        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
            if cdId <= 0:
                raise ValueError
        except ValueError:
            print('====Error!!=====')
            print(f'You entered {cdId}, which is not a valid entry for ID.')
            print('Please enter a number that is greater than zero.')
            print()
            return
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx
        """
        
        try: 
            cd_idx = int(cd_idx)
            if cd_idx <= 0:
                raise ValueError        
        except ValueError:
            print('====Error!!=====')
            print(f'You entered {cd_idx}, which is not a valid entry for CD ID.')
            print('Please enter the CD ID from the list above.')
            print()
            return
            
        for row in table: 
            if row.cd_id == cd_idx: 
                return row 
            
        raise Exception('This CD / Album index does not exist')

    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd

        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.
        """

        trkPos, trkTitle, trkLength = track_info 
        try:
            trkPos = int(trkPos)
            if trkPos <= 0:
                raise ValueError
        except ValueError: 
            print('====Error!!=====')
            print(f'You entered {trkPos}, which is not a valid Track ID.')
            print('Please enter a number for Track ID.')
            print()
            return
        
        track = DC.Track(trkPos, trkTitle, trkLength) 
        cd.add_track(track)
        


