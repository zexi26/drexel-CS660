if __name__ == "__main__":
    input_file = "./input/input.txt"
    result_file = "./results.json"

    input_dict = {}
    result_dict = {}

    with open(input_file, "r") as input, open(result_file, "r") as result:

        for line in input:
            k_str, _ = line.replace('"', "").split("\t", 1)
            cat, doc = k_str.split(",")

            cat = int(cat)
            doc = int(doc)

            input_dict[doc] = cat

        for line in result:
            doc, cat = line.replace('"', "").replace("\n", "").split("\t", 1)

            cat = int(cat)
            doc = int(doc)

            result_dict[doc] = cat

        results = {
            1: [0, 0],
            0: [0, 0],
            "precision": 0.0,
            "recall": 0.0,
            "f-measure": 0.0
        }

        true_spam = 0
        true_ham = 0
        false_spam = 0
        false_ham = 0

        for a_doc, a_cat in input_dict.items():
            r_cat = result_dict.get(a_doc, -1)

            if r_cat == -1:
                continue


            print(results[a_cat][0])
            print(results[r_cat][1])
            results[a_cat][0] += 1
            results[r_cat][1] += 1

            # spam
            if a_cat == 1:
                if r_cat == 1:
                    true_spam += 1
                else:
                    false_ham += 1

            if a_cat == 0:
                if r_cat == 0:
                    true_ham += 1
                else:
                    false_spam += 1


        precision = true_spam / (true_spam + false_spam)
        results["precision"] = precision
        recall = true_spam / (true_spam + false_ham)
        results["recall"] = recall
        f_measure = (2 * precision * recall) / (precision + recall)
        results["f-measure"] = f_measure

        print("\nResults Summary:")
        for r in results:
            print("%s: %s" % (r, results[r]))



