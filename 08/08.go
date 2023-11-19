package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isVisible(treeLine *[]int, treePos *int) bool {
	visible := false
	// Right or top side of treeLine
	for i := 0; i < *treePos; i++ {
		if (*treeLine)[i] < (*treeLine)[*treePos] {
			visible = true
		} else {
			visible = false
			break
		}
	}
	if !visible {
		// Left or bottom side of treeLine
		for i := len(*treeLine) - 1; i > *treePos; i-- {
			if (*treeLine)[i] < (*treeLine)[*treePos] {
				visible = true
			} else {
				visible = false
				break
			}
		}
	}
	fmt.Printf("%v in position %v is visible? %v\n", (*treeLine)[*treePos], *treePos, visible)
	return visible
}

func main() {
	fmt.Println("Advent of Code 2022 - Day 8")

	file, err := os.Open("input.txt")
	if err != nil {
		panic("File not found")
	}

	scanner := bufio.NewScanner(file)

	forest := [][]int{}

	lengthOfRow := 0

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "")
		treeLine := []int{}
		if lengthOfRow == 0 {
			lengthOfRow = len(line)
		}
		for _, tree := range line {
			height, _ := strconv.ParseInt(tree, 10, 0)
			treeLine = append(treeLine, int(height))
		}
		forest = append(forest, treeLine)
	}
	file.Close()

	// Visible trees from edge
	visibleTrees := lengthOfRow*2 + (len(forest)-2)*2

	// Get visible trees from inside forest
	for i := 1; i < len(forest)-1; i++ {
		for j := 1; j < len(forest[i])-1; j++ {
			// Check height of tree in row
			if isVisible(&forest[i], &j) {
				visibleTrees++
				continue
			}
			// Check height of tree in column
			treeColumn := []int{}
			for i := 0; i < len(forest); i++ {
				treeColumn = append(treeColumn, forest[i][j])
			}
			if isVisible(&treeColumn, &i) {
				visibleTrees++
				continue
			}
		}
	}
	fmt.Println(visibleTrees)
}
