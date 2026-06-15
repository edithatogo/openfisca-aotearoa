"""This module provides eligibility rates for Youth Payment under Schedule 4, Part 6."""

import numpy

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part6_1_a(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784879.html"
    label = "Part 6 Youth Payment - Clause 1(a) (single, 16-17, living with parents)"

    def formula_2018_11_26(persons, period, parameters):
        single = numpy.logical_not(persons("social_security__in_a_relationship", period))
        age_16_or_17 = (persons("age", period.first_day) >= 16) * (persons("age", period.first_day) < 18)
        living_with_parents = persons("jobseeker_support__living_with_parent", period)

        return single * age_16_or_17 * living_with_parents


class schedule_4__part6_1_b(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784879.html"
    label = "Part 6 Youth Payment - Clause 1(b) (single, 16-17, not living with parents)"

    def formula_2018_11_26(persons, period, parameters):
        single = numpy.logical_not(persons("social_security__in_a_relationship", period))
        age_16_or_17 = (persons("age", period.first_day) >= 16) * (persons("age", period.first_day) < 18)
        not_living_with_parents = numpy.logical_not(persons("jobseeker_support__living_with_parent", period))

        return single * age_16_or_17 * not_living_with_parents
