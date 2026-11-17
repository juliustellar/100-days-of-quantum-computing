experiment = {
    "question": "Does noise change Bell correlation?",
    "baseline": "ideal simulator",
    "metric": "same-outcome rate",
    "test": "noisy simulator",
    "limit": "simulation is not hardware evidence",
}

for key, value in experiment.items():
    print(key, "->", value)
