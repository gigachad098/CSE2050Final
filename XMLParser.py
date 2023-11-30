from lxml import etree
from Question import Question

def parse(filename):
    
    # Open file and read XML tree from XML file
    file = open(filename, "rb")
    tree = etree.fromstring(file.read())
    
    question_list = []
    # For each question...
    for question in tree.getchildren():
        # Make sure this current item is a question (there is some header info)
        if question.tag != "question":
            continue
        
        # Get the children of the question
        parts = question.getchildren()
        # Initialize question variables
        question_text = ""
        question_image_path = None
        answers = []
        correct_answer = None
        answer_comments = ""
        # For each child of the question XML
        for part in parts:
            # Test for which part of the question it is, and store it accordingly
            if part.tag == "questionText":  
                question_text = part.text.strip()
            elif part.tag == "questionImage":
                question_image_path = part.get("path")
                image_file = open(question_image_path, "rb")
                image = image_file.read()
            elif part.tag == "answer":
                answers.append(part.text.strip())
                if part.get("correct") == "true":
                    correct_answer = part.text.strip()
            elif part.tag == "answerComments":
                answer_comments = part.text.strip()
        
        # If there is no image associated with the question...
        if question_image_path == None:
            tempquestion = Question(question_text, correct_answer, answers, answer_comments, None)
            question_list.append(tempquestion)
        else:
            tempquestion = Question(question_text, correct_answer, answers, answer_comments, image)
            question_list.append(tempquestion)
            # Otherwise...

    return question_list
