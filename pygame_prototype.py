from itertools import product
from random import shuffle, choice
import pygame
import os
import sys


def pause(time):
	clock = pygame.time.Clock()
	current_time= pygame.time.get_ticks()
	exit_time = current_time + time
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		current_time = pygame.time.get_ticks()
		if current_time >= exit_time:
			paused = False
		clock.tick(5)


def load_image(filename):
	return pygame.image.load('assets/' + filename)


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


def display_cards(screen, hand, pos: tuple):
	x, y = pos[0], pos[1]
	for card in hand:
		card_type = card[0] + card[1]
		card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
		screen.blit(card_asset, (x, y))
		x -= 30
		y -= 30


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


	
	def play(self):
		"""Start a game sequence."""


		self.deck = self.random_deck()

		pygame.init()
		font = pygame.font.Font(('assets/ARCADECLASSIC.TTF'), 40)
		background = load_image('background.png')
		screen = pygame.display.set_mode((1920, 1080))

		# Deal cards
		your_hand = [self.deck.pop(), self.deck.pop()]
		dealers_hand = [self.deck.pop(), self.deck.pop()]

		
		screen.blit(background, (0, 0))
		pygame.display.update()


		# Dealing sequence
		card = your_hand[0]
		card_type = card[0] + card[1]
		card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
		screen.blit(card_asset, (750, 650))
		pygame.display.update()
		pause(500)
		card = dealers_hand[0]
		card_type = card[0] + card[1]
		card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
		screen.blit(card_asset, (750, 150))
		pygame.display.update()
		pause(500)
		card = your_hand[1]
		card_type = card[0] + card[1]
		card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
		screen.blit(card_asset, (720, 620))
		pygame.display.update()
		pause(500)
		card_asset = pygame.transform.scale(load_image('red_back.png'), (172, 264))
		screen.blit(card_asset, (550, 150))
		pygame.display.update()
		pause(1000)

		if get_score(your_hand) == 21:

			screen.blit(font.render('Blackjack!', False, (255, 255, 0)), (750, 650))
		
		if get_score(dealers_hand) == 21:
			card = dealers_hand[1]
			card_type = card[0] + card[1]
			card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
			screen.blit(card_asset, (550, 150))
			pause(1000)
			screen.blit(font.render('Blackjack!', False, (255, 255, 0)), (750, 150))

		pygame.display.update()

		if get_score(your_hand) == 21 and get_score(dealers_hand) == 21:
			screen.blit(font.render('Draw!', False, (255, 255, 0)), (750, 450))
			pygame.display.update()
			return

		
		else:

			your_turn = True
			you_lost = False
			while your_turn:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:	# Press ENTER to hit
							your_hand.append(self.deck.pop())
							pass
						if event.key == pygame.K_ESCAPE:	# Press ESCAPE to stand
							your_turn = False

				#screen.fill((0, 75, 0))	# Draw background
				screen.blit(background, (0, 0))

				x, y = 750, 650
				for card in your_hand:
					card_type = card[0] + card[1]
					card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
					screen.blit(card_asset, (x, y))
					x -= 30
					y -= 30

				your_score = get_score(your_hand)
				screen.blit(font.render(str(your_score), False, (255, 255, 0)), (850, 950))

				card = dealers_hand[0]
				card_type = card[0] + card[1]
				card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
				screen.blit(card_asset, (750, 150))
				card_asset = pygame.transform.scale(load_image('red_back.png'), (172, 264))
				screen.blit(card_asset, (550, 150))

				shown_card = [dealers_hand[0]]
				dealers_score = get_score(shown_card)
				screen.blit(font.render(str(dealers_score), False, (255, 255, 0)), (850, 100))

				if your_score == 21:
					pygame.display.update()
					your_turn = False
					pause(5000)
				if your_score > 21:
					screen.blit(font.render('Bust!', False, (255, 255, 0)), (750, 450))
					your_turn = False
					you_lost = True
					pygame.display.update()
					pause(1000)

				pygame.display.update()


			if not you_lost:	# Dealer's turn

				dealer_lost = False

				pause(1000)
				card = dealers_hand[0]
				card_type = card[0] + card[1]
				card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
				screen.blit(card_asset, (750, 150))
				card = dealers_hand[1]
				card_type = card[0] + card[1]
				card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
				screen.blit(card_asset, (550, 150))
				screen.blit(font.render(str(dealers_score), False, (255, 255, 0)), (850, 100))
				pygame.display.update()
				pause(1000)

				if get_score(dealers_hand) > 21:
					screen.blit(font.render('Bust!', False, (255, 255, 0)), (750, 350))
					dealer_lost = True
					pygame.display.update()
					pause(1000)



				dealers_turn = True
				while dealers_turn and not dealer_lost:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()

					screen.blit(background, (0, 0))

					x, y = 750, 650

					display_cards(screen, your_hand, (750, 650))

					your_score = get_score(your_hand)
					screen.blit(font.render(str(your_score), False, (255, 255, 0)), (850, 950))
					screen.blit(font.render(str(dealers_score), False, (255, 255, 0)), (850, 425))


					x, y = 750, 150
					for card in dealers_hand:
						card_type = card[0] + card[1]
						card_asset = pygame.transform.scale(load_image(card_type + '.png'), (172, 264))
						screen.blit(card_asset, (x, y))
						x -= 30
						y -= 30


					dealers_score = get_score(dealers_hand)

					if dealers_score > your_score and dealers_score <= 21:
						screen.blit(font.render('Dealer Wins!', False, (255, 255, 0)), (750, 450))
						pause(1000)
						dealers_turn = False
					elif dealers_score < 17 and dealers_score <= your_score:
						pause(100)
						screen.blit(font.render('Dealer  Hits!', False, (255, 255, 0)), (750, 450))
						dealers_hand.append(self.deck.pop())
						pause(1000)
					elif dealers_score > 17:
						screen.blit(font.render('Dealer  Stands! You Win!', False, (255, 255, 0)), (750, 450))
						dealers_turn = False
						pygame.display.update()
						pause(2000)

					

					pygame.display.update()
					pause(1000)





		# pause(5000)



		
		
		






a = Game()

while True:
	a.play()

