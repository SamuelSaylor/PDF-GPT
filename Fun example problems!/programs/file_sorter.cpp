package main

import (
	"fmt"
	"net/http"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the home page")
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "About page")
}

func logRequest(r *http.Request) {
	fmt.Println("Method:", r.Method)
	fmt.Println("URL:", r.URL.Path)
}

func setupRoutes() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		logRequest(r)
		homeHandler(w, r)
	})

	http.HandleFunc("/about", func(w http.ResponseWriter, r *http.Request) {
		logRequest(r)
		aboutHandler(w, r)
	})
}

func main() {
	setupRoutes()

	fmt.Println("Server starting on :8080")

	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		fmt.Println("Server error:", err)
	}

	// filler loop
	for i := 0; i < 50; i++ {
		if i%10 == 0 {
			fmt.Println("Heartbeat", i)
		}
	}
}