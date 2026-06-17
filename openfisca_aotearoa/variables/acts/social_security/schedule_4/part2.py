"""This module provides eligibility rates for Sole Parent Support under Schedule 4, Part 2."""

import numpy

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part2_1(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784854.html"
    label = "Part 2 Sole Parent Support - Clause 1 (single person with dependent children)"

    def formula_2018_11_26(persons, period, parameters):
        single = numpy.logical_not(persons("social_security__in_a_relationship", period))
        has_dependent_children = persons("social_security__dependent_children", period) > 0
        principal_caregiver = persons(
            "social_security__principal_caregiver",
            period.first_month,
        )
        is_parent_or_principal = persons.has_role(entities.Family.PARENT) + persons.has_role(
            entities.Family.PRINCIPAL,
        )

        return single * has_dependent_children * (principal_caregiver + is_parent_or_principal)
