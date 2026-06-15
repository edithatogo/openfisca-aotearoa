"""Variables related to compliance, timelines, and filing declarations under the Tax Administration Act 1994."""

from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class tax_admin__automatic_tax_assessment(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    default_value = True
    label = "Is the person eligible for automatic tax assessment"
    reference = "https://www.legislation.govt.nz/act/public/1994/0166/latest/DLM342465.html"


class tax_admin__filing_deadline_months_after_year_end(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Standard individual filing deadline in months after the end of the tax year"
    reference = "https://www.legislation.govt.nz/act/public/1994/0166/latest/DLM342465.html"

    def formula(person, period, parameters):
        auto_assessed = person("tax_admin__automatic_tax_assessment", period)
        # Auto-assessed individuals do not have manual filing deadlines (represented by 0), manual filing has a 3-month default (by July 7th)
        return (not auto_assessed) * 3
