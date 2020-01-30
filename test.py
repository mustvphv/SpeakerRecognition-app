import sidekit
import sidekit.frontend
#from sidekit.frontend.features import *
from sidekit.features_extractor import FeaturesExtractor
#import numpy

import copy
import logging
import numpy
from scipy.fftpack import fft
from scipy import ndimage
from sidekit.mixture import Mixture

#from numpy.fft import fft, ifft
#import numpy.fft
#from numpy.fft import fftpack

#val = sidekit.frontend.features.mfcc("011_1_2.wav", lowfreq=100, maxfreq=8000, nlinfilt=0, nlogfilt=24, nwin=0.025,
#fs=16000, nceps=13, shift=0.01, get_spec=False, get_mspec=False,
#prefac=0.97)

"""
extractor = sidekit.FeaturesExtractor(audio_filename_structure="011_1_2.wav",
feature_filename_structure="{}.h5",
sampling_frequency=8000,
lower_frequency=0,
higher_frequency=4000,
filter_bank="log",
filter_bank_size=40,
window_size=0.025,
shift=0.01,
ceps_number=20,
vad="snr",
snr=40,
pre_emphasis=0.97,
save_param=["energy"],
keep_all_features=True)
"""


extractor = sidekit.FeaturesExtractor(audio_filename_structure=None,
                                      feature_filename_structure=None,
                                      sampling_frequency=None,
                                      lower_frequency=200,
                                      higher_frequency=3800,
                                      filter_bank="log",
                                      filter_bank_size=24,
                                      window_size=0.025,
                                      shift=0.01,
                                      ceps_number=20,
                                      vad="snr",
                                      snr=40,
                                      pre_emphasis=0.97,
                                      save_param=["vad", "energy", "cep", "fb"],
                                      keep_all_features=True)

"""
extractor = sidekit.FeaturesExtractor(audio_filename_structure=None,
feature_filename_structure=None,
sampling_frequency=None,
lower_frequency=200,
higher_frequency=3800,
filter_bank="log",
filter_bank_size=24,
window_size=0.025,
shift=0.01,
ceps_number=20,
vad="snr",
snr=40,
pre_emphasis=0.97,
save_param=["vad", "energy", "cep", "fb"],
keep_all_features=True)
"""
#extractor.save("011_1_2")
#fh = extractor.extract("011_1_2")

#fh = extractor.extract("taaf");
#fh = extractor.extract(show="011_1_2", channel=1)
#fh = extractor.save(show="011_1_2", channel=1)

extractor.save(show="011_1_2",
channel=0,
input_audio_filename="audio/nist_2004/011_1_2.wav",
output_feature_filename="feat/nist/taaa.h5")

"""
fh = extractor.extract(show="taaa",
channel=0,
input_audio_filename="audio/sre04/taaa.sph",
output_feature_filename="feat/nist/taaa.h5")
"""



#extractor.save()

#extractor.save("011_1_2");
"""
extractor.save(show="011_1_2",
channel=0,
input_audio_filename="011_1_2.wav",
output_feature_filename="feat/nist2004/taaa.h5")
"""

"""
fh = extractor.extract("jourbon");

show_list = ["jourbon", "jourbonf"]
channel_list = [0, 0]

extractor.save_list(show_list=show_list,
                    channel_list=channel_list,
                    num_thread=10)

"""

"""
extractor2 = sidekit.FeaturesExtractor(audio_filename_structure="012_3_2.wav",
sampling_frequency=8000,
lower_frequency=0,
higher_frequency=4000,
filter_bank="log",
filter_bank_size=40,
window_size=0.025,
shift=0.01,
ceps_number=20,
vad="snr",
snr=40,
pre_emphasis=0.97,
save_param=["energy"],
keep_all_features=True)
"""

"""
fs_1 = sidekit.FeaturesServer(features_extractor=extractor,
feature_filename_structure=None,
sources=None,
#vad="snr",
#snr=40,
dataset_list=["energy"],
keep_all_features=True)
"""

print(extractor)
#print(extractor2)
#print(fs_1)