import os
import sys
import inspect
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), '../../')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), './')))

from models.effunetpp_if import EffUnetPPModel

N_NAME = os.path.basename(os.path.dirname(inspect.getfile(inspect.currentframe())))

MODEL_INTERFACE = EffUnetPPModel
