import json

api_filter = {
        "createdAt": {
            "gt": "asdf"
        }
    }


print(f"filter={api_filter}")
print(f"filter={json.dumps(api_filter)}")