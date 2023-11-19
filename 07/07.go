package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Advent of code 2022 - 07")

	file, err := os.Open("input.txt")
	if err != nil {
		panic("File not found")
	}

	scanner := bufio.NewScanner(file)

	// Keep track of actual dir route
	dirRoute := []string{}

	dirSizes := map[string]int{}

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")

		if line[0] == "$" {
			// Set actual route
			if line[1] == "cd" && line[2] != ".." {
				dirRoute = append(dirRoute, line[2])
			} else if line[1] == "cd" && line[2] == ".." {
				dirRoute = dirRoute[:len(dirRoute)-1]
			}
			// Creates new route in map
			if _, ok := dirSizes[strings.Join(dirRoute, "/")]; !ok {
				dirSizes[strings.Join(dirRoute, "/")] = 0
			}
		} else {
			if line[0] != "dir" {
				// Adds size of file to current dir and father dirs up to root
				num, _ := strconv.ParseInt(line[0], 10, 0)
				for i := range dirRoute {
					dirSizes[strings.Join(
						dirRoute[:len(dirRoute)-i], "/",
					)] += int(num)
				}
			}
		}
		fmt.Println(dirRoute)
	}

	file.Close()

	fmt.Println(dirSizes)

	// Result for first star
	result := 0
	for _, v := range dirSizes {
		if v <= 100000 {
			result += v
		}
	}
	fmt.Println("SUM OF DIR SIZES BIGGER OR EQUAL TO 100000", result)

	// Result for second start
	usedSpace := dirSizes["/"]
	fmt.Println("TOTAL SPACE IN DISK:", usedSpace)
	emptySpace := 70000000 - usedSpace
	fmt.Println("EMPTY SPACE IN DISK:", emptySpace)
	spaceToDelete := 30000000 - emptySpace
	fmt.Println("SPACE TO DELETE:", spaceToDelete)
	minDelete := 30000000
	for _, v := range dirSizes {
		if v >= spaceToDelete && v < minDelete {
			minDelete = v
		}
	}
	fmt.Println(
		"SIZE OF SMALLEST DIR TO BE DELETED TO GET EMPTY SPACE:",
		minDelete,
	)
}
