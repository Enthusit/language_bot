import api_handler
from db_handler import DatabaseHandler
from language_manager import LanguageLearningManager

class LanguageLearningBot:
    def __init__(self):
        self.db = DatabaseHandler()
        self.language_manager = LanguageLearningManager()
        self.current_session = None

    def setup_session(self):
        print("Welcome to Language Learning Bot!")
        print("Available languages:", ", ".join(self.language_manager.languages.keys()))
        
        while True:
            language = input("\nWhich language would you like to learn? ").lower()
            if self.language_manager.validate_language(language):
                break
            print("Invalid language. Please try again.")

        while True:
            level = input("Choose your level (beginner/intermediate/advanced): ").lower()
            if self.language_manager.validate_level(language, level):
                break
            print("Invalid level. Please try again.")

        self.current_session = self.db.create_session(language, level)
        return language, level

    def run(self):
        language, level = self.setup_session()
        system_prompt = self.language_manager.get_system_prompt(language, level)
        
        print("\nGreat! You can start chatting in your target language.")
        print("Type 'exit' to end the session.")
        print("-" * 50)

        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nThank you for learning! Goodbye!")
                break

            # Combine system prompt with user input
            full_prompt = f"{system_prompt}\n\nUser: {user_input}"
            
            print("\nBot: ", end="")
            response = api_handler.get_response(full_prompt)
            print(response)
            
            # Save conversation to database
            self.db.save_conversation(self.current_session, user_input, response)
            print("-" * 50)

if __name__ == "__main__":
    bot = LanguageLearningBot()
    bot.run()