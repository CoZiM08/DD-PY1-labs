

def find_common_participants(participants_first_group, participants_second_group, delimiter="|"):
  """Возвращает список общих участников из двух групп.

  Участники в группах разделены символом-разделителем.
  """
  first_group_set = set(participants_first_group.split(delimiter))
  second_group_set = set(participants_second_group.split(delimiter))

  common_participants = first_group_set.intersection(second_group_set)
  return list(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка с разделителем отличным от запятой
participants_first_group_with_comma = "Иванов, Петров, Сидоров"
participants_second_group_with_comma = "Петров, Сидоров, Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
print(find_common_participants(participants_first_group_with_comma, participants_second_group_with_comma, delimiter=","))
