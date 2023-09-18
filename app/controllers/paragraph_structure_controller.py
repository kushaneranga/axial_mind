import re


class ParagraphStructure:
    """
        A class for processing and formatting paragraphs of text.
    """

    def __init__(self, paragraph):
        self.paragraph = paragraph

    def remove_double_spaces(self):
        # Use regular expression to replace double or more spaces with a single space
        self.paragraph = re.sub(r'\s+', ' ', self.paragraph)

    def remove_line_breaks(self):
        # Replace all newline characters with a space
        self.paragraph = self.paragraph.replace('\n', ' ')

    def capitalize_first_letter(self):
        # Split the text into paragraphs using '\n' as the delimiter
        paragraphs = self.paragraph.split('\n')

        # Initialize a list to store the final result
        result = []

        for paragraph in paragraphs:
            if paragraph.strip():  # Check if the paragraph is not empty after stripping whitespace
                paragraph = paragraph.strip()  # Remove leading and trailing spaces
                paragraph = paragraph[0].upper() + paragraph[1:]

                # Split the paragraph into sentences using '.', '!', or '?' as sentence delimiters
                sentences = re.split(r'(?<=[.!?])\s+', paragraph)

                # Capitalize the first letter of each sentence
                capitalized_sentences = []
                for sentence in sentences:
                    if sentence:
                        sentence = sentence.strip()  # Remove leading and trailing spaces
                        capitalized_sentence = sentence[0].upper() + sentence[1:]
                        capitalized_sentences.append(capitalized_sentence)

                # Join the sentences back into a single paragraph
                capitalized_paragraph = ' '.join(capitalized_sentences)

                result.append(capitalized_paragraph)
            else:
                result.append(paragraph)  # Preserve empty paragraphs

        # Join the paragraphs back into a single string with preserved line breaks
        self.paragraph = '\n'.join(result)
