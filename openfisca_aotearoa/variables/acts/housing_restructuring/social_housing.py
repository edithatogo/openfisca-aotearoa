"""Variables related to social housing eligibility and income-related rent calculations under the Public and Community Housing Management Act 1992."""

from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class housing_restructuring__social_housing_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = False
    label = "Is the person eligible for social housing placement"
    reference = "https://www.legislation.govt.nz/act/public/1992/76/en/latest/"


class housing_restructuring__income_related_rent(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Calculated income-related rent for social housing tenants"
    reference = "https://www.legislation.govt.nz/act/public/1992/76/en/latest/"

    def formula(person, period, parameters):
        eligible = person("housing_restructuring__social_housing_eligible", period)
        income = person("income_tax__annual_gross_income", period.this_year) / 12.0
        # Income-related rent is typically capped at 25% of net income for low-income brackets
        return eligible * (income * 0.25)
