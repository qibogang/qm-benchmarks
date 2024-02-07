
# Single QUA script generated at 2024-02-07 17:07:09.341746
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    wait((4+(0*(Cast.to_int(v2)+Cast.to_int(v3)))), "readout0")
    with for_(v1,0,(v1<4096),(v1+1)):
        align()
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        frame_rotation_2pi(-0.013333333333333334, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(21, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        r1 = declare_stream()
        save(v2, r1)
        r2 = declare_stream()
        save(v3, r2)
        wait(75501, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(250, "drive0")
        frame_rotation_2pi(-0.3466666666666667, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(75270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(500, "drive0")
        frame_rotation_2pi(-0.6799999999999999, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(75520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(750, "drive0")
        frame_rotation_2pi(-1.0133333333333334, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(75770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(1000, "drive0")
        frame_rotation_2pi(-1.3466666666666667, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(76020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(1250, "drive0")
        frame_rotation_2pi(-1.6800000000000002, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(76270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(1500, "drive0")
        frame_rotation_2pi(-2.013333333333333, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(76520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(1750, "drive0")
        frame_rotation_2pi(-2.3466666666666667, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(76770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(2000, "drive0")
        frame_rotation_2pi(-2.68, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(77020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(2250, "drive0")
        frame_rotation_2pi(-3.0133333333333336, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(77270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(2500, "drive0")
        frame_rotation_2pi(-3.3466666666666662, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(77520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(2750, "drive0")
        frame_rotation_2pi(-3.6800000000000006, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(77770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(3000, "drive0")
        frame_rotation_2pi(-4.013333333333333, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(78020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(3250, "drive0")
        frame_rotation_2pi(-4.346666666666667, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(78270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(3500, "drive0")
        frame_rotation_2pi(-4.68, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(78520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(3750, "drive0")
        frame_rotation_2pi(-5.013333333333333, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(78770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(4000, "drive0")
        frame_rotation_2pi(-5.346666666666668, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(79020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(4250, "drive0")
        frame_rotation_2pi(-5.680000000000001, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(79270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(4500, "drive0")
        frame_rotation_2pi(-6.013333333333333, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(79520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(4750, "drive0")
        frame_rotation_2pi(-6.346666666666666, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(79770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(5000, "drive0")
        frame_rotation_2pi(-6.68, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(80020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(5250, "drive0")
        frame_rotation_2pi(-7.013333333333333, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(80270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(5500, "drive0")
        frame_rotation_2pi(-7.346666666666667, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(80520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(5750, "drive0")
        frame_rotation_2pi(-7.68, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(80770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(6000, "drive0")
        frame_rotation_2pi(-8.013333333333332, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(81020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(6250, "drive0")
        frame_rotation_2pi(-8.346666666666666, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(81270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(6500, "drive0")
        frame_rotation_2pi(-8.680000000000001, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(81520, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(6750, "drive0")
        frame_rotation_2pi(-9.013333333333334, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(81770, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(7000, "drive0")
        frame_rotation_2pi(-9.346666666666666, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(82020, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75500, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        wait(7250, "drive0")
        frame_rotation_2pi(-9.680000000000001, "drive0")
        play("drive(40, 0.0025, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(82270, "readout0")
        measure("readout(2000, 0.005, Rectangular())", "readout0", None, dual_demod.full("cos", "out1", "sin", "out2", v2), dual_demod.full("minus_sin", "out1", "cos", "out2", v3))
        save(v2, r1)
        save(v3, r2)
        wait(75000, )
    with stream_processing():
        r1.buffer(30).average().save("readout(2000, 0.005, Rectangular())_0_I")
        r2.buffer(30).average().save("readout(2000, 0.005, Rectangular())_0_Q")


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
                "I": ('con3', 3),
                "Q": ('con3', 4),
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
                "I": ('con3', 9),
                "Q": ('con3', 10),
                "lo_frequency": 5000000000,
                "mixer": "mixer_readout0",
            },
            "outputs": {
                "out1": ('con3', 1),
                "out2": ('con3', 2),
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
            "samples": [0.00012816812592664437, 0.00017246906479309853, 0.0002284843883901181, 0.0002979998210066183, 0.0003826393443408954, 0.00048370145401761686, 0.0006019761856806215, 0.0007375566404361071, 0.000889663130355346, 0.001056501108057972, 0.001235174933829096, 0.0014216776342966804, 0.0016109718120629881, 0.0017971689242729397, 0.00197380392415197, 0.002134190903362869, 0.002271834390902675, 0.002380861999737941, 0.0024564386723947514] + [0.002495121952768689] * 2 + [0.0024564386723947514, 0.002380861999737941, 0.002271834390902675, 0.002134190903362869, 0.00197380392415197, 0.0017971689242729397, 0.0016109718120629881, 0.0014216776342966804, 0.001235174933829096, 0.001056501108057972, 0.000889663130355346, 0.0007375566404361071, 0.0006019761856806215, 0.00048370145401761686, 0.0003826393443408954, 0.0002979998210066183, 0.0002284843883901181, 0.00017246906479309853, 0.00012816812592664437],
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
        "mixer_drive0": [{'intermediate_frequency': 198114578, 'lo_frequency': 3900000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_readout0": [{'intermediate_frequency': 228200000, 'lo_frequency': 5000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con3": {
            "type": "opx1",
            "analog_outputs": {
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "9": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
                "10": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "drive0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "intermediate_frequency": 198114578.0,
            "operations": {
                "drive(40, 0.0025, Gaussian(5))": "drive(40, 0.0025, Gaussian(5))",
            },
            "mixInputs": {
                "I": ('con3', 3),
                "Q": ('con3', 4),
                "mixer": "mixer_drive0",
                "lo_frequency": 3900000000.0,
            },
        },
        "readout0": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con3', 1),
                "out2": ('con3', 2),
            },
            "time_of_flight": 280,
            "smearing": 0,
            "intermediate_frequency": 228200000.0,
            "operations": {
                "readout(2000, 0.005, Rectangular())": "readout(2000, 0.005, Rectangular())",
            },
            "mixInputs": {
                "I": ('con3', 9),
                "Q": ('con3', 10),
                "mixer": "mixer_readout0",
                "lo_frequency": 5000000000.0,
            },
        },
    },
    "pulses": {
        "drive(40, 0.0025, Gaussian(5))": {
            "length": 40,
            "waveforms": {
                "I": "Envelope_Waveform_I(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))",
                "Q": "Envelope_Waveform_Q(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))",
            },
            "operation": "control",
        },
        "readout(2000, 0.005, Rectangular())": {
            "length": 2000,
            "waveforms": {
                "I": "constant_wf0.005",
                "Q": "constant_wf0.005",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "cos": "cosine_weights0",
                "sin": "sine_weights0",
                "minus_sin": "minus_sine_weights0",
            },
            "operation": "measurement",
        },
    },
    "waveforms": {
        "Envelope_Waveform_I(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))": {
            "samples": [0.00012816812592664437, 0.00017246906479309853, 0.0002284843883901181, 0.0002979998210066183, 0.0003826393443408954, 0.00048370145401761686, 0.0006019761856806215, 0.0007375566404361071, 0.000889663130355346, 0.001056501108057972, 0.001235174933829096, 0.0014216776342966804, 0.0016109718120629881, 0.0017971689242729397, 0.00197380392415197, 0.002134190903362869, 0.002271834390902675, 0.002380861999737941, 0.0024564386723947514] + [0.002495121952768689] * 2 + [0.0024564386723947514, 0.002380861999737941, 0.002271834390902675, 0.002134190903362869, 0.00197380392415197, 0.0017971689242729397, 0.0016109718120629881, 0.0014216776342966804, 0.001235174933829096, 0.001056501108057972, 0.000889663130355346, 0.0007375566404361071, 0.0006019761856806215, 0.00048370145401761686, 0.0003826393443408954, 0.0002979998210066183, 0.0002284843883901181, 0.00017246906479309853, 0.00012816812592664437],
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "Envelope_Waveform_Q(num_samples = 40, amplitude = 0.0025, shape = Gaussian(5))": {
            "samples": [0.0] * 40,
            "type": "arbitrary",
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "constant_wf0.005": {
            "sample": 0.005,
            "type": "constant",
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
            "sine": [(0.0, 2000)],
        },
        "sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(1.0, 2000)],
        },
        "minus_sine_weights0": {
            "cosine": [(0.0, 2000)],
            "sine": [(-1.0, 2000)],
        },
    },
    "mixers": {
        "mixer_drive0": [{'intermediate_frequency': 198114578.0, 'lo_frequency': 3900000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_readout0": [{'intermediate_frequency': 228200000.0, 'lo_frequency': 5000000000.0, 'correction': [1.0, 0.0, 0.0, 1.0]}],
    },
}

