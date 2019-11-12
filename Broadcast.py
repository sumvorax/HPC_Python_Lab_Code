
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank * rank

if rank == 0:
    data = { 'key1' : [7, 2.72, 2 + 3j], 'key2' : ('abc', 'xyz') }
else:
    data = None

print("[Before] rank = %r: data = %r" % (rank, data))

data = comm.bcast(data, root=0)

print("[After] rank = %r: data = %r" % (rank, data))
