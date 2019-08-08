import argparse
import logging

import numpy as np
from page_rank import PageRankSimple

if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser(description="PageRank with MRJob")

    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("--epsilon", type=float, default=1.0e-8, help="Convergence value")

    args = parser.parse_args()

    input_file = args.input
    output_dir = "output/graph-%s"

    iteration = 1
    running = True
    epsilon = args.epsilon

    last_v = []
    v = []

    logging.info("Running PageRank algorithm on %s with epsilon value %s" % (input_file, epsilon))

    while running:
        logging.info("Running iteration %s" % iteration)

        job_input = input_file if iteration == 1 else output_dir % (iteration - 1)
        job_output = "--output-dir=%s" % (output_dir % iteration)

        job = PageRankSimple([job_input, job_output])

        with job.make_runner() as runner:
            runner.run()

            last_v = v

            # get page_rank vector for this iteration
            v = [value[0] for _, value in job.parse_output(runner.cat_output())]

            # compare it to last iteration to check for convergence
            if len(last_v) > 0:
                running = np.linalg.norm(np.array(v) - np.array(last_v), 2) > epsilon

        iteration += 1
