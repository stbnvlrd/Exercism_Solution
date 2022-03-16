package partyrobot

import (
	"strconv"
)

// Welcome greets a person by name.
func Welcome(name string) string {
	greets := "Welcome to my party, " + name + "!"
	return greets
}

// HappyBirthday wishes happy birthday to the birthday person and exclaims their age.
func HappyBirthday(name string, age int) string {
	age_text := strconv.Itoa(age)
	greets := "Happy birthday " + name + "! You are now " + age_text + " years old!"
	return greets
}

// AssignTable assigns a table to each guest.
func AssignTable(name string, table int, neighbor, direction string, distance float64) string {
	greets := "Welcome to my party, " + name + "!"
	extra_0 := ""
	if table < 10 {
		extra_0 = "00"
	} else if table < 100 && table >= 10 {
		extra_0 = "0"
	}
	table_num := extra_0 + strconv.Itoa(table)
	distance_text := strconv.FormatFloat(distance, 'f', 1, 64)
	table_text := "You have been assigned to table " + table_num + ". Your table is " + direction + ", exactly " + distance_text + " meters from here."
	neighbor_text := "You will be sitting next to " + neighbor + "."
	final_text := greets + "\n" + table_text + "\n" + neighbor_text
	return final_text
}
