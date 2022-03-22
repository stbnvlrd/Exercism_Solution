def round_scores(student_scores):
    """"Round all provided student scores.

    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    round_scores = []
    for x in student_scores:
        round_scores.append(int(round(x)))
        print(x)
    return round_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    failing_scores = 0
    for x in student_scores:
        if x <= 40:
            failing_scores = failing_scores + 1
    return failing_scores


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for x in student_scores:
        if x >= threshold:
            best_scores.append(x)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    letter_range = int((highest - 40)/4)
    list_grade =[]
    for x in range(4):
        x_num = 41 + (letter_range * x)
        list_grade.append(x_num)

    return list_grade


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    students_grade =[]
    for x in range(len(student_scores)):
        
        student_info = str(x+1) + ". " + str(student_names[x]) + ": " + str(student_scores[x])
        students_grade.append(student_info)
        print(student_info)
    return students_grade


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """ 
    if len(student_info) == 0:
        best_student = []
    else:
        for x in range(len(student_info)):
            find_100 = student_info[x]
            print(find_100)
            if 100 in find_100:
                best_student = student_info[x]
                break
            best_student = []
    
    return best_student
