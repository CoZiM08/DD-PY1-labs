# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(participants_first_group, participants_second_group, delimiter=","):


  first_group_set = set(participants_first_group.split(delimiter))
  second_group_set = set(participants_second_group.split(delimiter))

  common_participants = first_group_set.intersection(second_group_set)
  return sorted(list(common_participants))
