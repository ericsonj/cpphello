import os
from os.path import basename
from pymakelib import MKVARS
from pymakelib import addon
from pymakelib.eclipse_addon import EclipseAddon
from pymakelib import toolchain

addon.add(EclipseAddon)

def getProjectSettings():
    return {
        'PROJECT_NAME': basename(os.getcwd()),
        'FOLDER_OUT':   'Release/Objects/'
    }


def getTargetsScript():
    PROJECT_NAME = basename(os.getcwd())
    FOLDER_OUT = 'Release/'
    TARGET = FOLDER_OUT + PROJECT_NAME

    TARGETS = {
        'TARGET': {
            'LOGKEY':  'OUT',
            'FILE':    TARGET,
            'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS]
        },
        'TARGET_ZIP': {
            'LOGKEY':   'ZIP',
            'FILE':     TARGET + '.zip',
            'SCRIPT':   ['zip', TARGET + '.zip', MKVARS.TARGET]
        }
    }

    return TARGETS


def getCompilerSet():
    return toolchain.get_cpp_linux()


LIBRARIES = []

def getCompilerOpts():

    PROJECT_DEF = {
    }

    return {
        'MACROS': PROJECT_DEF,
        'MACHINE-OPTS': [
        ],
        'OPTIMIZE-OPTS': [
        ],
        'OPTIONS': [
        ],
        'DEBUGGING-OPTS': [
            '-g3'
        ],
        'PREPROCESSOR-OPTS': [
            '-MP',
            '-MMD'
        ],
        'WARNINGS-OPTS': [
        ],
        'CONTROL-C-OPTS': [
        ],
        'GENERAL-OPTS': [
        ],
        'LIBRARIES': LIBRARIES
    }


def getLinkerOpts():
    return {
        'LINKER-SCRIPT': [
        ],
        'MACHINE-OPTS': [
        ],
        'GENERAL-OPTS': [
        ],
        'LINKER-OPTS': [
        ],
        'LIBRARIES': LIBRARIES
    }
