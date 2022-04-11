from Utility.ByteStream import Writer
from Utility.Utils import Utils

class OwnHomeDataMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.client = client
        self.player = player

    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)  # Timestamp
        
        self.writeVInt(self.player.trophies)  # trophies
        self.writeVInt(self.player.trophies)

        self.writeVInt(0)
        self.writeVInt(99)  # reward for trophy road

        self.writeVInt(self.player.player_experience)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(0)
        
        self.writeVInt(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeVInt(29)
            self.writeVInt(self.player.brawlers_skins[brawler_id])  # skinID

        # Unlocked Skins array
        self.writeVInt(len(self.player.skins_id))
        for skin_id in self.player.skins_id:
            self.writeDataReference(29, skin_id)
            
        self.writeVInt(0) # array
        
        self.writeVInt(1) # ?
        self.writeVInt(1) # ?
        self.writeVInt(1) # ?
        
        self.writeBoolean(True) # token limt reached
        self.writeVInt(1) # ?
        self.writeBoolean(True) # ?
        
        self.writeVInt(self.player.tokensdoubler)
        self.writeVInt(6) # season end timer
        self.writeVInt(1)
        self.writeVInt(1)
        
        self.writeVInt(200)
        self.writeVInt(5)
        self.writeVInt(93)
        
        self.writeVInt(206)
        
        self.writeVInt(456)
        self.writeVInt(1001)
        self.writeVInt(2264)
        
        self.writeVInt(4)
        self.writeVInt(2)
        
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(1)
        
        count = 0

        self.writeVInt(count)
        
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(200)
        self.writeVInt(-1)
        self.writeVInt(0)
        
        self.writeVInt(100008)
        self.writeVInt(0)
        
        self.writeDataReference(16, self.player.brawler_id)
        
        self.writeString("RU")  # location
        self.writeString(self.player.content_creator)
        
        self.writeVInt(2) # Animation array (count) 
        self.writeInt(4) # [3 = Tokens, 4 = Trophies, 8 = Star Points, 10 = Power Points]
        self.writeInt(self.player.trophyanimation)
        self.writeInt(3) # [3 = Tokens, 4 = Trophies, 8 = Star Points, 10 = Power Points]
        self.writeInt(self.player.tokenanimation)
        self.writeVInt(0) # array
        self.writeVInt(1) # season array
        self.writeVInt(0)
        
        self.writeVInt(0)  # brawl pass tokens
        self.writeVInt(-1)  # premium pass progress
        self.writeVInt(-1)  # free pass progress
        self.writeVInt(0)  # premium pass unlocked boolean
        
        self.writeVInt(1)
        self.writeVInt(0)
         # Brawl Pass End??
        self.writeVInt(1) # array
        self.writeVInt(0)
        self.writeVInt(1)
        
        self.writeVInt(0)
        self.writeVInt(2020141)
        
        self.writeVInt(100)
        self.writeVInt(10)

        for item in range(2):
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(500)
        self.writeVInt(50)
        self.writeVInt(999900)
        
        self.writeVInt(0)  # array

        self.writeVInt(8)  # array

        for i in range(8):
            self.writeVInt(i)
            
        maps = [7]
        count = len(maps)
        self.writeVInt(count)

        for map in maps:

            self.writeVInt(maps.index(map) + 1)
            self.writeVInt(maps.index(map) + 1)
            self.writeVInt(0)  # IsActive | 0 = Active, 1 = Disabled
            self.writeVInt(86400)  # Timer

            self.writeVInt(0)
            self.writeDataReference(15, map)

            self.writeVInt(3)

            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)  # Powerplay game played
            self.writeVInt(0)  # Powerplay game left maximum
            
            self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)  # array
    # Shop array
        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(2)  # array
        self.writeVInt(200)  # Max Tokens
        self.writeVInt(20)  # Plus Tokens

        self.writeVInt(8640)
        self.writeVInt(10)
        self.writeVInt(5)

        self.writeVInt(6)

        self.writeVInt(50)
        self.writeVInt(604800)

        self.writeBoolean(True)  # Box boolean

        self.writeVInt(0)  # array

        self.writeVInt(1)  # Menu Theme
        self.writeInt(1)
        self.writeInt(41000000) # Theme ID

        self.writeVInt(0)  # array

        self.writeInt(0)
        self.writeInt(self.player.low_id)

        self.writeVInt(0)

        self.writeVInt(1)

        self.writeBoolean(True)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(self.player.high_id)  # High Id
        self.writeVInt(self.player.low_id)  # Low Id

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        if self.player.name == "Guest":
            self.writeString("Guest") # player name
            self.writeVInt(0)
        else:
            self.writeString(self.player.name) # player name
            self.writeVInt(1)

        self.writeInt(0)
        self.writeVInt(8)
 # unlocked brawlers array
        self.writeVInt(len(self.player.card_unlock_id))  # count

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeVInt(23)
            self.writeVInt(unlock_id)
            try:
                self.writeVInt(1)
            except:
                self.writeVInt(1)

            if index == 34:
                index += 3
            elif index == 32:
                index += 2
            else:
                index += 1

        # Array
        '''self.writeVInt(5)  # csv id
        self.writeVInt(1)  # resource id
        self.writeVInt(0)  # resource amount

        self.writeVInt(5)  # csv id
        self.writeVInt(8)  # resource id
        self.writeVInt(0)  # resource amount

        self.writeVInt(5)  # csv id
        self.writeVInt(9)  # resource id
        self.writeVInt(0)  # resource amount

        self.writeVInt(5)  # csv id
        self.writeVInt(10)  # resource id
        self.writeVInt(0)  # resource amount'''
        
        # Brawlers Trophies array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(0)

        # Brawlers Trophies for Rank array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(1)

        self.writeVInt(0)  # array

        # Brawlers Upgrade Points array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(1410)

        # Brawlers Power Level array
        self.writeVInt(len(self.player.brawlers_id))  # brawlers count

        for brawler_id in self.player.brawlers_id:
            self.writeDataReference(16, brawler_id)
            self.writeVInt(8)

        # Gadgets and Star Powers array
        '''spgList = []
        for id, level in self.player.Brawler_level.items():
            if level == 8:
                spg = []#Cards.get_unlocked_spg(self, int(id))
                for i in range(len(spg)):
                    spgList.append(spg[i])'''
        self.writeVInt(len(self.player.card_skills_id))  # count

        for skill_id in self.player.card_skills_id:
            self.writeVInt(23)
            self.writeVInt(skill_id)
            self.writeVInt(1)

        # "new" Brawler Tag array
        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(1)
        # Unknown
        self.writeVInt(self.player.gems)  # gems
        self.writeVInt(self.player.gems) # Fre Gems
        self.writeVInt(self.player.player_experience)
        self.writeVInt(100)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(1589967120)
        self.writeInt(65535)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(-33)
        self.writeVInt(-49)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(65535)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(-50)
        self.writeVInt(9)
        self.writeVInt(0)
        self.writeVInt(9)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(65535)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        