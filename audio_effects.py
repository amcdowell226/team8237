from audioFX.Fx import Fx
from librosa import load
import soundfile

infile = 'jingle.wav'
outfile = 'altered_jingle.wav'

x, sr = load(infile)

fx = Fx(sr)

def flanger(x, sr, fx): 
    fx_chain = {
                "flanger": 1.0
                }

    optional_parameters = {"flanger_frequency": 1.0,
                            "flanger_depth": 10.0,
                            "flanger_delay": 1.0
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def wahwah(x, sr, fx): 
    fx_chain = {
                "wahwah": 1.0
                }

    optional_parameters = {"wahwah_damp": 0.49,
                            "wahwah_minf": 100.0,
                            "wahwah_maxf": 2000.0,
                            "wahwah_wahf": 2000.0
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def tremolo(x, sr, fx): 
    fx_chain = {
                "tremolo": 1.0
                }

    optional_parameters = {"tremolo_alpha": 1.0,
                            "tremolo_modfreq": 10.0
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def distortion(x, sr, fx): 
    fx_chain = {
                "distortion": 1.0
                }

    optional_parameters = {"distortion_alpha": 5.0
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def chorus(x, sr, fx): 
    fx_chain = {
                "chorus": 1.0
                }

    optional_parameters = {"chorus_frequency": 2.0,
                           "chorus_depth": 0.9,
                           "chorus_delay": 0.0
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def high_pitch(x, sr, fx): 
    fx_chain = {
                "pitch": 1.0
                }

    optional_parameters = {"pitch_semitones": 12.0,
                           "pitch_mirror": False
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def low_pitch(x, sr, fx): 
    fx_chain = {
                "pitch": 1.0
                }

    optional_parameters = {"pitch_semitones": 5.0,
                           "pitch_mirror": True
                            }

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def griffin(x, sr, fx): 
    fx_chain = {
                "griffin": 1.0
                }

    optional_parameters = {}

    y = fx.process_audio(x, fx_chain, optional_parameters)
    return soundfile.write(outfile, y, sr)

def timestretch_slow(x, sr, fx): 
    fx_chain = {
                "timestretch": 0.5
                }

    y = fx.process_audio(x, fx_chain)
    return soundfile.write(outfile, y, sr)

def timestretch_fast(x, sr, fx): 
    fx_chain = {
                "timestretch": 1.5
                }

    y = fx.process_audio(x, fx_chain)
    return soundfile.write(outfile, y, sr)