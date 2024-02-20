# Single QUA script generated at 2024-02-18 20:09:08.027535
# QUA library version: 1.1.6

from qm.qua import *

with program() as prog:
    v1 = declare(
        int,
    )
    v2 = declare(
        fixed,
    )
    v3 = declare(
        fixed,
    )
    v4 = declare(
        int,
    )
    wait(
        (4 + (0 * ((Cast.to_int(v2) + Cast.to_int(v3)) + Cast.to_int(v4)))), "readout0"
    )
    with for_(v1, 0, (v1 < 500), (v1 + 1)):
        align()
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(41, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        r1 = declare_stream()
        save(v4, r1)
        wait(526, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(525, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        frame_rotation_2pi(0.5, "drive0")
        play("drive(80, 0.06875, Gaussian(5))", "drive0")
        reset_frame("drive0")
        wait(65, "readout0")
        measure(
            "readout(2000, 0.013, Rectangular())",
            "readout0",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", v2),
            dual_demod.full("minus_sin", "out1", "cos", "out2", v3),
        )
        assign(
            v4,
            Cast.to_int(
                ((v2 * 0.4923575835133495) - (v3 * 0.8703930203976219)) > -0.001777
            ),
        )
        save(v4, r1)
        wait(
            25,
        )
    with stream_processing():
        r1.buffer(20).buffer(500).save("readout(2000, 0.013, Rectangular())_0_shots")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 20,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 20,
                },
            },
            "analog_outputs": {
                "9": {
                    "offset": 0.0,
                    "filter": {},
                },
                "10": {
                    "offset": 0.0,
                    "filter": {},
                },
                "1": {
                    "offset": 0.0,
                    "filter": {},
                },
                "2": {
                    "offset": 0.0,
                    "filter": {},
                },
            },
        },
    },
    "octaves": {
        "octave1": {
            "RF_outputs": {
                "5": {
                    "LO_frequency": 5700000000,
                    "gain": 0,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
                "1": {
                    "LO_frequency": 7200000000,
                    "gain": -20,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                },
            },
            "connectivity": "con1",
            "RF_inputs": {
                "1": {
                    "LO_frequency": 7200000000,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
        },
    },
    "elements": {
        "drive0": {
            "RF_inputs": {
                "port": ("octave1", 5),
            },
            "intermediate_frequency": 96222441,
            "operations": {
                "drive(80, 0.06875, Gaussian(5))": "drive(80, 0.06875, Gaussian(5))",
            },
        },
        "readout0": {
            "RF_inputs": {
                "port": ("octave1", 1),
            },
            "RF_outputs": {
                "port": ("octave1", 1),
            },
            "intermediate_frequency": 92027169,
            "operations": {
                "readout(2000, 0.013, Rectangular())": "readout(2000, 0.013, Rectangular())",
            },
            "time_of_flight": 100,
            "smearing": 0,
        },
    },
    "pulses": {
        "drive(80, 0.06875, Gaussian(5))": {
            "operation": "control",
            "length": 80,
            "waveforms": {
                "I": "Envelope_Waveform_I(num_samples = 80, amplitude = 0.06875, shape = Gaussian(5))",
                "Q": "Envelope_Waveform_Q(num_samples = 80, amplitude = 0.06875, shape = Gaussian(5))",
            },
        },
        "readout(2000, 0.013, Rectangular())": {
            "operation": "measurement",
            "length": 2000,
            "waveforms": {
                "I": "constant_wf0.013",
                "Q": "constant_wf0.013",
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
        "Envelope_Waveform_I(num_samples = 80, amplitude = 0.06875, shape = Gaussian(5))": {
            "type": "arbitrary",
            "samples": [
                0.0032645223411788245,
                0.0038017337219231487,
                0.004410088270728658,
                0.005095847310976187,
                0.0058652843021570955,
                0.006724581582231184,
                0.007679713219847413,
                0.008736314818737951,
                0.009899541622357698,
                0.01117391680160789,
                0.012563172356426587,
                0.014070085604537706,
                0.015696314746782493,
                0.017442237465583973,
                0.019306796907704003,
                0.021287359701103705,
                0.023379590836109836,
                0.025577350283199855,
                0.027872616106961658,
                0.030255438556132067,
                0.032713929156612497,
                0.03523428820796064,
                0.037800873291056684,
                0.040396310449800146,
                0.043001648634537884,
                0.04559655681820219,
                0.04815956195289309,
                0.050668324665132,
                0.053099948336315754,
                0.05543131602719755,
                0.05763944862792848,
                0.05970187669291469,
                0.06159701769323906,
                0.06330454992359016,
                0.06480577406284795,
                0.06608395342588577,
                0.06712462426669273,
                0.06791586809658753,
                0.06844853885192936,
            ]
            + [0.0687164388583674] * 2
            + [
                0.06844853885192936,
                0.06791586809658753,
                0.06712462426669273,
                0.06608395342588577,
                0.06480577406284795,
                0.06330454992359016,
                0.06159701769323906,
                0.05970187669291469,
                0.05763944862792848,
                0.05543131602719755,
                0.053099948336315754,
                0.050668324665132,
                0.04815956195289309,
                0.04559655681820219,
                0.043001648634537884,
                0.040396310449800146,
                0.037800873291056684,
                0.03523428820796064,
                0.032713929156612497,
                0.030255438556132067,
                0.027872616106961658,
                0.025577350283199855,
                0.023379590836109836,
                0.021287359701103705,
                0.019306796907704003,
                0.017442237465583973,
                0.015696314746782493,
                0.014070085604537706,
                0.012563172356426587,
                0.01117391680160789,
                0.009899541622357698,
                0.008736314818737951,
                0.007679713219847413,
                0.006724581582231184,
                0.0058652843021570955,
                0.005095847310976187,
                0.004410088270728658,
                0.0038017337219231487,
                0.0032645223411788245,
            ],
        },
        "Envelope_Waveform_Q(num_samples = 80, amplitude = 0.06875, shape = Gaussian(5))": {
            "type": "arbitrary",
            "samples": [0.0] * 80,
        },
        "constant_wf0.013": {
            "type": "constant",
            "sample": 0.013,
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
    "mixers": {},
}
