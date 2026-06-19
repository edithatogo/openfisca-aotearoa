"""Variables related to ACC Earners' Levy calculations under the Accident Compensation (Earners' Levy) Regulations."""

import numpy
from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class acc__earners_levy_liable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income liable for the ACC Earners' Levy"
    reference = "https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/"

    def formula(person, period, parameters):
        gross_income = person("income_tax__annual_gross_income", period)
        max_liable = parameters(period).acc.earners_levy.max_threshold
        # Liable income is gross income capped at the maximum threshold
        return numpy.minimum(gross_income, max_liable)


class acc__earners_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Calculated ACC Earners' Levy amount"
    reference = "https://www.legislation.govt.nz/secondary-legislation/pco-drafted/2025/18/en/latest/"

    def formula(person, period, parameters):
        liable_income = person("acc__earners_levy_liable_income", period)
        rate = parameters(period).acc.earners_levy.rate
        return liable_income * rate
