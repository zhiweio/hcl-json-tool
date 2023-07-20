package main

import (
	"fmt"
	"github.com/hashicorp/hcl/v2"
	"github.com/hashicorp/hcl/v2/hclwrite"
	"github.com/hashicorp/hcl/v2/json"
	"log"
	"os"
)

func addAttrToHCL(attrs hcl.Attributes, body *hclwrite.Body) {
	for name, attr := range attrs {
		val, diags := attr.Expr.Value(nil)
		if diags.HasErrors() {
			log.Fatalf("Error evaluating attribute %s: %s", name, diags.Error())
		}

		body.SetAttributeValue(name, val)
	}
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: json2hcl <input_file.json> <output_file.tf>")
		return
	}

	inputFile := os.Args[1]
	data, diags := json.ParseFile(inputFile)
	if diags.HasErrors() {
		log.Fatalf("Error parsing JSON: %s", diags.Error())
	}

	attrs, diags := data.Body.JustAttributes()
	if diags.HasErrors() {
		log.Fatal(diags.Error())
	}

	hclFile := hclwrite.NewEmptyFile()
	rootBody := hclFile.Body()

	addAttrToHCL(attrs, rootBody)

	// Write HCL file
	outputFile := os.Args[2]
	file, err := os.Create(outputFile)
	if err != nil {
		log.Fatalf("Error creating HCL file: %s", err)
	}
	defer file.Close()

	if _, err := file.Write(hclFile.Bytes()); err != nil {
		log.Fatalf("Error writing to HCL output file: %s", err)
	}

	fmt.Println("Conversion successful. HCL file generated:", outputFile)
}
