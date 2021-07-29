import re


class TagManipulator():
    def remove_whitespace(self, word):
        return word.strip()

    def parse_string(self, tags, regex=""):
        result = []

        tempResult = re.split(regex, tags)
        tempResult = [element.strip() for element in tempResult]
        if(len(tempResult[0]) > 0):
            result = tempResult

        return result
