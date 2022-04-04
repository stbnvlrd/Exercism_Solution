package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	count := 0
	k := 0
	for ; k <= len(birdsPerDay)-1; k++ {
		count = count + birdsPerDay[k]
	}
	return count
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	count := 0
	k := (week - 1) * 7
	l := k + 6
	for ; k <= l; k++ {
		count = count + birdsPerDay[k]
	}
	return count
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	k := 0
	for k <= len(birdsPerDay)-1 {
		birdsPerDay[k] = birdsPerDay[k] + 1
		k = k + 2
	}
	return birdsPerDay
}
