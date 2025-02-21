class TaskRewardSystem:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = {task: False for task in tasks}  # False means incomplete

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True
        else:
            print(f"Task '{task}' not found.")

    def get_completion_level(self):
        completed_tasks = sum(self.tasks.values())
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return 0  # Avoid division by zero
        return (completed_tasks / total_tasks) * 100

    def get_encouragement(self):
        completion = self.get_completion_level()
        if completion == 100:
            return "Excellent job! You've completed all tasks!"
        elif completion >= 75:
            return "Great work! You're almost there!"
        elif completion >= 50:
            return "Nice effort! Keep pushing forward!"
        elif completion > 0:
            return "You're making progress! Keep it up!"
        else:
            return "Let's get started! You can do this!"

    def display_status(self):
        print(f"{self.name}'s Task Progress:")
        for task, completed in self.tasks.items():
            status = "✔" if completed else "✘"
            print(f"[{status}] {task}")
        print(f"Completion: {self.get_completion_level():.2f}%")
        print(self.get_encouragement())

# Example Usage
name = input("Enter your name: ")
tasks = input("Enter tasks separated by commas: ").split(', ')
system = TaskRewardSystem(name, tasks)

while True:
    system.display_status()
    task = input("Enter a task to mark as complete (or type 'exit' to quit): ")
    if task.lower() == 'exit':
        break
    system.complete_task(task)
