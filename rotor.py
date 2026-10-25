from random import shuffle, seed

class rotor():
#we going to need 6 dicts
#each one unique
   entryDicts=[{},{},{}]
   exitDicts=[{},{},{}]
   revExitRotor3 = {}      #i use this to reverse the dict, found it out through stack overflow (Very cool stuff)
   revEntryRotor3 = {} 
   revExitRotor2 = {}       
   revEntryRotor2 = {} 
   revExitRotor1 = {}       
   revEntryRotor1 = {} 
   alphabetDict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5
                , 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11
            , 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18,
            'T' : 19 , 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}
   letterLists = []
   numberLists = []



   def __init__(self, randSeed):
      seed(randSeed)
      letters1 = list(self.alphabetDict.keys())
      shuffle(letters1)
      self.letterLists.append(letters1)

      letters2 = list(self.alphabetDict.keys())
      shuffle(letters2)
      self.letterLists.append(letters2)

      letters3 = list(self.alphabetDict.keys())
      shuffle(letters3)
      self.letterLists.append(letters3)

      letters4 = list(self.alphabetDict.keys())
      shuffle(letters4)
      self.letterLists.append(letters4)

      letters5 = list(self.alphabetDict.keys())
      shuffle(letters5)
      self.letterLists.append(letters5)

      letters6 = list(self.alphabetDict.keys())
      shuffle(letters6)
      self.letterLists.append(letters6)


      positions1 = list(self.alphabetDict.values())
      shuffle(positions1)
      self.numberLists.append(positions1)

      positions2 = list(self.alphabetDict.values())
      shuffle(positions2)
      self.numberLists.append(positions2)

      positions3 = list(self.alphabetDict.values())
      shuffle(positions3)
      self.numberLists.append(positions3)

      positions4 = list(self.alphabetDict.values())
      shuffle(positions4)
      self.numberLists.append(positions4)

      positions5 = list(self.alphabetDict.values())
      shuffle(positions5)
      self.numberLists.append(positions5)

      positions6 = list(self.alphabetDict.values())
      shuffle(positions6)
      self.numberLists.append(positions6)

      for i in range(0,3):
         for letters, numbers in zip(self.letterLists[i], self.numberLists[i]):
            # print(numberLists)
            if(letters not in self.entryDicts[i]):
               self.entryDicts[i][letters] = numbers

      for i in range(3,6):
         for numbers, letters in zip(self.numberLists[i], self.letterLists[i]):
            if(letters not in self.exitDicts[i-3]):
               self.exitDicts[i-3][numbers] = letters

      self.revEntryRotor1 = {value: key for key,value in self.entryDicts[0].items()}
      self.revExitRotor1 = {value: key for key,value in self.exitDicts[0].items()}

      self.revEntryRotor2 = {value: key for key,value in self.entryDicts[1].items()}
      self.revExitRotor2 = {value: key for key,value in self.exitDicts[1].items()}

      self.revEntryRotor3 = {value: key for key,value in self.entryDicts[2].items()}
      self.revExitRotor3 = {value: key for key,value in self.exitDicts[2].items()}      #i use this to reverse the dict, found it out through stack overflow (Very cool stuff)




   def rotate(self):
      self.letterLists = []
      self.numberLists = []
      self.entryDicts=[{},{},{}]
      self.exitDicts=[{},{},{}]

      letters1 = list(self.alphabetDict.keys())
      shuffle(letters1)
      self.letterLists.append(letters1)

      letters2 = list(self.alphabetDict.keys())
      shuffle(letters2)
      self.letterLists.append(letters2)

      letters3 = list(self.alphabetDict.keys())
      shuffle(letters3)
      self.letterLists.append(letters3)

      letters4 = list(self.alphabetDict.keys())
      shuffle(letters4)
      self.letterLists.append(letters4)

      letters5 = list(self.alphabetDict.keys())
      shuffle(letters5)
      self.letterLists.append(letters5)

      letters6 = list(self.alphabetDict.keys())
      shuffle(letters6)
      self.letterLists.append(letters6)


      positions1 = list(self.alphabetDict.values())
      shuffle(positions1)
      self.numberLists.append(positions1)

      positions2 = list(self.alphabetDict.values())
      shuffle(positions2)
      self.numberLists.append(positions2)

      positions3 = list(self.alphabetDict.values())
      shuffle(positions3)
      self.numberLists.append(positions3)

      positions4 = list(self.alphabetDict.values())
      shuffle(positions4)
      self.numberLists.append(positions4)

      positions5 = list(self.alphabetDict.values())
      shuffle(positions5)
      self.numberLists.append(positions5)

      positions6 = list(self.alphabetDict.values())
      shuffle(positions6)
      self.numberLists.append(positions6)

      for i in range(0,3):
         for letters, numbers in zip(self.letterLists[i], self.numberLists[i]):
            # print(numberLists)
            if(letters not in self.entryDicts[i]):
               self.entryDicts[i][letters] = numbers


      for i in range(3,6):
         for numbers, letters in zip(self.numberLists[i], self.letterLists[i]):
            if(letters not in self.exitDicts[i-3]):
               self.exitDicts[i-3][numbers] = letters


   def printDicts(self):
    print(self.entryDicts,"\n")
    print(self.exitDicts)
    return
