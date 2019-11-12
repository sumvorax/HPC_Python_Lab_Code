
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

sendbuf = None

if rank == 0:
    sendbuf = np.empty([size, 10], dtype='i')
    sendbuf.T[:,:] = range(size)
    print("[Before] rank = %r: sendbuf = %r" % (rank, sendbuf))

recvbuf = np.empty(10, dtype='i')


comm.Scatter(sendbuf, recvbuf, root=0)

print("[After] rank = %r: recvbuf = %r" % (rank, recvbuf))

#assert np.allclose(recvbuf, rank)
