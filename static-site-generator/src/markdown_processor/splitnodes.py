from src.markdown_processor.regex_extractimages import extract_markdown_images
from src.markdown_processor.regex_extractlinks import extract_markdown_links
from src.nodes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAINTEXT:
            nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Delimiter {delimiter} not closed properly")
        new_nodes = node.text.split(delimiter)

        for idx, new_node in enumerate(new_nodes):
            if idx % 2 != 0:
                nodes.append(TextNode(text=new_node, text_type=text_type))
            else:
                nodes.append(TextNode(text=new_node, text_type=TextType.PLAINTEXT))

    return nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.PLAINTEXT:
            nodes.append(node)
            continue
        matches = extract_markdown_images(node.text)

        cursor = 0
        for match in matches:
            if match.start() != cursor:
                nodes.append(TextNode(text=node.text[cursor:match.start()], text_type=TextType.PLAINTEXT))

            nodes.append(TextNode(text=match.groups()[0], text_type=TextType.IMAGES, url=match.groups()[1]))
            cursor = match.end()
        if cursor != len(node.text):
            nodes.append(TextNode(text=node.text[cursor:], text_type=TextType.PLAINTEXT))

    return nodes

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.PLAINTEXT:
            nodes.append(node)
            continue
        matches = extract_markdown_links(node.text)

        cursor = 0
        for match in matches:
            if match.start() != cursor:
                nodes.append(TextNode(text=node.text[cursor:match.start()], text_type=TextType.PLAINTEXT))

            nodes.append(TextNode(text=match.groups()[0], text_type=TextType.LINK, url=match.groups()[1]))
            cursor = match.end()
        if cursor != len(node.text):
            nodes.append(TextNode(text=node.text[cursor:], text_type=TextType.PLAINTEXT))

    return nodes