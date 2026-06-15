"""Variables related to health services and primary care funding under the Pae Ora Act 2022."""

from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class pae_ora__primary_health_organization_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    default_value = True
    label = "Is the person eligible for primary health services under a PHO"
    reference = "https://www.legislation.govt.nz/act/public/2022/0030/latest/LMS521034.html"


class pae_ora__primary_care_copayment_subsidy(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Primary care copayment subsidy amount"
    reference = "https://www.legislation.govt.nz/act/public/2022/0030/latest/LMS521034.html"

    def formula(person, period, parameters):
        # Simplistic mapping: eligible persons receive a standard primary care subsidy
        eligible = person("pae_ora__primary_health_organization_eligible", period)
        return eligible * 15.0
