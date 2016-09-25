import random

def getWords(num):
	wordsFound=[]
	numberOfWords=0
	fin=open("words.txt")
	for line in fin:
		word=line.strip()
		numberOfWords=numberOfWords+1
		if len(word)==numberOfLetters:
			wordsFound.append(word)
	fin.close()		
	return wordsFound		

def replaceAll(guess,word,letter):
	for pos in range(len(guess)):
		if word[pos]==letter:
			guess=guess[:pos]+letter+guess[pos+1:]
	return guess

numberOfLetters=int(raw_input("Enter word length: "))
words=getWords(numberOfLetters)
print "There are {} words with {} letters".format(len(words),numberOfLetters)

guessWord=words[random.randint(0,len(words)-1)]

print "Guessing the word: {}".format(guessWord)

lives=6
guessString="_"*numberOfLetters
while lives>0:
	thisLetter=raw_input("Guess a letter: ")
	if thisLetter in guessWord:
		guessString=replaceAll(guessString,guessWord,thisLetter)
		if guessString==guessWord:
			print "You guessed the word!"
			break
	else:
		lives=lives-1
		print "Letter not found - Lives remaining: {}".format(lives)
	print guessString

print "Game over!"

if lives>0:
	player=raw_input("Enter player name: ")
	fout=open("hangmanScores.txt","a")
	score=lives*numberOfLetters
	newScoreText="{},{}\n".format(player,score)
	fout.write(newScoreText)
	fout.close()

print "Score added to hangmanScores.txt"
	
	
	
		