"""
This following instantiates the CountryTaxBenefitSystem
"""

from os import environ

environ.setdefault("OPENBLAS_NUM_THREADS", "1")
environ.setdefault("OMP_NUM_THREADS", "1")

from openfisca_aotearoa.aotearoa_legislationmodel import (
    AotearoaLegislationModel,
    )
from openfisca_aotearoa.simulation import BatchSimulator

CountryTaxBenefitSystem = AotearoaLegislationModel
__all__ = ["CountryTaxBenefitSystem", "BatchSimulator"]
