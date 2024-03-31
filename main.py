import csv  # Import the csv module for reading and writing CSV files

while True:
    #display = input('Press enter to continue ----- pre entret fo kontino')
    print('-------------------- Welcome to the main menu Aliens and Humans -------------------- \n\
        Enter an option of your choice ---- echer nu topion fo rou kois\n\
        1. English to Aliench ---- English tre Aliench \n\
        2. Aliench to English ---- Aliench to English \n\
        3. Add a new word ---- adt nuo wurr \n\
        4. Exit ---- Etix'
        )
    
    try:  # to handle errors
        choice = int(input('Choice ---- Kois : '))

        if choice == 1:  # If the user chooses option 1 (English to Aliench)
            # Open the CSV file containing the dictionary for reading
            with open('dictionary.csv','r') as eng:
                reader = csv.reader(eng, delimiter=',')  # Create a CSV reader
                print('English to Aliench')
                find_word = input('Enter an english word : ')  # Prompt user for an English word
                for line in reader:  # Iterate through each line in the CSV file
                    if line[0] == find_word.lower():  # Check if the English word matches
                        print(find_word.lower(), ':', line[1])  # Print the corresponding Aliench word


        elif choice == 2:  # If the user chooses option 2 (Aliench to English)
            # Open the CSV file containing the dictionary for reading
            with open('dictionary.csv','r') as aln:
                reader = csv.reader(aln, delimiter=',')  # Create a CSV reader
                print('Aliench tre English')
                find_word = input('Entro ne alieniish wurr: ')  # Prompt user for an Aliench word
                for line in reader:  # Iterate through each line in the CSV file
                    if line[1] == find_word.lower():  # Check if the Aliench word matches
                        print(find_word, ':', line[0])  # Print the corresponding English word


        elif choice == 3:  # If the user chooses option 3 (Add a new word)
            print('Add a new word ---- adt nuo wurr')
            print('Enter the english word ---- Entro de english wurr')
            eng_word = input(': ')  # Prompt user for a new English word
            print('Enter the alienish word ---- Entro de alienish wurr')
            aln_word = input(': ')  # Prompt user for the corresponding Aliench word
            # Open the CSV file containing the dictionary for appending
            with open('dictionary.csv','a+', newline='') as new:
                new_word = eng_word, aln_word + ' '  # Create a new word pair
                writer = csv.writer(new)  # Create a CSV writer
                writer.writerow(new_word)  # Write the new word pair to the CSV file
                print('Word has been added ---- wurr shukre iatde')  # Confirm word addition
        

        elif choice == 4:
            print('Exiting the program...')
            break  # Exit the loop and terminate the program


        else:  # If the user enters an invalid choice
            print('Invalid entry ---- iroi entrio')  # Print an error message


    except ValueError:  # If the user enters a non-integer value
        print('Invalid entry  ---- iroi entrio')  # Print an error message
    except:  # If any other error occurs
        print('An error has occurred') # Print a generic error message