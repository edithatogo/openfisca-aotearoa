"""This module provides eligibility rates for Unsupported Child's Benefit under Schedule 4, Part 5."""

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part5_1(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784877.html"
    label = "Part 5 Unsupported Child's Benefit - Clause 1 (eligible caregiver)"

    def formula_2018_11_26(persons, period, parameters):
        return persons("unsupported_child__entitled", period)
