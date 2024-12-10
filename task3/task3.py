import json
import sys

values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]

with open(values_path) as json_file:
    values_data = json.load(json_file)

with open(tests_path) as json_file:
    tests_data = json.load(json_file)

def fill_values(tests, values):
    for test in tests:
        if "values" in test:
            fill_values(test["values"], values)
        for value in values:
            if test["id"] == value["id"]:
                test["value"] = value["value"]
                break

fill_values(tests_data["tests"], values_data["values"])

# результат в report.json
with open(report_path, 'w') as f:
    json.dump(tests_data, f, sort_keys=True, indent=2)