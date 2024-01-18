from conftest import test_photovoltaic
import pvlib


def test_get_system_for_model():
    """Test _get_system_for_model for a valid system."""
    system = test_photovoltaic._get_system_for_model()
    assert isinstance(system, pvlib.pvsystem.PVSystem)


def test_run_model():
    """Test _run_model for a valid result from model running."""
    model_results = test_photovoltaic._run_model()
    assert isinstance(model_results, pvlib.modelchain.ModelChainResult)


def test_get_value():
    """Test get_value() for the valid value from Photovoltaic."""
    pv_value = test_photovoltaic.get_value()
    assert pv_value > 0
