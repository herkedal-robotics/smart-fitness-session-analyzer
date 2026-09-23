Smart fitness session analyzer (option A).

Beata, s376634 

Description.
This program analyzes simulated fitness sessions. It checks measurements, calculates minimum, maximum, average values, compares measurements with a baseline of each person, and classifies the session. It also reports invalid observations.

Class design.
- Participant - it stores the participant's baseline measurements,
- Observation - it stores one sensor reading anc checks whether it is valid,
- FitnessSession - it merges together participant and their observations, 
- SessionAnalyzer - calculates results, classifies the session and prints the report.

Composition: The classes work together. FitnessSession stores a participant and their observations. SessionAnalyzer uses the session to calculate results and classify it. I used composition instead of inheritance because the participant, observations, session and analyzer have different jobs (thus they are different objects). None of them needs to be a special type of another class. So inheritance and method overriding are not needed in this project. 

Encapsulation: FitnessSession stores observation list in _observations. This observations property allows reading the list, while add_observation() is used to add new observations. 

Static method: Observation.is_number() checks whether a measurement is numeric without needing a particular observation object.

Assumptions and classification rules. 
Only valid observations are used in calculations. Signal quality must be at least 0.7.

Insufficient data and recovery are checked before the other classifications:
- insufficient data: no valid observations,
- recovery: at least three valid observations, with a heart-rate drop of at least 20 bpm and activity drop of at least 0.3 from the first to the last observation,
- resting: average activity below 0.3 and average heart-rate within 15 bpm of baseline,
- moderate activity: average activity from 0.3 to below 0.6,
- high activity: average activity of at least 0.6.

Run the program and tests (on Windows):

py main.py
py tests.py

No third-party packages are required. The project uses basic Python and standard library.

Example output:
Participant:  P005
Valid observations:  10
Invalid observations:  0

Minimum heart rate:  64.00 bpm
Maximum heart rate:  125.00 bpm
Average heart rate:  97.20 bpm
Heart rate change:  37.20 bpm
Average temp change:  0.28 C
Average activity level:  0.48

Classification:  recovery
Explanation: Heart rate and activity levels declined at the end of the session.

Known limitations.
The data is simulated. Classification uses fixed thresholds and does not provide medical or fitness advice. Recovery is based on the first and last valid observations rather than a detailed trend analysis.

