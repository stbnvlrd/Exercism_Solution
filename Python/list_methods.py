"""
Chaitana's Colossal Coaster
Chaitana owns a very popular theme park. She only has one ride in the very center of beautifully landscaped grounds: The Biggest Roller Coaster in the World(TM). Although there is only this one attraction, people travel from all over the world and stand in line for hours for the opportunity to ride Chaitana's hypercoaster.

There are two queues for this ride, each represented as a list:

Normal Queue
Express Queue (also known as the Fast-track) - where people pay extra for priority access.
You have been asked to write some code to better manage the guests at the park. You need to implement the following functions as soon as possible before the guests (and your boss, Chaitana!) get cranky.
"""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if ticket_type == 1:
        queue_line = express_queue
        queue_line.append(person_name)
    else:
        queue_line = normal_queue
        queue_line.append(person_name)
    return queue_line


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    for count, i in enumerate(queue):
        if i == friend_name:
            friend_place = count
    return friend_place


def add_me_with_my_friends(queue, index, person_name):
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """

    for count, i in enumerate(queue):
        if i == person_name:
            mean_person = count
    queue.pop(mean_person)
    return queue


def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """

    name_count = 0
    for count, i in enumerate(queue):
        if i == person_name:
            name_count = name_count + 1
    return name_count


def remove_the_last_person(queue):
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    person_name = queue[-1]
    queue.pop()
    return person_name


def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    queue.sort()
    return queue
