from random import shuffle, seed

class rotor():
#we going to need 6 dicts
#each one unique
   entryDicts=[{},{},{}]
   exitDicts=[{},{},{}]
   def __init__(self):
      seed(42)

      alphabetDict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5
                , 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11
            , 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18,
            'T' : 19 , 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}


      letterLists = []
      numberLists = []
      letters1 = list(alphabetDict.keys())
      shuffle(letters1)
      letterLists.append(letters1)

      letters2 = list(alphabetDict.keys())
      shuffle(letters2)
      letterLists.append(letters2)

      letters3 = list(alphabetDict.keys())
      shuffle(letters3)
      letterLists.append(letters3)

      letters4 = list(alphabetDict.keys())
      shuffle(letters4)
      letterLists.append(letters4)

      letters5 = list(alphabetDict.keys())
      shuffle(letters5)
      letterLists.append(letters5)

      letters6 = list(alphabetDict.keys())
      shuffle(letters6)
      letterLists.append(letters6)


      positions1 = list(alphabetDict.values())
      shuffle(positions1)
      numberLists.append(positions1)

      positions2 = list(alphabetDict.values())
      shuffle(positions2)
      numberLists.append(positions2)

      positions3 = list(alphabetDict.values())
      shuffle(positions3)
      numberLists.append(positions3)

      positions4 = list(alphabetDict.values())
      shuffle(positions4)
      numberLists.append(positions4)

      positions5 = list(alphabetDict.values())
      shuffle(positions5)
      numberLists.append(positions5)

      positions6 = list(alphabetDict.values())
      shuffle(positions6)
      numberLists.append(positions6)

      for i in range(0,3):
         for letters, numbers in zip(letterLists[i], numberLists[i]):
            # print(numberLists)
            if(letters not in self.entryDicts[i]):
               self.entryDicts[i][letters] = numbers

      for i in range(3,6):
         for numbers, letters in zip(numberLists[i], letterLists[i]):
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
        return(cipherText)
   def decrypt(self, cipherText):
      plainText = ""
      for char in cipherText:

        if(char == " "):
            plainText += " "
        else:
           revExitRotor3 = {value: key for key,value in self.exitDicts[2].items()} #i use this to reverse the dict, found it out through stack overflow (Very cool stuff)
           tempNum3 = revExitRotor3[char]
           revEntryRotor3 = {value: key for key,value in self.entryDicts[2].items()}
           tempLetter2 = revEntryRotor3[tempNum3]

           revExitRotor2 = {value: key for key,value in self.exitDicts[1].items()}
           tempNum2 = revExitRotor2[tempLetter2]
           revEntryRotor2 = {value: key for key,value in self.entryDicts[1].items()}
           tempLetter1 = revEntryRotor2[tempNum2]

           revExitRotor1 = {value: key for key,value in self.exitDicts[0].items()}
           tempNum1 = revExitRotor1[tempLetter1]
           revEntryRotor1 = {value: key for key,value in self.entryDicts[0].items()}
           plainLetter = revEntryRotor1[tempNum1]
           plainText += plainLetter
      return(plainText)


    


if (__name__ == "__main__"):
      
 instance1 = rotor()
 cipherText = instance1.encrypt("TESTING MY ROTORS")
 print(f"Cipher text: {cipherText}")


 pt = instance1.decrypt(cipherText)
 print(f"Plain text: {pt}")