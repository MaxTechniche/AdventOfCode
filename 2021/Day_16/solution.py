from time import time

# First 3 bits: packet version
# Second 3 bits: packet type ID
# Type 4 ID: Literal value
#

values = []


def get_int(bits):
    return int(bits, 2)


def parse_bits(bits):
    global values
    values.append('[')
    version_total = int(bits[0:3], 2)
    packet_type = int(bits[3:6], 2)
    pos = 6

    if packet_type == 4:
        version, pos_change = parse_4(bits[pos:])
        version_total += version
        pos += pos_change
        values.append(']')
        return version_total, pos

    length_type = bits[pos]
    pos += 1
    values.append(str(packet_type))
    if length_type == '0':
        total_length = int(bits[pos:pos+15], 2)
        pos += 15
        current_pos = pos
        pos += total_length
        while total_length > 0:
            version, pos_change = parse_bits(
                bits[current_pos:current_pos+total_length])
            version_total += version
            total_length -= pos_change
            current_pos += pos_change
        values.append(']')
        return version_total, pos

    if length_type == '1':
        num_of_sub_packets = int(bits[pos:pos+11], 2)
        pos += 11
        while num_of_sub_packets > 0:
            version, pos_change = parse_bits(bits[pos:])
            version_total += version
            pos += pos_change
            num_of_sub_packets -= 1

        values.append(']')
        return version_total, pos

    values.append(']')
    return version_total


def parse_values(values):
    total = 0
    pos = 2
    type_ = values[1]
    current_values = []
    while pos < len(values):
        if type(values[pos]) is str:
            if values[pos] == '[':
                value, pos_change = parse_values(values[pos:])
                current_values.append(value)
                pos += pos_change
            elif values[pos] == ']':

                if type_ in '04':
                    total += sum(current_values)
                elif type_ == '1':
                    x = 1
                    for val in current_values:
                        x *= val
                    total += x
                elif type_ == '2':
                    total += min(current_values)
                elif type_ == '3':
                    total += max(current_values)
                elif type_ == '5':
                    if current_values[0] > current_values[1]:
                        total += 1
                elif type_ == '6':
                    if current_values[0] < current_values[1]:
                        total += 1
                elif type_ == '7':
                    if current_values[0] == current_values[1]:
                        total += 1
                return total, pos
            else:
                type_ = values[pos]
        else:
            current_values.append(values[pos])
        pos += 1

    return total, pos


def parse_4(bits):
    global values
    values.append('4')
    pos = 0
    final_bit_string = ''
    for p in range(0, len(bits), 5):
        final_bit_string += bits[p+1:p+5]
        pos += 5

        if bits[p] == '0':
            break

    values.append(int(final_bit_string, 2))

    return 0, pos


def main():
    t1 = time()

    with open("2021/Day_16/input") as f:
        sections = f.read().split('\n\n')
        hex_packet = sections[0].strip()
        hex_to_bin = [line.split(' = ') for line in sections[1].splitlines()]
        hex_to_bin = {l: r for l, r in hex_to_bin}

    bin_packet = ''.join([hex_to_bin[i] for i in hex_packet])

    version_total = parse_bits(bin_packet)[0]

    print('Version Total: ' + str(version_total))

    print('Value Total: ' + str(parse_values(values)[0]))

    print("Time:", time() - t1)


main()
