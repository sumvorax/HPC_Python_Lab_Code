
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = { 'a': 7, 'b': 3.14 }
    request = comm.isend(data, dest = 1, tag = 11)
    request.wait()

    print("rank = %r, data = %r" % (rank, data))

elif rank == 1:
    request = comm.irecv(source = 0, tag = 11)
    data = request.wait()

    print("rank = %r, data = %r" % (rank, data))

else:
    print("rank = %r, data = <NONE>" % rank)
