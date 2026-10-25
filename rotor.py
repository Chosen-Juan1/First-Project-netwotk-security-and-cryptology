from random import shuffle, seed

class rotor():
#we going to need 6 dicts
#each one unique
   entryDicts=[{},{},{}]
   exitDicts=[{},{},{}]
   def __init__(self,strInput):
      self.strInput = strInput
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
   def encrypt(self):
        cipherText = ""
        for char in self.strInput:
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
   def decrypt(self, str2Decrypt):
      plainText = ""
      for char in str2Decrypt:
        if(char == " "):
            plainText += " "
        else:
        #    revExit3 = (for )
           tempNum3 = #need the reverse of each rotor, reverse the dicts

    


    
        
         


if (__name__ == "__main__"):
      
 instance1 = rotor("TESTING MY ROTORS")

 print(instance1.encrypt())