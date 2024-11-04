def copy_lines(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            #open the output file in write mode
            with open(output_file, 'w') as outfile:
                #iterate through each line in the input file
                for line in infile:
                    # Check if the line ends with " - DONE"
                    if line.strip().endswith(" - DONE"):
                        #write the line to an output file
                        outfile.write(line)
        print(f"Lines ending with ' - DONE' have been copied to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the input and output filenames
input_file = input("Enter the name of the input text file (with .txt extension): ")
output_file = input("Enter the name of the output text file (with .txt extension): ")

# Call the function with the user-provided filenames
copy_lines(input_file, output_file)