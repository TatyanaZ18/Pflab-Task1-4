import json
import sys

values = sys.argv[1]
tests = sys.argv[2]
report = sys.argv[3]

with open(values) as json_file: #values.json
    values = json.load(json_file)
    with open(tests) as json_file: #test.json
        data = json.load(json_file)
        to_json = ""
        h = ""
        c = ""
        g = ""
        with open(report, 'w') as f:
            json.dump(to_json, f, sort_keys=True, indent=2)

        for j in values["values"]:
            for i in data["tests"]:
                if ("values" in i):
                    for t in i["values"]:
                        if (j["id"] == t["id"]):
                            t["value"] = j["value"]
                            h = data["tests"]
                            with open('report.json', 'w') as f:
                                json.dump(h, f, sort_keys=True, indent=2)
                        if ("values" in t):
                            for l in t["values"]:
                                if (j["id"] == l["id"]):
                                    l["value"] = j["value"]
                                    c = data["tests"]
                                    with open('report.json', 'w') as f:
                                        json.dump(
                                            c, f, sort_keys=True, indent=2)
                                if ("values" in l):
                                    for m in l["values"]:
                                        if (j["id"] == m["id"]):
                                            m["value"] = j["value"]
                                            g = data["tests"]
                                            with open('report.json', 'w') as f:
                                                json.dump(
                                                    g, f, sort_keys=True, indent=2)

                if (j["id"] == i["id"]):
                    i["value"] = j["value"]
                    to_json = data["tests"]
                    with open('report.json', 'w') as f:
                        json.dump(to_json, f, sort_keys=True, indent=2)

# with open('report.json') as f:
#     print(f.read())
