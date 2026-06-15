"""Jobseeker Support ineligibility provisions under section 26 of the Social Security Act 2018."""

from openfisca_core import holders, periods, variables

from openfisca_aotearoa import entities


class jobseeker_support__full_time_student(variables.Variable):
    value_type = bool
    default_value = False
    entity = entities.Person
    label = "Person is a full-time student (s26(a) ineligibility)"
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/whole.html#DLM6783152"
    set_input = holders.set_input_dispatch_by_period


class jobseeker_support__strike_action(variables.Variable):
    value_type = bool
    default_value = False
    entity = entities.Person
    label = "Person is engaged, or is likely to be engaged, in a strike (s26(b) ineligibility)"
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/whole.html#DLM6783152"
    set_input = holders.set_input_dispatch_by_period


class jobseeker_support__employment_training(variables.Variable):
    value_type = bool
    default_value = False
    entity = entities.Person
    label = "Person has, in MSD's opinion, left employment for the purpose of undertaking employment-related training (s26(c) ineligibility)"
    definition_period = periods.WEEK
    reference = "https://www.legislation.govt.nz/act/public/2018/0032/latest/whole.html#DLM6783152"
    set_input = holders.set_input_dispatch_by_period
