"""
AI Skill Path Optimizer
Goal-aware adaptive recommendation system
Author: MANOHAR
"""


# STEP 1 – Skill Signal Engine

def skill_scores(study_hours, attendance, sleep_hours):
    return {
        "learning_effort": study_hours / 10,
        "discipline": attendance / 100,
        "consistency": sleep_hours / 8
    }



# STEP 2 – Goal-Based Weighting

def weighted_scores(scores, goal):
    weights = {
        "placement": {
            "learning_effort": 1.5,
            "discipline": 1.2,
            "consistency": 1.0
        },
        "internship": {
            "learning_effort": 1.3,
            "discipline": 1.0,
            "consistency": 1.1
        }
    }

    adjusted = {}

    for skill, value in scores.items():
        adjusted[skill] = value * weights[goal][skill]

    return adjusted


# STEP 3 – Priority Optimization

def priority_areas(scores):
    sorted_skills = sorted(
        scores.items(),
        key=lambda x: x[1]
    )
    return [skill for skill, _ in sorted_skills]



# STEP 4 – Goal-Aware Recommendation


def recommend_actions(priorities, scores, goal):
    actions = []

    for skill in priorities[:2]:  # top 2 focus areas

        if skill == "learning_effort":
            if scores[skill] < 0.3:
                actions.append("Urgently increase study hours by 2+ daily")
            else:
                actions.append("Increase focused study time")

        elif skill == "discipline":
            actions.append("Improve attendance & build strict routine")

        elif skill == "consistency":
            actions.append("Fix sleep schedule and maintain consistency")

    if goal == "placement":
        actions.append("Start mock interviews & DSA practice")
    elif goal == "internship":
        actions.append("Build 1 project per month & apply consistently")

    return actions


# MAIN EXECUTION

if __name__ == "__main__":

    print("\n=== AI Skill Path Optimizer ===\n")

    # Example inputs (you can later replace with input())
    study_hours = 5
    attendance = 70
    sleep_hours = 6
    goal = "placement"

    scores = skill_scores(study_hours, attendance, sleep_hours)
    adjusted = weighted_scores(scores, goal)
    priorities = priority_areas(adjusted)
    recommendations = recommend_actions(priorities, scores, goal)

    print("Skill Scores:", scores)
    print("Weighted Scores:", adjusted)
    print("Priority Order:", priorities)

    print("\nRecommended Actions:")
    for action in recommendations:
        print("-", action)
