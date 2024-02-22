import os

# Replace 'your_folder_path' with the path to the directory containing your files
folder_path = '/home/nasredine/dev/llm_learning/Arabic Newspapers Corpus/علمية وتقنية'
output_file_path = 'arabic_tech_news.txt'

# Initialize a variable to hold the concatenated content
concatenated_content = ''

# Loop through each file in the directory
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Make sure to only process files (and avoid directories)
    if os.path.isfile(file_path):
        # Open and read the content of the file using the correct encoding
        with open(file_path, 'r', encoding='windows-1256') as file:
            content = file.read()
            concatenated_content += content + "\n"  # Add a newline between articles

# Write the concatenated content to a new file with UTF-8 encoding
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(concatenated_content)

print("Files have been concatenated and saved in UTF-8 encoding.")
