from participant import Participant
from observation import Observation
from fitness_session import FitnessSession
from data_generator import generate_fitness_data
from session_analyzer import SessionAnalyzer
from sample_data import get_sample_scenarios

# we create this function to save some space when creating Participant objects
def create_participant(profile):
    return Participant(
        participant_id=profile["participant_id"],
        baseline_heart_rate=profile["baseline_heart_rate"],
        baseline_skin_response=profile["baseline_skin_response"],
        baseline_temperature=profile["baseline_temperature"]
    )

# define another function because of repetitive code:
def add_observations(session, observations):
    for data in observations:
        observation = Observation(
            timestamp=data["timestamp"],
            heart_rate=data["heart_rate"],
            skin_response=data["skin_response"],
            temperature=data["temperature"],
            activity_level=data["activity_level"],
            signal_quality=data["signal_quality"]
        )
        session.add_observation(observation)

"""
THIS IS REPETITIVE AGAIN, SO WE WANT TO HAVE A FUNCTION FOR IT
participant4 = create_participant(profile4)
session4 = FitnessSession(participant4)
add_observations(session4, observations4)
analyzer4 = SessionAnalyzer(session4)
"""

#define a function that creates analyzer:
def create_analyzer(profile, observations):
    participant = create_participant(profile)
    session = FitnessSession(participant)
    add_observations(session, observations)
    analyzer = SessionAnalyzer(session)
    return analyzer

"""
profile5, observations5 = generate_fitness_data(
    participant_id="P005",
    scenario="recovery",
    seed=46,
    number_of_windows=10)

# from sample_data.py:
# sample_data.append((profile,observations))
"""
for profile, observations in get_sample_scenarios():
    analyzer = create_analyzer(profile,observations)
    analyzer.nicely_presented_results()
    print("------------------------------")
"""
analyzer1 = create_analyzer(profile1, observations1)
analyzer2 = create_analyzer(profile2, observations2)
analyzer3 = create_analyzer(profile3, observations3)
analyzer4 = create_analyzer(profile4, observations4)
analyzer5 = create_analyzer(profile5, observations5)

######TESTING ALL 5 EXAMPLES########
print("")
analyzers = [analyzer1,analyzer2,analyzer3,analyzer4,analyzer5]
for i in analyzers:
    print("----------------------------")
    i.nicely_presented_results()
"""