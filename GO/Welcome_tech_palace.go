package techpalace

import (
	"fmt"
	"strings"
)

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) (welcomeMessage string) {
	welcomeMessage = "Welcome to the Tech Palace, " + strings.ToUpper(customer)
	fmt.Println(welcomeMessage)
	return
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) (welcome_message string) {
	k := 1
	star_line := ""
	for ; k <= numStarsPerLine; k++ {
		star_line = star_line + "*"
	}
	welcome_message = star_line + "\n" + welcomeMsg + "\n" + star_line
	return
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) (clean_message string) {
	message_1 := strings.ReplaceAll(oldMsg, "*", "")
	message_2 := strings.ReplaceAll(message_1, "   ", "")
	message_3 := strings.ReplaceAll(message_2, "\n ", "")
	clean_message = strings.ReplaceAll(message_3, "\n", "")
	return
}
