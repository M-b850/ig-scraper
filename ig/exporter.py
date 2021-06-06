import json


def export_json(result):
    """ Serializing json """
    with open('sample/output.json', 'w') as f:
        # json_object = json.dumps(result, ensure_ascii=False, indent=4)
        json.dump(
            result,
            f,
            ensure_ascii=False,
            indent=4,
            sort_keys=True,
            default=str
        )
