"""Public and community housing income-related rent variables."""

import numpy

from openfisca_core import periods
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person

ACT_REFERENCE = "https://www.legislation.govt.nz/act/public/1992/0076/latest/whole.html"
REGULATIONS_REFERENCE = "https://www.legislation.govt.nz/regulation/public/2018/0173/latest/whole.html"
MSD_GUIDANCE_REFERENCE = "https://www.workandincome.govt.nz/housing/live-in-home/live-in-public-housing/calculating-rent-payments.html"


class housing_restructuring__social_housing_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.MONTH
    default_value = False
    label = "Is the person eligible for social housing placement"
    reference = ACT_REFERENCE


class housing_restructuring__income_related_rent_information_sufficient(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.WEEK
    default_value = True
    label = "Tenant has supplied sufficient and accurate information for income-related rent"
    reference = ACT_REFERENCE


class housing_restructuring__income_related_rent_discrepancy_unresolved(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.WEEK
    default_value = False
    label = "Income-related rent discrepancy remains unresolved after the statutory response period"
    reference = ACT_REFERENCE


class housing_restructuring__pre_2026_amendment_calculation(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.WEEK
    default_value = False
    label = "Income-related rent calculation or review is excluded from the 2 March 2026 amendments"
    reference = ACT_REFERENCE


class housing_restructuring__applicable_person(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.WEEK
    default_value = True
    label = "Person is included as an applicable person for household income-related rent assessment"
    reference = ACT_REFERENCE


class housing_restructuring__assessable_income(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly assessable income after tax and permitted deductions for income-related rent"
    reference = ACT_REFERENCE

    def formula(person, period, parameters):
        annual_gross_income = person("income_tax__annual_gross_income", period.this_year)
        return annual_gross_income / 52.0


class housing_restructuring__household_assessable_income(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly household assessable income for applicable persons in the tenancy"
    reference = ACT_REFERENCE

    def formula(person, period, parameters):
        assessable_income = person("housing_restructuring__assessable_income", period)
        applicable_income = (
            assessable_income
            * person("housing_restructuring__applicable_person", period)
        )
        tenancy_income = person.tenancy.sum(applicable_income)
        return numpy.maximum(applicable_income, tenancy_income)


class housing_restructuring__income_threshold(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly income threshold for income-related rent"
    reference = [REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]

    def formula(person, period, parameters):
        p = parameters(period).housing_restructuring.income_related_rent
        sole_threshold = p.thresholds.sole_without_children
        other_threshold = p.thresholds.other_households
        is_sole_without_children = person(
            "housing_restructuring__sole_without_children_threshold_applies",
            period,
        )
        return (
            is_sole_without_children * sole_threshold
            + (1 - is_sole_without_children) * other_threshold
        )


class housing_restructuring__sole_without_children_threshold_applies(Variable):
    value_type = bool
    entity = Person
    definition_period = periods.WEEK
    default_value = False
    label = "Sole-without-children public housing threshold applies"
    reference = [REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]


class housing_restructuring__weekly_family_tax_credit_entitlement(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    default_value = 0.0
    label = "Weekly family tax credit entitlement included in income-related rent"
    reference = [ACT_REFERENCE, REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]


class housing_restructuring__additional_resident_contributions(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    default_value = 0.0
    label = "Weekly contributions received from additional residents or boarders"
    reference = [ACT_REFERENCE, MSD_GUIDANCE_REFERENCE]


class housing_restructuring__jobseeker_support_floor(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    default_value = 0.0
    label = "Appropriate weekly Jobseeker Support rate before reductions for income-related rent floor"
    reference = ACT_REFERENCE


class housing_restructuring__weekly_market_rent(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    default_value = 0.0
    label = "Weekly market rent for the public or community housing tenancy"
    reference = [ACT_REFERENCE, MSD_GUIDANCE_REFERENCE]


class housing_restructuring__minimum_weekly_rent(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    default_value = 0.0
    label = "Minimum weekly rent required for the tenant's public housing circumstances"
    reference = MSD_GUIDANCE_REFERENCE


class housing_restructuring__income_formula_rent_weekly(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly income-related rent calculated from household assessable income"
    reference = [ACT_REFERENCE, REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]

    def formula(person, period, parameters):
        p = parameters(period).housing_restructuring.income_related_rent
        income = person("housing_restructuring__household_assessable_income", period)
        threshold = person("housing_restructuring__income_threshold", period)
        family_tax_credit = person(
            "housing_restructuring__weekly_family_tax_credit_entitlement",
            period,
        )
        additional_residents = person(
            "housing_restructuring__additional_resident_contributions",
            period,
        )
        income_component = (
            p.proportions.income_up_to_threshold
            * numpy.minimum(income, threshold)
            + p.proportions.income_above_threshold
            * numpy.maximum(income - threshold, 0)
        )
        family_tax_credit_component = (
            p.proportions.family_tax_credit
            * numpy.minimum(family_tax_credit, p.family_tax_credit_cap)
        )
        additional_resident_component = (
            p.proportions.additional_resident_contribution
            * additional_residents
        )
        return (
            income_component
            + family_tax_credit_component
            + additional_resident_component
        )


class housing_restructuring__benefit_floor_rent_weekly(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly income-related rent calculated from the Jobseeker Support floor"
    reference = [ACT_REFERENCE, REGULATIONS_REFERENCE]

    def formula(person, period, parameters):
        p = parameters(period).housing_restructuring.income_related_rent
        jobseeker_floor = person("housing_restructuring__jobseeker_support_floor", period)
        family_tax_credit = person(
            "housing_restructuring__weekly_family_tax_credit_entitlement",
            period,
        )
        additional_residents = person(
            "housing_restructuring__additional_resident_contributions",
            period,
        )
        return (
            p.proportions.benefit
            * jobseeker_floor
            + p.proportions.family_tax_credit
            * numpy.minimum(family_tax_credit, p.family_tax_credit_cap)
            + p.proportions.additional_resident_contribution
            * additional_residents
        )


class housing_restructuring__income_related_rent_weekly(Variable):
    value_type = float
    entity = Person
    definition_period = periods.WEEK
    label = "Weekly income-related rent for public and community housing tenants"
    reference = [ACT_REFERENCE, REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]

    def formula(person, period, parameters):
        return _legacy_income_related_rent_weekly(person, period)

    def formula_2026_03_02(person, period, parameters):
        eligible = person(
            "housing_restructuring__social_housing_eligible",
            period.first_month,
        )
        information_sufficient = person(
            "housing_restructuring__income_related_rent_information_sufficient",
            period,
        )
        discrepancy_unresolved = person(
            "housing_restructuring__income_related_rent_discrepancy_unresolved",
            period,
        )
        market_rent = person("housing_restructuring__weekly_market_rent", period)
        minimum_rent = person("housing_restructuring__minimum_weekly_rent", period)
        income_formula = person(
            "housing_restructuring__income_formula_rent_weekly",
            period,
        )
        benefit_formula = person(
            "housing_restructuring__benefit_floor_rent_weekly",
            period,
        )
        pre_2026_calculation = person(
            "housing_restructuring__pre_2026_amendment_calculation",
            period,
        )
        current_law_rent = numpy.maximum(income_formula, benefit_formula)
        current_law_rent = numpy.maximum(current_law_rent, minimum_rent)
        current_law_rent = _cap_at_market_rent(current_law_rent, market_rent)
        old_law_scaffold = 0.25 * person(
            "housing_restructuring__household_assessable_income",
            period,
        )
        old_law_scaffold = _cap_at_market_rent(old_law_scaffold, market_rent)
        calculated_rent = (
            pre_2026_calculation * old_law_scaffold
            + (1 - pre_2026_calculation) * current_law_rent
        )
        market_rent_notice = market_rent * (
            (1 - information_sufficient) + discrepancy_unresolved
        )
        assessed_rent = (
            information_sufficient
            * (1 - discrepancy_unresolved)
            * calculated_rent
            + market_rent_notice
        )
        return eligible * numpy.floor(assessed_rent)


class housing_restructuring__income_related_rent(Variable):
    value_type = float
    entity = Person
    definition_period = periods.MONTH
    label = "Calculated income-related rent for social housing tenants"
    reference = [ACT_REFERENCE, REGULATIONS_REFERENCE, MSD_GUIDANCE_REFERENCE]

    def formula(person, period, parameters):
        weekly_rent = person(
            "housing_restructuring__income_related_rent_weekly",
            period.first_week.offset(1),
        )
        return weekly_rent * 52.0 / 12.0


def _cap_at_market_rent(rent, market_rent):
    return numpy.where(market_rent > 0, numpy.minimum(rent, market_rent), rent)


def _legacy_income_related_rent_weekly(person, period):
    eligible = person(
        "housing_restructuring__social_housing_eligible",
        period.first_month,
    )
    assessable_income = person("housing_restructuring__household_assessable_income", period)
    market_rent = person("housing_restructuring__weekly_market_rent", period)
    return eligible * numpy.floor(_cap_at_market_rent(0.25 * assessable_income, market_rent))
