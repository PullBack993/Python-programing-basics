V = int(input())
P1 = int(input())
P2 = int(input())
time = float(input())

volume_p2 = P2 * time
volume_p1 = P1 * time
total = volume_p1 + volume_p2
if total > V:
    print(f'For {time:.2f} hours the pool overflows with {total - V:.2f} liters.')
else:
    print(f'The pool is {total / V * 100:.2f}% full. Pipe 1: {volume_p1 / total * 100:.2f}%. Pipe 2: {volume_p2 / total * 100:.2f}%.')

V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

p1_liters = P1 * H
p2_liters = P2 * H
total_liters = p1_liters + p2_liters
if total_liters > V:
    print(f"For {H:.2f} hours the pool overflows with {total_liters - V:.2f} liters.")
else:
    print(f"The pool is {total_liters / V * 100:.2f}% full. Pipe 1: {p1_liters / total_liters * 100:.2f}%. Pipe 2: {p2_liters / total_liters * 100:.2f}%.")