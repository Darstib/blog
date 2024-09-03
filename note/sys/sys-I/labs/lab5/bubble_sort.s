.text
.globl  bubble_sort

bubble_sort:
    # Prologue: Setup stack frame and save registers
    addi sp, sp, -128           # Allocate stack space
    sd s0, 120(sp)             # Save s0 to stack
    addi s0, sp, 128           # Set s0 to point to the top of the stack

    # Save arguments to stack
    sd a0, -112(s0)            # Save arr to stack
    sd a1, -102(s0)            # Save len to stack

    # Initialize loop variables
    sd zero, -96(s0)           # Initialize i to 0
    sd zero, -88(s0)           # Initialize j to 0

    # Prepare for the outer loop by calculating len - 2
    addi a1, a1, -2            # len - 2
    sd a1, -80(s0)             # Save len - 2 to stack
    sd a1, -72(s0)             # Save len - 2 - i to stack

    # Start outer loop (i loop)
    j .L2                      # Jump to the beginning of the i loop

.L5:  # Inner loop body (j loop)
    ld a0, -88(s0)             # Load j from stack
    ld a1, -112(s0)            # Load arr from stack
    addi a6, zero, 8
    mul a0, a0, a6             # Calculate shift value for arr[j]
    add a1, a1, a0             # Calculate address of arr[j]
    ld a3, 0(a1)               # Load arr[j] into a3
    ld a4, 8(a1)               # Load arr[j + 1] into a4

    # Compare and possibly swap arr[j] and arr[j + 1]
    ble a3, a4, .L4            # If arr[j] <= arr[j + 1], skip the swap
    sd a4, 0(a1)               # Swap: arr[j] = arr[j + 1]
    sd a3, 8(a1)               # Swap: arr[j + 1] = arr[j]

.L4:
    # Increment j
    ld a0, -88(s0)             # Load j from stack
    addi a0, a0, 1             # Increment j
    sd a0, -88(s0)             # Save j back to stack

.L3:  # Inner loop comparison (j loop condition)
    ld a1, -80(s0)             # Load len - 2 from stack
    ld a0, -96(s0)             # Load i from stack
    addi a6, zero, -1
    mul a0, a0, a6             # Calculate -i
    add a1, a1, a0             # Calculate len - 2 - i
    ld a2, -88(s0)             # Load j from stack
    ble a2, a1, .L5            # If j <= len - 2 - i, continue inner loop

    # Increment i
    ld a0, -96(s0)             # Load i from stack
    addi a0, a0, 1             # Increment i
    sd a0, -96(s0)             # Save i back to stack

.L2:  # Outer loop comparison (i loop condition)
    ld a0, -96(s0)             # Load i from stack
    ld a1, -80(s0)             # Load len - 2 from stack
    sd zero, -88(s0)           # Reset j to 0
    ble a0, a1, .L3            # If i <= len - 2, continue outer loop

    # Epilogue: Restore registers and stack
    ld s0, 120(sp)             # Restore s0 from stack
    addi sp, sp, 128           # Deallocate stack space
    ret                        # Return from function
