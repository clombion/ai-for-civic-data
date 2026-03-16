#!/usr/bin/env python3
"""
Build script for AI for Civic Data.
Reads _cases/*.yaml and _glossary.yaml, injects JSON into template.html,
writes index.html.
"""

import json
import glob
import pathlib
import sys
import yaml


def load_cases():
    cases = []
    for path in sorted(glob.glob("_cases/*.yaml")):
        with open(path) as f:
            case = yaml.safe_load(f)
        # Validate required fields
        required = ["id", "title", "shortDesc", "context", "pipelineTags",
                    "topicTags", "material", "risks", "principles", "prompt"]
        missing = [k for k in required if k not in case]
        if missing:
            print(f"WARNING: {path} missing fields: {missing}", file=sys.stderr)
        cases.append(case)
    return cases


def load_glossary():
    with open("_glossary.yaml") as f:
        return yaml.safe_load(f)


def build():
    cases = load_cases()
    glossary = load_glossary()
    template = pathlib.Path("template.html").read_text(encoding="utf-8")

    output = template.replace("{{CASES_JSON}}", json.dumps(cases, ensure_ascii=False))
    output = output.replace("{{GLOSSARY_JSON}}", json.dumps(glossary, ensure_ascii=False))

    pathlib.Path("index.html").write_text(output, encoding="utf-8")
    print(f"Built index.html — {len(cases)} cases, {len(glossary)} glossary terms")


if __name__ == "__main__":
    build()
