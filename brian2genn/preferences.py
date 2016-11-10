'''
Preferences that relate to the brian2genn interface.
'''

from brian2.core.preferences import *


prefs.register_preferences(
    'devices.genn',
    'Preferences that relate to the brian2genn interface',
    connectivity=BrianPreference(
        validator=lambda value: value in ['DENSE', 'SPARSE'],
        docs='''
        This preference determines which connectivity scheme is to be employed within GeNN. The valid alternatives are 'DENSE' and 'SPARSE'. For 'DENSE' the GeNN dense matrix methods are used for all connectivity matrices. When 'SPARSE' is chosen, the GeNN sparse matrix representations are used.''',
        default='SPARSE'
    ),
    extra_compile_args_nvcc=BrianPreference(
        docs='''Extra compile arguments (a list of strings) to pass to the nvcc compiler.''',
        default=['-O3']
    )
)
