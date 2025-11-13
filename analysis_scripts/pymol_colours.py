from pymol import cmd
import ast

# Define the file path to load colors
color_file = r"C:\Users\emfla\Desktop\Favour\CodeStuff\PYMOl_Prot_color_index_SAPI.txt"  # Change this to your actual file path

# Function to read colors from a file and parse them correctly
def load_colors_from_file(file_path):
    colors = []
    with open(file_path, "r") as f:
        for line in f:
            try:
                # Convert line to a Python object
                parsed = ast.literal_eval(line.strip())  # Parse as list
                
                # Check if it's a double-bracketed list (nested list)
                if isinstance(parsed, list) and len(parsed) == 1 and isinstance(parsed[0], list):
                    rgb = parsed[0][0]  # Extract the inner list
                else:
                    rgb = parsed[0][0]  # Already in the correct format
                
                # Ensure valid RGB format
                if isinstance(rgb, list) and len(rgb) == 3:
                    colors.append(rgb)
                else:
                    print(f"Skipping invalid line: {line.strip()} (not a valid RGB list)")
            except (ValueError, SyntaxError):
                print(f"Skipping invalid line: {line.strip()} (format error)")
    return colors


# Load colors from the file
colors = load_colors_from_file(color_file)

# Define the first atom index (adjust as needed)
first_atom_index = 11160  # Change this to the correct starting index

# Ensure colors are loaded
if not colors:
    print("Error: No valid colors found in the file.")
else:
    # Loop through colors and apply to corresponding atom indices
    for i, color in enumerate(colors):
        color_name = f"color_{i+1}"  # Unique color name
        atom_id = first_atom_index + i + 1 # Calculate atom index

        # Define color in PyMOL
        cmd.set_color(color_name, color)

        # Apply color to atom by index
        cmd.color(color_name, f"id {atom_id}")

    print(f"Successfully colored {len(colors)} atoms using colors from {color_file}.")
