package main

import "fmt"

func main() {
	color1 := []string{"赤", "青", "黄","オレンジ","ピンク"}
	for i := 0; i < len(color1); i++ {
		fmt.Println(color1[i])
	}

}