#    def resetRotors
   def encrypt(self, plainText):
        cipherText = ""
        for char in plainText:
            if(char == " "):
                cipherText += " "
            else:
                tempNum1 = self.entryDicts[0][char]
                tempLetter1 = self.exitDicts[0][tempNum1]


                tempNum2 = self.entryDicts[1][tempLetter1]
                tempLetter2 = self.exitDicts[1][tempNum2]


                tempNum3 = self.entryDicts[2][tempLetter2]
                cipherLetter = self.exitDicts[2][tempNum3]
                cipherText += cipherLetter
        self.revEntryRotor1 = {value: key for key,value in self.entryDicts[0].items()}
        self.revExitRotor1 = {value: key for key,value in self.exitDicts[0].items()}

        self.revEntryRotor2 = {value: key for key,value in self.entryDicts[1].items()}
        self.revExitRotor2 = {value: key for key,value in self.exitDicts[1].items()}
        
        self.revEntryRotor3 = {value: key for key,value in self.entryDicts[2].items()}
        self.revExitRotor3 = {value: key for key,value in self.exitDicts[2].items()}  
        self.rotate()

    #i use this to reverse the dict, found it out through stack overflow (Very cool stuff)

        return(cipherText)


   def decrypt(self, cipherText):
      plainText = ""
      for char in cipherText:

        if(char == " "):
            plainText += " "
        else:
           tempNum3 = self.revExitRotor3[char]
           tempLetter2 = self.revEntryRotor3[tempNum3]

           tempNum2 = self.revExitRotor2[tempLetter2]
           tempLetter1 = self.revEntryRotor2[tempNum2]

           tempNum1 = self.revExitRotor1[tempLetter1]
           plainLetter = self.revEntryRotor1[tempNum1]
           plainText += plainLetter
      return(plainText)


    


if (__name__ == "__main__"):
      
 instance1 = rotor(randSeed=42)
#  instance1.printDicts()
 cipherText = instance1.encrypt("NEW YEAR")
 print(f"\nCipher text: {cipherText}\n")

#  instance1.printDicts()

 pt = instance1.decrypt(cipherText)
 print(f"Plain text: {pt}")

 print("\nTesting rotation of rotors after first encryption: ")
 cipherText = instance1.encrypt("NEW YEAR")
 print(f"\nSecond Cipher text: {cipherText}\n")

#  instance1.printDicts()

 pt = instance1.decrypt(cipherText)
 print(f"Second Plain text: {pt}")

 print("\n\nNow, for the others: \n")

 cipherText = instance1.encrypt("HELLO")
 print(f"Cipher text: {cipherText}\n")

#  instance1.printDicts()

 pt = instance1.decrypt(cipherText)
 print(f"Plain text: {pt}\n")


 cipherText = instance1.encrypt("HOPE")
 print(f"Cipher text: {cipherText}\n")

#  instance1.printDicts()

 pt = instance1.decrypt(cipherText)
 print(f"Plain text: {pt}\n")




