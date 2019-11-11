
#===============================================================================
#   Hello World scatter
#===============================================================================

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [x**2 for x in range(4)] #"Hello World!" []
else:
    data = None

print("rank = %r: data = %r") % (rank, data)

data = comm.scatter(data, root = 0)
comm.Barrier()

print("rank = %r: data = %r") % (rank, data)

