class LanguageLearningManager:
    def __init__(self):
        self.languages = {
            "spanish": {"levels": ["beginner", "intermediate", "advanced"]},
            "french": {"levels": ["beginner", "intermediate", "advanced"]},
            "german": {"levels": ["beginner", "intermediate", "advanced"]},
            "italian": {"levels": ["beginner", "intermediate", "advanced"]}
        }

    def get_system_prompt(self, language, level):
        return f"""You are a helpful {language} language tutor. The student's level is {level}.
        Please help them learn {language} by:
        1. Responding in {language} with English translations
        2. Correcting any mistakes they make
        3. Keeping the conversation appropriate for their {level} level
        4. Providing helpful tips and explanations when needed"""

    def validate_language(self, language):
        return language.lower() in self.languages

    def validate_level(self, language, level):
        return level.lower() in self.languages[language.lower()]["levels"]