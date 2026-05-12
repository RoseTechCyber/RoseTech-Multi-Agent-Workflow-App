from agents import planner_agent, coder_agent, critic_agent

def run_workflow(user_request: str):
    plan = planner_agent(user_request)
    code = coder_agent(user_request)
    review = critic_agent(code)

    return {
        "Plan": plan,
        "Code": code,
        "Review": review
    }
