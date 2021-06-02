import logging

logging.basicConfig(filename='report.log', filemode='w', level=logging.INFO)
counter = {
    'Glider': 0,
    'Block': 0,
    'Behive': 0,
    'Loaf': 0,
    'Boat': 0,
    'Tub': 0,
    'Blinker': 0,
    'Toad': 0,
    'Spaceship': 0,
    'Beacon': 0,
    'Others': 0
}


def print_report(num):
    frame = "\tFrame " + str(num)
    logging.info(frame)
    num += 1
    for s in counter:
        line = "\t" + s + ": " + str(counter[s])
        logging.info(line)

