from brian2 import *
import brian2genn

set_device('genn', directory='simple_example')

Npre = 10000
Npost= 1000
tau = 10*ms
Iin = 0.11/ms 
eqs = '''
dV/dt = -V/tau + Iin : 1
'''
G = NeuronGroup(Npre, eqs, threshold='V>1', reset='V=0', refractory=5 * ms)
G2= NeuronGroup(Npost, eqs, threshold='V>1', reset='V=0', refractory=5 * ms)

S=Synapses(G, G2, 'w:1', on_pre='V+= w');
S2= Synapses(G2, G, 'w:1', on_pre='V+= w');
S.connect(i=np.array([1, 1, 2, 2]), j=np.array([0, 1, 2, 3]));
S2.connect(condition= 'i != j',p=0.5);
run(10*ms)