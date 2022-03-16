package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	card_value := 0
	switch card {
	case "ace":
		card_value = 11
	case "two":
		card_value = 2
	case "three":
		card_value = 3
	case "four":
		card_value = 4
	case "five":
		card_value = 5
	case "six":
		card_value = 6
	case "seven":
		card_value = 7
	case "eight":
		card_value = 8
	case "nine":
		card_value = 9
	case "ten":
		card_value = 10
	case "jack":
		card_value = 10
	case "queen":
		card_value = 10
	case "king":
		card_value = 10
	default:
		card_value = 0
	}
	return card_value
}

// IsBlackjack returns true if the player has a blackjack, false otherwise.
func IsBlackjack(card1, card2 string) bool {
	return ParseCard(card1)+ParseCard(card2) == 21
}

// LargeHand implements the decision tree for hand scores larger than 20 points.
func LargeHand(isBlackjack bool, dealerScore int) string {
	strategy := ""
	switch isBlackjack {
	case true:
		if dealerScore < 10 {
			strategy = "W"
		} else {
			strategy = "S"
		}
	case false:
		strategy = "P"
	}
	return strategy
}

// SmallHand implements the decision tree for hand scores with less than 21 points.
func SmallHand(handScore, dealerScore int) string {
	strategy := ""
	if handScore >= 17 {
		strategy = "S"
	} else if handScore <= 11 {
		strategy = "H"
	} else {
		if dealerScore >= 7 {
			strategy = "H"
		} else {
			strategy = "S"
		}
	}
	return strategy
}
