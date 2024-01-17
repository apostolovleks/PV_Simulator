from conftest import test_photovoltaic
import pvlib


def test_get_system_for_model():
    system = test_photovoltaic._get_system_for_model()
    assert isinstance(system, pvlib.pvsystem.PVSystem)


def test_run_model():
    model_results = test_photovoltaic._run_model()
    assert isinstance(model_results, pvlib.modelchain.ModelChainResult)


def test_get_value():
    pv_value = test_photovoltaic.get_value()
    assert pv_value > 0
