class InvalidRelationError(Exception):
  pass

class Relation:

  FORWARD_RELATIONS = {
    'SON': ['FATHER', 'MOTHER'],
    'DAUGHTER': ['FATHER', 'MOTHER'],
  }

  BACKWARD_RELATIONS = {
    'FATHER': ['SON', 'DAUGHTER'],
    'MOTHER': ['SON', 'DAUGHTER'],
    'BROTHER': ['BROTHER', 'SISTER'],
    'SISTER': ['BROTHER', 'SISTER'],
  }

  @staticmethod
  def __add_relations(from_person, to_person, forward, backward):
    from_person.add_relation(to_person, forward)
    to_person.add_relation(from_person, backward)

  @staticmethod
  def __handle_forward_relations(from_person, to_person, forward, backward):
    valid = backward is None or backward in self.FORWARD_RELATIONS[forward]
    if not valid:
      raise InvalidRelationError(f'Relation from {from_person} to {to_person} is not valid.')
    Relation.__add_relations(from_person, to_person, forward, backward)

  @staticmethod
  def __handle_backward_relations(from_person, to_person, forward, backward):
    valid = forward is None or forward in self.BACKWARD_RELATIONS[backward]
    if not valid:
      raise InvalidRelationError(f'Relation from {from_person} to {to_person} is not valid.')
    Relation.__add_relations(from_person, to_person, forward, backward)

  @staticmethod
  def connect(from_person, to_person, forward=None, backward=None):
    if forward is None and backward is None:
      raise InvalidRelationError(f'Relation from {from_person} to {to_person} is not valid.')
    if forward in Relation.FORWARD_RELATIONS:
      Relation.__handle_forward_relations(from_person, to_person, forward, backward)
    elif backward in Relation.BACKWARD_RELATIONS:
      Relation.__handle_backward_relations(from_person, to_person, forward, backward)
    else:
      raise InvalidRelationError(f'Relation from {from_person} to {to_person} is not valid.')
