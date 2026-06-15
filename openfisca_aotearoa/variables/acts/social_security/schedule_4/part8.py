"""This module provides eligibility rates for Emergency Benefit under Schedule 4, Part 8."""

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part8_1(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784889.html"
    label = "Part 8 Emergency Benefit - Clause 1 (person granted emergency benefit)"

    def formula_2018_11_26(persons, period, parameters):
        return persons("emergency_benefit__granted", period)
