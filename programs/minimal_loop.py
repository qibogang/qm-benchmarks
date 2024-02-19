# Single QUA script generated at 2024-02-07 17:07:09.341746
# QUA library version: 1.1.6

# Logged output for this program:
# Connection time: 1.4587697982788086
# Execution time: 0.5983867645263672
# readout(2000, 0.005, Rectangular())_0_I (30,)
# readout(2000, 0.005, Rectangular())_0_Q (30,)
# Fetch time: 39.20936918258667
# Total time: 41.266525745391846

from qm.qua import *

nosc = 10
delay_end = 30000
prefactor = -nosc / delay_end

with program() as prog:
    v2 = declare(fixed)
    v3 = declare(fixed)
    v = declare(fixed)
    wait((4 + (0 * (Cast.to_int(v2) + Cast.to_int(v3)))), "readout0")
    with for_(v, 0, (v < 30), (v + 1)):
        align()
        measure(
            "readout(2000, 0.005, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        wait(75000)
    with stream_processing():
        r1.buffer(30).save("readout(2000, 0.005, Rectangular())_0_I")
        r2.buffer(30).save("readout(2000, 0.005, Rectangular())_0_Q")


config = {
    "version": 1,
    "controllers": {
        "con3": {
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
            },
            "analog_outputs": {
                "3": {
                    "offset": 0.0,
                    "filter": {},
                },
                "4": {
                    "offset": 0.0,
                    "filter": {},
                },
                "9": {
                    "offset": 0.0,
                    "filter": {},
                },
                "10": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
        },
    },
    "octaves": {},
    "elements": {
        "drive0": {
            "mixInputs": {
                "I": ("con3", 3),
                "Q": ("con3", 4),
                "lo_frequency": 3900000000,
                "mixer": "mixer_drive0",
            },
            "intermediate_frequency": 198114578,
            "operations": {
                "drive(40, 0.0025, Gaussian(5))": "drive(40, 0.0025, Gaussian(5))",
            },
        },
        "readout0": {
            "mixInputs": {
                "I": ("con3", 9),
                "Q": ("con3", 10),
                "lo_frequency": 5000000000,
                "mixer": "mixer_readout0",
            },
            "outputs": {
                "out1": ("con3", 1),
                "out2": ("con3", 2),
            },
            "intermediate_frequency": 228200000,
            "operations": {
                "readout(2000, 0.005, Rectangular())": "readout(2000, 0.005, Rectangular())",
            },
            "time_of_flight": 280,
            "smearing": 0,
        },
    },
    "pulses": {
        "drive(40, 0.0025, Gaussian(5))": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "Envelope_Waveform_I(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))",
                "Q": "Envelope_Waveform_Q(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))",
            },
        },
        "readout(2000, 0.005, Rectangular())": {
            "operation": "measurement",
            "length": 2000,
            "waveforms": {
                "I": "constant_wf0.005",
                "Q": "constant_wf0.005",
            },
            "integration_weights": {
                "cos": "cosine_weights0",
                "sin": "sine_weights0",
                "minus_sin": "minus_sine_weights0",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "Envelope_Waveform_I(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))": {
            "type": "arbitrary",
            "samples": [
                0.00012816812592664437,
                0.00017246906479309853,
                0.0002284843883901181,
                0.0002979998210066183,
                0.0003826393443408954,
                0.00048370145401761686,
                0.0006019761856806215,
                0.0007375566404361071,
                0.000889663130355346,
                0.001056501108057972,
                0.001235174933829096,
                0.0014216776342966804,
                0.0016109718120629881,
                0.0017971689242729397,
                0.00197380392415197,
                0.002134190903362869,
                0.002271834390902675,
                0.002380861999737941,
                0.0024564386723947514,
            ]
            + [0.002495121952768689] * 2
            + [
                0.0024564386723947514,
                0.002380861999737941,
                0.002271834390902675,
                0.002134190903362869,
                0.00197380392415197,
                0.0017971689242729397,
                0.0016109718120629881,
                0.0014216776342966804,
                0.001235174933829096,
                0.001056501108057972,
                0.000889663130355346,
                0.0007375566404361071,
                0.0006019761856806215,
                0.00048370145401761686,
                0.0003826393443408954,
                0.0002979998210066183,
                0.0002284843883901181,
                0.00017246906479309853,
                0.00012816812592664437,
            ],
        },
        "Envelope_Waveform_Q(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "constant_wf0.005": {
            "type": "constant",
            "sample": 0.005,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights0": {
            "cosine": [(1.0, 2000)],
            "sine": [(-0.0, 2000)],
        },
        "sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights0": {
            "cosine": [(-0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "mixer_drive0": [
            {
                "intermediate_frequency": 198114578,
                "lo_frequency": 3900000000,
                "correction": [1.0, 0.0, 0.0, 1.0],
            }
        ],
        "mixer_readout0": [
            {
                "intermediate_frequency": 228200000,
                "lo_frequency": 5000000000,
                "correction": [1.0, 0.0, 0.0, 1.0],
            }
        ],
    },
}
