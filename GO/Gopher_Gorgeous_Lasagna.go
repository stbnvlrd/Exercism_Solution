package lasagna

// TODO: define the 'OvenTime' constant
const OvenTime = 40

// RemainingOvenTime returns the remaining minutes based on the `actual` minutes already in the oven.
func RemainingOvenTime(actualMinutesInOven int) int {
	RemainingOvenTime := OvenTime - actualMinutesInOven
	return RemainingOvenTime
}

// PreparationTime calculates the time needed to prepare the lasagna based on the amount of layers.
func PreparationTime(numberOfLayers int) (Preparationtime int) {
	Preparationtime = numberOfLayers * 2
	return
}

// ElapsedTime calculates the total time needed to create and bake a lasagna.
func ElapsedTime(numberOfLayers, actualMinutesInOven int) (Elapsedtime int) {
	Elapsedtime = numberOfLayers*2 + actualMinutesInOven
	return
}
