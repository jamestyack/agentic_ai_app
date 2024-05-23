from crewai import Crew

def create_crew(agents, tasks):
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=2
    )
    return crew