
PLACEHOLDER = '[name]'

# Reading the list of names
with open(r'D:\Anantacoder_python\100days of code by Angela yu\Days\Intermediate\day-24- files , dictionaries\Mail Merge Project Start\Input\Names\invited_names.txt') as file:
    names = file.readlines()  # Get names as a list

# Reading the starting letter template
with open(r'D:\Anantacoder_python\100days of code by Angela yu\Days\Intermediate\day-24- files , dictionaries\Mail Merge Project Start\Input\Letters\starting_letter.txt') as letter_file:
    letter_cont = letter_file.read()  # Read the letter content

# Looping through names and creating personalized letters
for i in names:
    stripped_name = i.strip()  # Remove any extra whitespace/newline
    new_letter = letter_cont.replace(PLACEHOLDER, stripped_name)  # Replace placeholder with name
    # print(new_letter)
    
    # Saving the new letter to the Output folder
    with open(f'Output/ReadyToSend/letter_for_{stripped_name}.md', mode='w') as completed_letter:
        
       completed_letter.write(new_letter)  # Write the new letter into the file
       print(f'Letter for {stripped_name} has been created')  # Confirmation message




'''#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp'''