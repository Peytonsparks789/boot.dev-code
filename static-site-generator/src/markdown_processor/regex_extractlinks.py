import re


def extract_markdown_links(text):
    return re.finditer(
        r"(?<!!)\[([^\]]+)\]\(([^)]+)\)",
        text
    )