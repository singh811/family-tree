from relation import Relation

class Family:
  def __init__(self):
    self._members = {}

  def add_member(self, person):
    self._members[person.name] = person

  def count_relation(self, of_person, relation, whole_family=False):
    immediate_sons = len(of_person.relations[relation])
    for son in of_person.relations[relation]:
      if son.relations[relation]:
        immediate_sons += self.count_sons(son, whole_family)
    return immediate_sons

  def count_sons(self, of_person):
    return count_relation(of_person, 'SON')

  def count_all_sons(self, of_person):
    return count_relation(of_person, 'SON', whole_family=True)

  def count_daughters(self, of_person):
    return count_relation(of_person, 'DAUGHTER')

  def count_all_daughters(self, of_person):
    return count_relation(of_person, 'DAUGHTER', whole_family=True)
