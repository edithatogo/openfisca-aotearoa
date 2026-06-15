"""This module provides eligibility rates for Young Parent Payment under Schedule 4, Part 7."""

import numpy

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part7_1_a(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784883.html"
    label = "Part 7 Young Parent Payment - Clause 1(a) (single with dependent children)"

    def formula_2018_11_26(persons, period, parameters):
        single = numpy.logical_not(persons("social_security__in_a_relationship", period))
        has_dependent_children = persons("social_security__dependent_children", period) > 0

        return single * has_dependent_children


class schedule_4__part7_1_b(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784883.html"
    label = "Part 7 Young Parent Payment - Clause 1(b) (in a relationship)"

    def formula_2018_11_26(persons, period, parameters):
        return persons("social_security__in_a_relationship", period)
