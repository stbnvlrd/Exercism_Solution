package purchase

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	return kind == "car" || kind == "truck"
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in dictionary order.
func ChooseVehicle(option1, option2 string) string {
	Output := ""
	if option1 < option2 {
		Output = option1 + " is clearly the better choice."
	} else {
		Output = option2 + " is clearly the better choice."
	}
	return Output
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {
	Output := 0.0
	if age < 3 {
		Output = originalPrice * 0.8
	} else if age >= 3 && age < 10 {
		Output = originalPrice * 0.7
	} else {
		Output = originalPrice * 0.5
	}
	return Output

}
