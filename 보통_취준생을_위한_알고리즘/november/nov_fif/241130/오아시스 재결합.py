n = int(input())
stack = []
answer = 0

for i in range(n):
    h = int(input())
    cnt = 1
    print(f"\nProcessing height {h}")
    print(f"Initial stack: {stack}")
    
    while stack and stack[-1][0] <= h:
        top = stack[-1]
        print(f"Popping {top} from stack")
        answer += top[1]
        print(f"Added {top[1]} to answer. Current answer: {answer}")
        if top[0] == h:
            cnt += top[1]
            print(f"Same height as top. Incremented cnt to {cnt}")
        stack.pop()
    
    if stack:
        answer += 1
        print(f"Non-empty stack after popping. Incremented answer to {answer}")
    
    stack.append((h, cnt))
    print(f"Pushed ({h}, {cnt}) to stack")
    print(f"Stack after processing {h}: {stack}")

print("\nFinal answer:", answer)
