from crewai import Agent, Task, Crew

# Define agents
planner = Agent(
    role="Planner",
    goal="Break down user requests into actionable steps",
    backstory="Strategic thinker who organizes tasks"
)

coder = Agent(
    role="Coder",
    goal="Write Python code to solve tasks",
    backstory="Efficient developer focused on implementation"
)

critic = Agent(
    role="Critic",
    goal="Review outputs for correctness and clarity",
    backstory="Detail-oriented reviewer"
)

# Define tasks
task1 = Task(description="Plan a simple calculator program", agent=planner)
task2 = Task(description="Write Python code for the calculator", agent=coder)
task3 = Task(description="Review the calculator code", agent=critic)

# Orchestrate workflow
crew = Crew(agents=[planner, coder, critic], tasks=[task1, task2, task3])
results = crew.run()

print(results)
