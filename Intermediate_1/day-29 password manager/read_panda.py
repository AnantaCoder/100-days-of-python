import pandas as pd

class PasswordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
        # Load the CSV file into a DataFrame
        try:
            df = pd.read_csv(self.file_path)
            # Normalize the column names
            df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
            df.columns = df.columns.str.lower()  # Convert to lowercase for consistency

            # Adjust column names for usage
            df.rename(columns={'website': 'website', 'username/email': 'username', 'password': 'password'}, inplace=True)
            return df
        except FileNotFoundError:
            print(f"File not found at: {self.file_path}")
            return None

    def search_credentials(self, website):
        if self.df is not None:
            # Search for the specific website
            result = self.df[self.df['website'].str.lower() == website.lower()]

            if not result.empty:
                # Retrieve the website, username, and password
                website = result['website'].values[0]
                username = result['username'].values[0]
                password = result['password'].values[0]

                # Format the result
                output = f"Your website is {website}, your email/username is {username}, and your password is {password}."
                return output
            else:
                return f"No credentials found for website: {website}"
        else:
            return "Data is not loaded properly."

# # Example usage
# file_path = r'D:\Anantacoder_python\100days of code by Angela yu\Days\Intermediate\day-29 password manager\Password_Database.csv'
# search_website = 'ram'

# # Create an instance of the PasswordManager class
# manager = PasswordManager(file_path)

# # Search for credentials
# result = manager.search_credentials(search_website)
# print(result)






















































# import pandas as pd

# def search_website_credentials(file_path, search_website):
#     # Load the CSV file into a DataFrame
#     df = pd.read_csv(file_path)
    
#     # Normalize the column names (if needed)
#     df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces
#     df.columns = df.columns.str.lower()  # Convert to lowercase for consistency
    
#     # Adjust column names for usage
#     df.rename(columns={'website': 'website', 'username/email': 'username', 'password': 'password'}, inplace=True)
    
#     # Search for the specific website
#     result = df[df['website'].str.lower() == search_website.lower()]
    
#     if not result.empty:
#         # Retrieve the username and password
#         website = result['website'].values[0]
#         username = result['username'].values[0]  # Ensure column names match
#         password = result['password'].values[0]  # Ensure column names match
        
#         # Format and print the result
#         output = f"Your website is {website}, your email is {username}, and your password is {password}."
#         print(output)
#     else:
#         print(f"No credentials found for website: {search_website}")

# # Example usage
# file_path = r'D:\Anantacoder_python\100days of code by Angela yu\Days\Intermediate\day-29 password manager\Password_Database.csv'
# search_website = 'ram'
# search_website_credentials(file_path, search_website)
