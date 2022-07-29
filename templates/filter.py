import ast
import json
import sys


def filter_on_source_ip(gathered_result, source_ip, match_file, hit_cnt_file):
    match = []
    temp_match_name = []
    for each in gathered_result["acls"]:
        for every in each["aces"]:
            if (
                every.get("source")
                and every["source"].get("address")
                and every["source"]["address"] == source_ip
            ):
                if each["name"] not in temp_match_name:
                    match.append(
                        {
                            "name": each["name"],
                            "acl_type": each["acl_type"],
                            "aces": [every],
                        }
                    )
                    temp_match_name.append(each["name"])
                else:
                    for every_match in match:
                        if every_match["name"] == each["name"]:
                            every_match["aces"].append(every)

    json_obj = json.dumps(match)
    with open(match_file, "w+") as ff:
        json_obj = json.dumps(match)
        ff.write("""{0}""".format(json_obj))

    filter_cmd = []
    for each in match:
        for line in each["aces"]:
            hit_line = line["line"]
            cmd_hitcount = "show access-list | inc {0} line {1}".format(
                each["name"], hit_line
            )
            filter_cmd.append(cmd_hitcount)

    with open(hit_cnt_file, "w") as ff:
        for item in filter_cmd:
            # ff.write("""{0}""".format(ydump))
            ff.write("{0}\n".format(item))

    return filter_cmd


def main():
    test_gather = ast.literal_eval(sys.argv[1])
    match_file = str(sys.argv[2]) + "/match.json"
    filter_ip = str(sys.argv[3])

    hit_cnt_file = str(sys.argv[2]) + "/filter_htcnt_cmd.yml"
    filter_cmd = filter_on_source_ip(
        test_gather["gathered"], filter_ip, match_file, hit_cnt_file
    )


if __name__ == "__main__":
    main()
