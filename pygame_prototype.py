from itertools import product
from random import shuffle, choice
import pygame
import os
import sys


def screen_sleep(time):
	timer = pygame.time.Clock()
	while True:
		delta_t = timer.tick()
		if delta_t >= time:
			break
	return



def card_image(filename):
	"""Load card graphics from 'cards'-folder."""
	return pygame.image.load('cards/' + filename)


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

		pygame.init()
		myfont = pygame.font.SysFont('Arial', 30)
		screen = pygame.display.set_mode((1000, 1000))

		self.deck = self.random_deck()

		# Deal cards
		your_hand = [self.deck.pop(), self.deck.pop()]
		dealers_hand = [self.deck.pop(), self.deck.pop()]
		
		
		# Dealing "animation"
		deal_sequence = True
		
		while deal_sequence:
			pygame.time.delay(100)
			screen.fill((0, 50, 0))
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			x, y = 500, 650
			for card in your_hand:
				x -= 30
				y -= 30

				card_type = card[0] + card[1]

				card_img = pygame.transform.scale(card_image(card_type + '.png'), (170, 263))

				screen.blit(card_img, (x, y))

				pygame.time.delay(1000)

				pygame.display.update()

			x, y = 500, 150
			for card in dealers_hand:
				x -= 30
				y -= 30

				card_type = card[0] + card[1]

				card_img = pygame.transform.scale(card_image(card_type + '.png'), (170, 263))

				screen.blit(card_img, (x, y))

				pygame.time.delay(1000)

				pygame.display.update()


			break

		your_score = get_score(your_hand)

		if your_score == 21:
			screen.blit(myfont.render('Blackjack!', False, (0, 0, 0)), (500, 500))
			pygame.display.update()
			pygame.time.delay(5000)
		else:

			run = True
			while run:

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:	# Hit
							your_hand.append(self.deck.pop())
						if event.key == pygame.K_ESCAPE:	# Stand
							print('escape')
							run = False


				pygame.time.delay(100)
				screen.fill((0, 50, 0))
				x, y = 500, 650

				for card in your_hand:
					x -= 30
					y -= 30

					card_type = card[0] + card[1]

					card_img = pygame.transform.scale(card_image(card_type + '.png'), (170, 263))

					screen.blit(card_img, (x, y))

				
				dealer_shown_card = dealers_hand[0]
				card_type = dealer_shown_card[0] + dealer_shown_card[1]
				card_img = pygame.transform.scale(card_image(card_type + '.png'), (170, 263))
				screen.blit(card_img, (500, 150))
				card_back_img = pygame.transform.scale(card_image('red_back.png'), (170, 263))
				screen.blit(card_back_img, (700, 150))


				your_score = get_score(your_hand)
				screen.blit(myfont.render(str(your_score), False, (0, 0, 0)), (750, 400))
				
				pygame.display.update()

				

				if your_score > 21:
					pygame.time.delay(500)
					screen.blit(myfont.render('Bust!', False, (0, 0, 0)), (500, 400))
					pygame.display.update()
					while True:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								sys.exit()


			while True:
				print('second loop')
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
				pygame.time.delay(100)
				screen.fill((0, 0, 0))

				for card in your_hand:
					x -= 30
					y -= 30

					card_type = card[0] + card[1]

					card_img = pygame.transform.scale(card_image(card_type + '.png'), (170, 263))

					screen.blit(card_img, (x, y))



				pygame.display.update()







a = Game()
a.play()

