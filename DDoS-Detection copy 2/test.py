import sys
import tracemalloc
import time

def generate_list_comprehension(n):
    
    return [i**2 for i in range(n)]

def generate_generator_expression(n):
    
    return (i**2 for i in range(n))

def measure_memory_usage(sequence):
   
    return sys.getsizeof(sequence)

def measure_peak_memory_usage(func, *args):
    
    tracemalloc.start()
    func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def measure_execution_time(func, *args):
    
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

# defining a function for edge case 
# provided in the documentation provided 

def test_edge_cases():
   
    
    small_n = 10
    print(f"\nTesting small input (N = {small_n}):")
    list_small = generate_list_comprehension(small_n)
    gen_small = generate_generator_expression(small_n)
    print(f"List comprehension memory: {measure_memory_usage(list_small)} bytes")
    print(f"Generator memory: {measure_memory_usage(gen_small)} bytes")

    
    large_n = 1000000
    print(f"\nTesting large input (N = {large_n}):")
    list_large = generate_list_comprehension(large_n)
    gen_large = generate_generator_expression(large_n)
    print(f"List comprehension memory: {measure_memory_usage(list_large)} bytes")
    print(f"Generator memory: {measure_memory_usage(gen_large)} bytes")

    
    print("\nTesting generator exhaustion:")
    gen = generate_generator_expression(5)
    print("First iteration of generator:", list(gen))
    print("Second iteration of generator (exhausted):", list(gen))

    
    print("\nTesting sequential access of generator elements:")
    gen = generate_generator_expression(5)
    print("Accessing elements using next():")
    for _ in range(5):
        print(next(gen), end=" ")
    print()

def main():
    n = 100000  
    print(f"Comparing list comprehension and generator expression for N = {n}:")

    
    list_comp = generate_list_comprehension(n)
    gen_expr = generate_generator_expression(n)
    print(f"List comprehension memory usage: {measure_memory_usage(list_comp)} bytes")
    print(f"Generator memory usage: {measure_memory_usage(gen_expr)} bytes")

    
    print("\nMeasuring peak memory usage:")
    list_comp_peak = measure_peak_memory_usage(generate_list_comprehension, n)
    gen_expr_peak = measure_peak_memory_usage(generate_generator_expression, n)
    print(f"List comprehension peak memory: {list_comp_peak} bytes")
    print(f"Generator peak memory: {gen_expr_peak} bytes")

    
    print("\nMeasuring execution time:")
    list_comp_time = measure_execution_time(generate_list_comprehension, n)
    gen_expr_time = measure_execution_time(generate_generator_expression, n)
    print(f"List comprehension execution time: {list_comp_time:.6f} seconds")
    print(f"Generator execution time: {gen_expr_time:.6f} seconds")

 
    test_edge_cases()

if __name__ == "__main__":
    main()