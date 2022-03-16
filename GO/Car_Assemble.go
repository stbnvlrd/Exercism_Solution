package cars

import "fmt"

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) (WorkingCars float64) {
	WorkingCars = float64(productionRate) * successRate / 100
	return
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) (WorkingCars int) {
	WorkingCars = int(float64(productionRate) * successRate / 6000)
	return
}

// CalculateCost works out the cost of producing the given number of cars
func CalculateCost(carsCount int) (calculateCost uint) {
	unit := (carsCount % 10)
	tens := (carsCount - unit) / 10
	calculateCost = uint((tens * 95000) + (unit * 10000))
	fmt.Println("Debug message")
	return
}
