from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = [1, 2, 3, 4, 5, 6, 7] #Data to be filtered
else: 
    data = []

def filter_func(x): #Filtering function
    return x % 2 == 0

data = comm.scatter(data, root=0)
data = (filter_func(data), data)

data= comm.gather(data, root=0)
comm.Barrier()

if rank == 0:
    data = [y for x,y in data if x]
    print(data)
