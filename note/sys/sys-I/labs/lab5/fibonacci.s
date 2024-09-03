.text
.globl fibonacci

fibonacci:
    # Prologue: Setup stack frame and save registers
    addi sp, sp, -64           # Allocate stack space
    sd ra, 56(sp)              # Save return address to stack
    sd s0, 48(sp)              # Save s0 to stack
    addi s0, sp, 64            # Set s0 to point to the top of the stack

    # Save argument n to stack
    sd a0, -56(s0)             # Save n to stack

    # Base case check: if n <= 1, return 1
    li a1, 1                   # Load immediate 1 into a1
    ble a0, a1, .L2            # If n <= 1, branch to .L2

    # Recursive case: calculate fibonacci(n - 1) + fibonacci(n - 2)
    j .L1                      # Jump to .L1 to perform the recursive calculation

.L1:
    # Calculate fibonacci(n - 1)
    ld a5, -56(s0)             # Load n from stack
    addi a5, a5, -1            # Calculate n - 1
    sd a5, -48(s0)             # Save n - 1 to stack
    mv a0, a5                  # Move n - 1 to a0 (argument for recursive call)
    call fibonacci             # Call fibonacci(n - 1)
    mv a3, a0                  # Move result of fibonacci(n - 1) to a3
    sd a3, -36(s0)             # Save result of fibonacci(n - 1) to stack

    # Calculate fibonacci(n - 2)
    ld a5, -56(s0)             # Load n from stack
    addi a5, a5, -2            # Calculate n - 2
    mv a0, a5                  # Move n - 2 to a0 (argument for recursive call)
    call fibonacci             # Call fibonacci(n - 2)
    mv a4, a0                  # Move result of fibonacci(n - 2) to a4

    # Combine results
    ld a3, -36(s0)             # Load result of fibonacci(n - 1) from stack
    add a5, a3, a4             # Add fibonacci(n - 1) and fibonacci(n - 2)
    j .L3                      # Jump to .L3 to return result

.L2:
    # Base case: return 1
    li a5, 1                   # Load immediate 1 into a5
    j .L3                      # Jump to .L3 to return result

.L3:
    # Epilogue: Return value and restore registers
    mv a0, a5                  # Move result to a0 (return value)
    ld ra, 56(sp)              # Restore return address from stack
    ld s0, 48(sp)              # Restore s0 from stack
    addi sp, sp, 64            # Deallocate stack space
    jr ra                      # Return from function
