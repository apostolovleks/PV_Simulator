import pandas as pd
import pvlib

from dto import Location


class Photovoltaic:

    def __init__(self, coordinates: Location, surface_tilt: int, surface_azimuth: int, dt: str):
        self.coordinates = coordinates
        self.surface_tilt = surface_tilt
        self.surface_azimuth = surface_azimuth
        self.current_datetime = dt
        self._cec_mod_db = pvlib.pvsystem.retrieve_sam('CECmod')
        self._invdb = pvlib.pvsystem.retrieve_sam('CECInverter')

        # Amerisolar-Worldwide Energy and Manufacturing USA Co. Ltd AS-6P-335W
        self._module_data = self._cec_mod_db.iloc[:, 290]

        # ABB: MICRO-0-3HV-I-OUTDU-S-240 [240V]'
        self._inverter_data = self._invdb.iloc[:, 5]

    def _get_system_for_model(self) -> pvlib.pvsystem.PVSystem:
        """Prepare system for model. Using certain model of modul and inverter.
        :return: System of photovoltaic
        """

        temperature_model_parameters = (
            pvlib.temperature.
            TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass'])
        system = pvlib.pvsystem.PVSystem(surface_tilt=self.surface_tilt, surface_azimuth=self.surface_azimuth,
                                         module_parameters=self._module_data,
                                         inverter_parameters=self._inverter_data,
                                         temperature_model_parameters=temperature_model_parameters)
        return system

    def _run_model(self) -> pvlib.modelchain.ModelChainResult:
        """Run model. Using specified date and time.
        :return: Model calculation results
        """

        system = self._get_system_for_model()
        location = pvlib.location.Location(self.coordinates.latitude, self.coordinates.longitude)
        mc = pvlib.modelchain.ModelChain(system, location,
                                         aoi_model='no_loss',
                                         spectral_model='no_loss',
                                         name='AssessingSolar_PV')
        times = pd.date_range(self.current_datetime, self.current_datetime, freq='S', tz='Etc/GMT+1')
        weather = location.get_clearsky(times)
        mc.run_model(weather)
        return mc.results

    def get_value(self) -> int:
        """Get value of alternating current from photovoltaic.
        :return: Value from photovoltaic
        """

        model_results = self._run_model()
        power_kw = round(model_results.ac.values[0] / 1000, 5)
        return power_kw if power_kw > 0 else 0
