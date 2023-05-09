import time
from . import dfs, kruskal, aldous_broder, maze_tools

print("Runtime testing starts")
print()

test_sizes = [4, 10, 25, 50, 100, 150, 200]
algos = ["dfs", "kruskal", "aldours-broder"]

for algorithm in algos:
    
    if algorithm == "dfs":
      print("Starting tests for iterative DFS.")

        for size in test_sizes:
            
            i = 0
            time_total = 0
            while i < 10:

                start_time = time.time()
                dfs_maze = dfs.create_dfs_maze(size)
                end_time = time.time()
                dfs_execution_time = round((end_time - start_time) * 1000, 4)
                time_total += dfs_execution_time
                i += 1

            average_run_time = time_total/10

            print("DFS algorithm, size " + size + "x" + size + ": average runtime " + average_run_time + " ms)
            i = 0
            time_total = 0
    print()
                  
    elif algorithm == "kruskal":
                  print("Starting tests for Kruskal's algorithm.")
        
         i = 0
            time_total = 0
            while i < 10:
            
                start_time = time.time()
                kruskal_maze = kruskal.create_kruskal_maze(size)
                end_time = time.time()
                kruskal_execution_time = round((end_time - start_time) * 1000, 4)
                time_total += kruskal_execution_time
                i += 1
        
            average_run_time = time_total/10
            
            print("Kruskal's algorithm, size " + size + "x" + size + ": average runtime " + average_run_time + " ms)
            i = 0
            time_total = 0

    print()
    elif algorithm == "aldour_broder":
                  print("Starting tests for Aldous-Broder algorithm.")
        
         i = 0
            time_total = 0
            while i < 10:
            
                start_time = time.time()
                aldous_broder_maze = aldous_broder.create_aldous_broder_maze(size)
                end_time = time.time()
                aldous_broder_execution_time = round((end_time - start_time) * 1000, 4)
                time_total += aldous_broder_execution_time
                i += 1
        
            average_run_time = time_total/10
            
            print("Aldous-Broder algorithm, size " + size + "x" + size + ": average runtime " + average_run_time + " ms)
            i = 0
            time_total = 0
    print()
    
    








