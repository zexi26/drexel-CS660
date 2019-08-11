import argparse
import logging
import shutil
import os

import numpy as np
from page_rank import PageRankJob, DanglingJob

if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser(description="PageRank with MRJob")

    parser.add_argument("input", type=str, help="Input file")
    parser.add_argument("--epsilon", type=float, default=1.0e-8, help="Convergence value")

    args = parser.parse_args()

    input_file = args.input
    output_dir = "output/"

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)

    iteration = 1
    running = True
    epsilon = args.epsilon

    last_v = []
    v = []

    logging.info("Running PageRank algorithm on %s with epsilon value %s" % (input_file, epsilon))

    while running:
        logging.info("Running iteration %s" % iteration)

        dangling_nodes = []

        main_job_input = input_file if iteration == 1 else output_dir
        main_job_output = "--output-dir=%s" % (output_dir)

        main_job = PageRankJob([main_job_input, main_job_output])

        with main_job.make_runner() as main_runner:
            main_runner.run()

            counters = main_runner.counters()

            out_job = main_job
            out_runner = main_runner

            # check for dangling nodes
            if len(counters[0]) > 1:
                dangling_nodes = counters[0]["dangling_nodes"]
                num_nodes = counters[0]["nodes"]["count"]

                print([str(num_nodes), str(dangling_nodes)])

                dangling_job = DanglingJob([output_dir, [str(num_nodes), str(dangling_nodes)], main_job_output])

                with dangling_job.make_runner() as dangling_runner:
                    dangling_runner.run()

                    out_job = dangling_job
                    out_runner = dangling_runner

            last_v = v

            for line in out_job.parse_output(out_runner.cat_output()):
                print(line)

            # get page_rank vector for this iteration
            v = [value[0] for _, value in out_job.parse_output(out_runner.cat_output())]

            # compare it to last iteration to check for convergence
            if len(last_v) > 0:
                running = np.linalg.norm(np.array(v) - np.array(last_v), 2) > epsilon

            iteration += 1

        # running = False
