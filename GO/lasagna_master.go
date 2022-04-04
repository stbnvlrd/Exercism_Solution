package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, prep_time int) int {

	if prep_time <= 0 {
		return len(layers) * 2
	} else {
		return len(layers) * prep_time
	}

}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (noodles int, sauce float64) {
	for i := 0; i < len(layers); i++ {
		if layers[i] == "sauce" {
			sauce = sauce + 0.2
		} else if layers[i] == "noodles" {
			noodles = noodles + 50
		}

	}

	return
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList []string, my_list []string) (myList []string) {
	for i := 0; i < len(my_list); i++ {
		if my_list[i] == "?" {
			my_list[i] = friendsList[len(friendsList)-1]
		}
	}
	return
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(quantities []float64, scale int) (amounts []float64) {
	for i := 0; i < len(quantities); i++ {
		amounts = append(amounts, quantities[i]*float64(scale)/2)
	}
	return
}
