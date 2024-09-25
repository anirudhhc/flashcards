class Flashcard:
    def __init__(self, question, answer):
        """
        Constructor for the Flashcard class.
        Initializes a flashcard with a question and an answer.
        """
        self.question = question
        self.answer = answer

    def display_question(self):
        """Displays the question of the flashcard."""
        return self.question

    def check_answer(self, user_answer):
        """
        Checks if the user's answer matches the correct answer.
        :param user_answer: Answer provided by the user.
        :return: True if correct, False otherwise.
        """
        return user_answer.lower() == self.answer.lower()


class FlashcardSet:
    def __init__(self):
        """Constructor for the FlashcardSet class. Initializes an empty list of flashcards."""
        self.flashcards = []

    def add_flashcard(self, question, answer):
        """Adds a flashcard to the set."""
        new_flashcard = Flashcard(question, answer)
        self.flashcards.append(new_flashcard)

    def remove_flashcard(self, question):
        """Removes a flashcard from the set based on the question."""
        self.flashcards = [fc for fc in self.flashcards if fc.question != question]

    def start_practice(self):
        """Simulates a practice session by asking the user questions."""
        for flashcard in self.flashcards:
            print(flashcard.display_question())
            user_answer = input("Your answer: ")
            if flashcard.check_answer(user_answer):
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is: {flashcard.answer}")

flashcard_set = FlashcardSet()
flashcard_set.add_flashcard("What is the capital of France?", "Paris")
flashcard_set.add_flashcard("What is 2 + 2?", "4")
flashcard_set.add_flashcard("Who wrote 'Hamlet'?", "Shakespeare")
