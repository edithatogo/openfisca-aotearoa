"""This module provides eligibility rates for Orphan's Benefit under Schedule 4, Part 4."""

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class schedule_4__part4_1(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784874.html"
    label = "Part 4 Orphan's Benefit - Clause 1 (eligible caregiver)"

    def formula_2018_11_26(persons, period, parameters):
        is_principal_caregiver = persons("social_security__principal_caregiver", period)
        is_carer_for_one_year = persons("social_security__principal_carer_for_one_year_from_application_date", period)
        has_orphaned_child = persons.family("social_security__orphaned_child_in_family", period)

        return is_principal_caregiver * is_carer_for_one_year * has_orphaned_child
