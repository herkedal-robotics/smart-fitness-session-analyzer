from observation import Observation
from participant import Participant
from fitness_session import FitnessSession
from session_analyzer import SessionAnalyzer

def test_observation_validation():
    valid_observation = Observation(
        timestamp=0,
        heart_rate=75,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.5,
        signal_quality=0.95,
    )
    invalid_observation = Observation(
        timestamp=1,
        heart_rate=275,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.5,
        signal_quality=0.95,
    )
    assert valid_observation.is_valid() is True
    assert invalid_observation.is_valid() is False
    """
    if either assert is wrong -> AssertionError raised
    """
    print("Observation validation test passed!")

test_observation_validation()

def test_get_results():
    participant = Participant(
        participant_id=1,
        baseline_heart_rate=90,
        baseline_skin_response=2.0,
        baseline_temperature=36.5
    )
    session = FitnessSession(participant)

    observation1 = Observation(
        timestamp=0,
        heart_rate=130,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.7,
        signal_quality=0.9
    )
    observation2 = Observation(
        timestamp=1,
        heart_rate=150,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.7,
        signal_quality=0.9
    )
    session.add_observation(observation1)
    session.add_observation(observation2)

    analyzer = SessionAnalyzer(session)
    result = analyzer.get_results()

    assert result["participant_id"] == 1
    assert result["valid_observations"] == 2
    assert result["invalid_observations"] == 0
    assert result["minimum_heart_rate"] == 130
    assert result["maximum_heart_rate"] == 150
    assert result["average_heart_rate"] == 140
    assert result["heart_rate_change"] == 50
    assert result["average_temp_change"] == 0
    assert result["average_activity_level"] == 0.7
    assert result["classification"] == "high_activity"

    print("Get_results test passed!")

test_get_results()


def test_invalid_observation_is_excluded():
    participant = Participant(
        participant_id=2,
        baseline_heart_rate=70,
        baseline_skin_response=2.0,
        baseline_temperature=36.5
    )
    session = FitnessSession(participant)

    valid_observation = Observation(
        timestamp=0,
        heart_rate=100,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.4,
        signal_quality=0.9
    )
    invalid_observation = Observation(
        timestamp=1,
        heart_rate=265,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.9,
        signal_quality=0.9
    )
    session.add_observation(valid_observation)
    session.add_observation(invalid_observation)

    analyzer = SessionAnalyzer(session)
    result = analyzer.get_results()

    assert result["valid_observations"] == 1
    assert result["invalid_observations"] == 1

    assert result["minimum_heart_rate"] == 100
    assert result["maximum_heart_rate"] == 100 #because 265 is excluded
    assert result["average_heart_rate"] == 100
    assert result["heart_rate_change"] == 30
    assert result["average_temp_change"] == 0
    assert result["average_activity_level"] == 0.4
    assert result["classification"] == "moderate_activity"

    print("Invalid observation exclusion test passed!")

test_invalid_observation_is_excluded()


def test_insufficient_data():
    participant = Participant(
        participant_id=3,
        baseline_heart_rate=70,
        baseline_skin_response=2.0,
        baseline_temperature=36.5
    )
    session = FitnessSession(participant)

    invalid_observation = Observation(
        timestamp=0,
        heart_rate=265,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.4,
        signal_quality=0.2
    )
    session.add_observation(invalid_observation)

    analyzer = SessionAnalyzer(session)
    result = analyzer.get_results()

    assert result["valid_observations"] == 0
    assert result["invalid_observations"] == 1

    assert result["average_heart_rate"] is None
    assert result["heart_rate_change"] is None
    assert result["minimum_heart_rate"] is None
    assert result["maximum_heart_rate"] is None
    assert result["average_temp_change"] is None
    assert result["average_activity_level"] is None
    assert result["classification"] == "insufficient_data"

    print("Insufficient data test passed!")

test_insufficient_data()


def test_recovery_classification():
    participant = Participant(
        participant_id=4,
        baseline_heart_rate=70,
        baseline_skin_response=2.0,
        baseline_temperature=36.5
    )
    session = FitnessSession(participant)

    observation1 = Observation(
        timestamp=0,
        heart_rate=160,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.8,
        signal_quality=0.9
    )
    observation2 = Observation(
        timestamp=1,
        heart_rate=150,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.6,
        signal_quality=0.9
    )
    observation3 = Observation(
        timestamp=2,
        heart_rate=140,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.4,
        signal_quality=0.9
    )    
    session.add_observation(observation1)
    session.add_observation(observation2)
    session.add_observation(observation3)

    analyzer = SessionAnalyzer(session)
    result = analyzer.get_results()

    assert result["participant_id"] == 4
    assert result["valid_observations"] == 3
    assert result["invalid_observations"] == 0
    assert result["average_heart_rate"] == 150
    assert result["heart_rate_change"] == 80
    assert result["minimum_heart_rate"] == 140
    assert result["maximum_heart_rate"] == 160
    assert result["average_temp_change"] == 0
    assert result["average_activity_level"] == 0.6
    assert result["classification"] == "recovery"

    print("recovery classification test passed!")

test_recovery_classification()


def test_resting_classification():
    participant = Participant(
        participant_id=5,
        baseline_heart_rate=70,
        baseline_skin_response=2.0,
        baseline_temperature=36.5
    )
    session = FitnessSession(participant)

    observation1 = Observation(
        timestamp=0,
        heart_rate=100,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.2,
        signal_quality=0.9
    )
    observation2 = Observation(
        timestamp=1,
        heart_rate=80,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.2,
        signal_quality=0.9
    )
    observation3 = Observation(
        timestamp=2,
        heart_rate=60,
        skin_response=2.0,
        temperature=36.5,
        activity_level=0.2,
        signal_quality=0.9
    )    
    session.add_observation(observation1)
    session.add_observation(observation2)
    session.add_observation(observation3)

    analyzer = SessionAnalyzer(session)
    result = analyzer.get_results()

    assert result["participant_id"] == 5
    assert result["valid_observations"] == 3
    assert result["invalid_observations"] == 0
    assert result["average_heart_rate"] == 80
    assert result["heart_rate_change"] == 10
    #assert result["average_activity_level"] == 0.2
    assert abs(result["average_activity_level"] - 0.2) < 0.000001
    assert result["classification"] == "resting"

    print("resting classification test passed!")

test_resting_classification()