t_input = input()                # Read the total number of test cases
if t_input.strip():
    T = int(t_input)

    for _ in range(T):           # Process each test case one by one
        N = int(input())

        
        ans = (N - 1) // 2      # Calculate the number of valid R values using integer division

        
        print(ans)       
