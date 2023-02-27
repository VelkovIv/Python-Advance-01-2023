class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if new_name == self.name:
            return "Name cannot be the same."

        self.name = new_name

        return self.name

    def change_due_date(self, new_due_date: str) -> str:
        if new_due_date == self.due_date:
            return "Date cannot be the same."

        self.due_date = new_due_date

        return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if comment_number < 0 or comment_number >= len(self.comments):
            return "Cannot find comment."

        self.comments[comment_number] = new_comment

        return f"{', '.join(self.comments)}"

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"

