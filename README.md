# Smart Fitness Session Analyzer (Option A)

**Student:** Beata, s376634

## Description

This program analyzes simulated fitness sessions. It checks measurements, calculates minimum, maximum and average values, compares measurements with each person's baseline, and classifies the session. It also reports invalid observations.

## Class design

- `Participant` - stores the participant's baseline measurements.
- `Observation` - stores one sensor reading and checks whether it is valid.
- `FitnessSession` - brings together a participant and their observations.
- `SessionAnalyzer` - calculates results, classifies the session and prints the report.

**Composition:** The classes work together. `FitnessSession` stores a participant and their observations. `SessionAnalyzer` uses the session to calculate results and classify it. I used composition instead of inheritance because the participant, observations, session and analyzer have different jobs. None of them needs to be a special type of another class. Therefore, inheritance and method overriding are not needed in this project.

**Encapsulation:** `FitnessSession` stores the observation list in `_observations`. The `observations` property allows reading the observations, while `add_observation()` is used to add new observations.

**Static method:** `Observation.is_number()` checks whether a measurement is numeric without needing a particular observation object.

## Assumptions and classification rules

Only valid observations are used in calculations. Signal quality must be at least 0.7.

Insufficient data and recovery are checked before the other classifications:

- **Insufficient data:** no valid observations.
- **Recovery:** at least three valid observations, with a heart-rate drop of at least 20 bpm and an activity drop of at least 0.3 from the first to the last valid observation.
- **Resting:** average activity below 0.3 and average heart rate within 15 bpm of baseline.
- **Moderate activity:** average activity from 0.3 to below 0.6.
- **High activity:** average activity of at least 0.6.

## Run the program and tests

Clone the repository and open its folder:

```bash
git clone https://github.com/herkedal-robotics/smart-fitness-session-analyzer.git
cd smart-fitness-session-analyzer
```

**On Windows:**

```powershell
py main.py
py tests.py
```

**On Linux/macOS (or systems using `python3`):**

```bash
python3 main.py
python3 tests.py
```

No third-party packages are required. The project uses Python and the standard library.

## Example output

```text
Participant: P005
Valid observations: 10
Invalid observations: 0

Minimum heart rate: 64.00 bpm
Maximum heart rate: 125.00 bpm
Average heart rate: 97.20 bpm
Heart rate change: 37.20 bpm
Average temp change: 0.28 C
Average activity level: 0.48

Classification: recovery
Explanation: Heart rate and activity levels declined at the end of the session.
```

## Known limitations

The data is simulated. Classification uses fixed thresholds and does not provide medical or fitness advice. Recovery is based on the first and last valid observations rather than a detailed trend analysis.

