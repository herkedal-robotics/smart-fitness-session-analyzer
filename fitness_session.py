"""
stores a participant and his/her observations
"""
class FitnessSession:
    def __init__(self, participant):
        self.participant = participant
        self._observations = []

    @property
    def observations(self):
        return tuple(self._observations)

    def add_observation(self, observation):
        self._observations.append(observation)