
import trade_attributes

# Just laid out this way so no accidental spaces
BASIC_TEST_INPUT = [
    [52924702, "aaa", 13, 1136],
    [52924702, "aac", 20,  477],
    [52925641, "aab", 31,  907],
    [52927350, "aab", 29,  724],
    [52927783, "aac", 21,  638],
    [52930489, "aaa", 18, 1222],
    [52931654, "aaa",  9, 1077],
    [52933453, "aab",  9,  756]
]

BASIC_TEST_OUTPUT = [
    ["aaa", 5787, 40, 1161, 1222],
    ["aab", 6103, 69,  810,  907],
    ["aac", 3081, 41,  559,  638]
]

def test_basic_input():

    # Write the data out to a file for input
    with open("input.csv", "w") as write_file:
        for line in BASIC_TEST_INPUT:
            write_file.write(",".join([str(item) for item in line]) + "\n")

    # Run the code
    trade_attributes.process_file()

    # Validate output
    with open("output.csv", "r") as read_file:
        for index, line in enumerate(read_file):

            written_attributes = line.strip().split(",")

            # Correct number of fields
            assert len(written_attributes) == len(BASIC_TEST_OUTPUT[0]), "Incorrect number of fields written for line " + str(index)

            # Field contents
            assert written_attributes[0] == BASIC_TEST_OUTPUT[index][0], "First field does not match for line " + str(index)
            assert int(written_attributes[1]) == BASIC_TEST_OUTPUT[index][1], "Second field does not match for line " + str(index)
            assert int(written_attributes[2]) == BASIC_TEST_OUTPUT[index][2], "Third field does not match for line " + str(index)
            assert int(written_attributes[3]) == BASIC_TEST_OUTPUT[index][3], "Fourth field does not match for line " + str(index)
            assert int(written_attributes[4]) == BASIC_TEST_OUTPUT[index][4], "Fifth field does not match for line " + str(index)

