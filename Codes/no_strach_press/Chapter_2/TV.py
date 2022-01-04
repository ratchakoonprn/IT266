# TV class

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]  
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0  # constant
        self.VOLUME_MAXIMUM = 10  # constant
        self.volume = self.VOLUME_MAXIMUM // 2  # integer divide
        
    def power(self):
        self.isOn = not self.isOn   # toggle เปลี่ยนสถานะจากปิดเป็นเปิด หรือจากเปิดเป็นปิด

    def volumeUp(self):
        if not self.isOn: #ถ้า self.isOn มีค่าเป็น False (เครื่องปิด) ก็จะไม่ทำอะไร
            return
        if self.isMuted: #ถ้า self.isMuted เป็น True ก็ให้ทำการเปิดเสียง
            self.isMuted = False  # changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1 #หากความดังไม่ถึง 10 ให้เพิ่มระดับเสียงขึ้นอีก 1 ระดับ

    def volumeDown(self):
        if not self.isOn: #ถ้า self.isOn มีค่าเป็น False (เครื่องปิด) ก็จะไม่ทำอะไร
            return
        if self.isMuted: #ถ้า self.isMuted เป็น True ก็ให้ทำการเปิดเสียง
            self.isMuted = False  # changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1 #ถ้าระดับเสียงมากกว่า 1 ให้ทำการลดระดับเสียงลง 1 ระดับ

    def channelUp(self):
        if not self.isOn: #ถ้า self.isOn มีค่าเป็น False (เครื่องปิด) ก็จะไม่ทำอะไร
            return
        self.channelIndex = self.channelIndex + 1 #เปลี่ยนไปยังช่องถัดไป
        if self.channelIndex == self.nChannels: #หากช่อง indexท คือช่องสุดท้าย ก็จะกลับไปที่ช่องเริ่มต้นอีกครั้ง
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn: #ถ้า self.isOn มีค่าเป็น False (เครื่องปิด) ก็จะไม่ทำอะไร
            return
        self.channelIndex = self.channelIndex - 1 #เปลี่ยนไปยังช่องก่อนหน้า
        if self.channelIndex < 0: #หากขณะนี้คือช่องเริ่มต้นการกดลดช่องก็ยังวนไปยังช่องสุดท้ายของลิสต์แทน
            self.channelIndex = self.nChannels - 1    # wrap around to the top channel

    def mute(self):
        if not self.isOn: #ถ้า self.isOn มีค่าเป็น False (เครื่องปิด) ก็จะไม่ทำอะไร
            return
        self.isMuted = not self.isMuted #ทำการปิด หรือ เปิดเสียง

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list of channels, don't do anything

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


# Test code
oTV = TV()  # create the TV object

# Turn the TV on and show the status
oTV.power() # on
oTV.showInfo() # channel 2, volume 5

# Change the channel up twice, and raise the volume twice, show status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Turn the TV off, show status, turn TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Change the Channel to 11
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()

        
            
