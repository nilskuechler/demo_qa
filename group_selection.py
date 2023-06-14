from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='Advantage_system4.1',
))

h = {}

J = {
    ('P1','P2'): 3,
    ('P1','P3'): 2,
    ('P1','P4'): 6,
    ('P2','P3'): 5,
    ('P2','P4'): 3,
    ('P3','P4'): 5,
}


response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
    chain_strength=4,
    annealing_time=100,
)
dwave.inspector.show(response)
