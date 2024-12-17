from collections import defaultdict

from app.models.models import Command, Direction


def clean_office(x: int, y: int, commands: list[Command]) -> int:
    """Clean the office floor and return the number of cleaned tiles"""
    row_ranges = defaultdict(list)
    col_ranges = defaultdict(list)
    curr_x, curr_y = x, y
    row_ranges[curr_y].append((curr_x, curr_x))

    for command in commands:
        d = command.direction
        steps = command.steps
        if d == Direction.east:
            row_ranges[curr_y].append((curr_x, curr_x + steps))
            curr_x += steps
        elif d == Direction.west:
            row_ranges[curr_y].append((curr_x - steps, curr_x))
            curr_x -= steps
        elif d == Direction.north:
            col_ranges[curr_x].append((curr_y, curr_y + steps))
            curr_y += steps
        else:
            col_ranges[curr_x].append((curr_y - steps, curr_y))
            curr_y -= steps

    cleaned_tiles = 0
    # Iterate through horizontal lines, merge overlapping ones,
    # and count the lengths.
    for curr_y, ranges in row_ranges.items():
        merged_ranges = merge_ranges(ranges)
        row_ranges[curr_y] = merged_ranges
        for start, end in merged_ranges:
            cleaned_tiles += end - start + 1

    # Iterate through vertical lines, merge overlapping ones,
    # count the lengths, and subtract 1 for every intersecting
    # horizontal line.
    for curr_x, vert_ranges in col_ranges.items():
        merged_vert_ranges = merge_ranges(vert_ranges)
        for vert_start, vert_end in merged_vert_ranges:
            current_count = vert_end - vert_start + 1
            for curr_y in range(vert_start, vert_end + 1):
                if curr_y in row_ranges:
                    for hor_start, hor_end in row_ranges[curr_y]:
                        if hor_start <= curr_x <= hor_end:
                            current_count -= 1
                            break

            cleaned_tiles += current_count

    return cleaned_tiles


def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]

    for current in sorted_ranges[1:]:
        previous = merged[-1]

        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)

    return merged
