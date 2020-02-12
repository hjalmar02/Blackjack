from itertools import product
from random import shuffle, choice
import pygame
import os



face_dict = {
	'S' : 'Spades',
	'H' : 'Hearts',
	'C' : 'Clubs',
	'D' : 'Diamonds'
}

suit_dict = {
	'2' : 'Two',
	'3' : 'Three',
	'4' : 'Four'
}


def get_score(hand):
		score = 0
		for i in range(len(hand)):
				if hand[i][0] == 'J' or hand[i][0] == 'Q' or hand[i][0] == 'K':
					score += 10
				elif hand[i][0] == 'A':
					if score <= 10:
						score += 11
					else:
						score += 1
				else:
					score += int(hand[i][0])
		return score




class Game():

	suits = ['S', 'H', 'C', 'D']
	faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

	def random_deck(cls):
		"""Generate a shuffled deck of cards.

		
		Creates a shuffled list of tuples consisting of a suit (e.g.
		hearts) and a face (e.g. ace).
		"""
		deck = product(cls.faces, cls.suits)
		deck = list(deck)
		shuffle(deck)
		return deck


	def burn(self):
		"""Remove the top card from the deck."""
		self.deck.pop()

	
	def play(self):
		"""Start a game sequence."""

		self.deck = self.random_deck()

		# Deal cards
		your_hand = [self.deck.pop(), self.deck.pop()]
		dealers_hand = [self.deck.pop(), self.deck.pop()]
		while True:
			score = get_score(your_hand)
			dealer_score = get_score(dealers_hand)

			#for i in range(len(your_hand)):
			#	if your_hand[i][0] == 'J' or your_hand[i][0] == 'Q' or your_hand[i][0] == 'K':
			#		score += 10
			#	elif your_hand[i][0] == 'A':
			#		if score <= 10:
			#			score += 11
			#		else:
			#			score += 1
			#	else:
			#		score += int(your_hand[i][0])

			#for i in range(len(dealers_hand)):
			#	if dealers_hand[i][0] == 'J' or dealers_hand[i][0] == 'Q' or dealers_hand[i][0] == 'K':
			#		dealer_score += 10
			#	elif dealers_hand[i][0] == 'A':
			#		if dealer_score <= 10:
			#			dealer_score += 11
			#		else:
			#			dealer_score += 1
			#	else:
			#		dealer_score += int(dealers_hand[i][0])

			print(f'Dealers hand: {dealers_hand}. Score: {dealer_score} \n')
			print(f'Your hand: {your_hand}. Score: {score}\n')
			
			action = input('Hit or Stand? [h/s]: ')
			if action == 's':

				while True:

					if dealer_score < 16 or score > dealer_score:
						dealers_hand.append(self.deck.pop())
						dealer_score = get_score(dealers_hand)
						print(f'Dealer hits, score: {dealer_score}')
						if dealer_score > 21:
								print('Dealer busts! \nYou win!')
								break

					else:
						dealer_action = choice(['h', 's'])
						if dealer_action == 'h':
							dealers_hand.append(self.deck.pop())
							dealer_score = get_score(dealers_hand)
							print(f'Dealer hits, score: {dealer_score}')
							if dealer_score > 21:
								print('Dealer busts! \nYou win!')
								break
						else:
							print(f'Dealer stands, score: {dealer_score}')
							if dealer_score > score:
								print('Dealer wins!')
							elif dealer_score == score:
								print('Draw!')
							else:
								print('You win!')
							break


				break
			else:
				your_hand.append(self.deck.pop())
				score = get_score(your_hand)
				if score > 21:
					print('Bust!\n Dealer wins!')
					break





a = Game()
a.play()

