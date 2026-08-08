import re


def extract_markdown_images(text):
    return re.finditer(
        r"\!\[([^\]]+)\]\(([^\)]+)\)",
        text
    )