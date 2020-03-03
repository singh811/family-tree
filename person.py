from relation import Relation

class Person():

  def __init__(self, name, gender):
    self._name = name
    self._gender = gender
    self._relations = {}

  @property
  def name(self):
    return self._name

  @property
  def relations(self):
    return self._relations

  def add_relation(self, person, relation):
    entities = self._relations.get(relation, [])
    entities.append(person)
    self._relations[relation] = entities


p1 = Person('Amit', 'Male')
p2 = Person('KK', 'Male')
Relation.connect(p1, p2, backward='SON')
