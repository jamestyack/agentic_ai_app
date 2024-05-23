import sys
import os
import warnings

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
warnings.filterwarnings('ignore')

from utils import get_openai_api_key
from agents import create_agents
from tasks import create_tasks
from crew_setup import create_crew
import logging
from IPython.display import Markdown





def main():


    model_name = 'gpt-3.5-turbo'
    get_openai_api_key()
    os.environ["OPENAI_MODEL_NAME"] = model_name

    # learner signs on, wants to cancel
    # look at feedback and behavior
    # what can we show as a deflector

    # product manager: do research on engaged learners to increase their usage of coach and drive engagement
    # how can agentic workflow help me
    # 1: DS - makes query to find engaged learners not using coach
    # 2: Product Research 
    #
    #   - create a research plan with questions for engaged learners to determine why their are not engaging with coach
    #    
    #   - calendar schedule, zoom link
    # 3: Scheduling assistant: recuiting email to learers to get them to sign up
    # 4: outcome.. data and interview notes - categorize, summarize etc... provide as input to.. 


    # 3: Design/product
    #   - Come up with ideas for how to solve the problem
    #   - create a mock? 
    #   - 


    planner, writer, editor = create_agents()
    plan, write, edit = create_tasks(planner, writer, editor)
    crew = create_crew([planner, writer, editor], [plan, write, edit])

    topic = "Great summmer vacations"
    result = crew.kickoff(inputs={"topic": topic})

    print(Markdown(result))

    # topic = "YOUR TOPIC HERE"
    # result = crew.kickoff(inputs={"topic": topic})

    # print(Markdown(result))


if __name__ == '__main__':
    main()