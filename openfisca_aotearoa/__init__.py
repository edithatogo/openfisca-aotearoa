"""
This following instantiates the CountryTaxBenefitSystem
"""

from openfisca_aotearoa.aotearoa_legislationmodel import (
    AotearoaLegislationModel,
    )
from openfisca_aotearoa.simulation import BatchSimulator

CountryTaxBenefitSystem = AotearoaLegislationModel
__all__ = ["CountryTaxBenefitSystem", "BatchSimulator"]

