from data_generator import generate_fitness_data
def get_sample_scenarios():
    scenarios = [
        ("P001", "poor_quality",42),
        ("P002", "moderate_activity",43),
        ("P003", "high_activity", 44),
        ("P004", "resting", 45),
        ("P005", "recovery", 46),
    ]
    sample_data = []

    for id, scen, seed in scenarios:
        profile,observations = generate_fitness_data(
            participant_id = id,
            scenario = scen,
            seed = seed,
            number_of_windows= 10
        )
        sample_data.append((profile,observations))
    return sample_data

"""
profile1, observations1 = generate_fitness_data(
    participant_id="P001",
    #scenario="recovery",  #we will test against this
    scenario="poor_quality",
    seed=42,
    number_of_windows=10)
profile2, observations2 = generate_fitness_data(
    participant_id="P002",
    scenario="moderate_activity",
    seed=43,
    number_of_windows=10)
profile3, observations3 = generate_fitness_data(
    participant_id="P003",
    scenario="high_activity",
    seed=44,
    number_of_windows=10)
profile4, observations4 = generate_fitness_data(
    participant_id="P004",
    scenario="resting",
    seed=45,
    number_of_windows=10)
profile5, observations5 = generate_fitness_data(
    participant_id="P005",
    scenario="recovery",
    seed=46,
    number_of_windows=10)

analyzer1 = create_analyzer(profile1, observations1)
analyzer2 = create_analyzer(profile2, observations2)
analyzer3 = create_analyzer(profile3, observations3)
analyzer4 = create_analyzer(profile4, observations4)
analyzer5 = create_analyzer(profile5, observations5)
"""
