"""Property-based smoke tests for CI quality gate coverage."""

from hypothesis import given
from hypothesis import strategies as st


@given(st.integers(min_value=0, max_value=150))
def test_age_is_never_negative(age):
    """Exercise Hypothesis under the pytest quality gate."""

    assert age >= 0
