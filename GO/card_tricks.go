package cards

// GetItem retrieves an item from a slice at given position. The second return value indicates whether
// the given index exists in the slice or not.
func GetItem(slice []int, index int) (int, bool) {
	if index+1 <= len(slice) && index >= 0 {
		return slice[index], true
	} else {
		return 0, false
	}

}

// SetItem writes an item to a slice at given position overwriting an existing value.
// If the index is out of range the value needs to be appended.
func SetItem(slice []int, index, value int) []int {
	if index+1 <= len(slice) && index >= 0 {
		slice[index] = value
	} else {
		slice = append(slice, value)
	}
	return slice
}

// PrefilledSlice creates a slice of given length and prefills it with the given value.
func PrefilledSlice(value, length int) []int {
	slice := []int{}
	if length <= 0 {
	} else {
		k := 0
		for ; k <= length-1; k++ {
			slice = append(slice, value)
		}

	}
	return slice
}

// RemoveItem removes an item from a slice by modifying the existing slice.
func RemoveItem(slice []int, index int) []int {
	new_slice := []int{}
	if index+1 <= len(slice) && index >= 0 {
		k := 0
		for ; k <= len(slice)-2; k++ {
			if k >= index {
				new_slice = append(new_slice, slice[k+1])
			} else {
				new_slice = append(new_slice, slice[k])
			}

		}
	} else {
		k := 0
		for ; k <= len(slice)-1; k++ {
			new_slice = append(new_slice, slice[k])
		}
	}
	return new_slice
}
