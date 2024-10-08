import csv
import json
import random
from io import StringIO

import yaml


def pick_random_file_format(avoid_format=None):
    formats = ['json', 'csv', 'markdown', 'plain text', 'yaml']
    if avoid_format is not None:
        formats.remove(avoid_format)
    format = random.choice(formats)

    if format == 'yaml' and random.choice([True, False]):
        format = 'yml'

    return format


class TabularDataFormatter:
    def __init__(self, data: list[dict]):
        self.data = data  # Expecting a list of dictionaries

    def to_markdown(self) -> str:
        headers = self.data[0].keys()
        lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
        for row in self.data:
            lines.append("| " + " | ".join(str(row[key]) for key in headers) + " |")
        return "\n".join(lines)

    def to_csv(self) -> str:
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=self.data[0].keys())
        writer.writeheader()
        writer.writerows(self.data)
        return output.getvalue()

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

    def to_yaml(self) -> str:
        return yaml.safe_dump(self.data)

    def to_yml(self) -> str:
        return yaml.safe_dump(self.data)

    def to_plain_text(self) -> str:
        text = ""
        for row in self.data:
            text += " | ".join(f"{key}: {value}" for key, value in row.items()) + "\n"
        return text

    def to(self, format_name: str) -> str:
        return getattr(self, f'to_{format_name.replace(" ", "_")}')()
