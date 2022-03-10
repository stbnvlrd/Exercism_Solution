// Package weather provides a String with the weather condition of a specific location.
package weather

// CurrentCondition represents de Current weather condition.
var CurrentCondition string

// CurrentLocation represents de Location.
var CurrentLocation string

// Forecast returns a string of the location current weathe location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
