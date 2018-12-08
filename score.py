from normalize import normalize
from wer import word_errors

samples = [
    # (truth, predicted)
    ('1 2 3 4', 'one two three four'),
    ('Hello, today we discussing software.', 'hello today we are discussing software'),
    ('The cat is too.', 'the hat is too big')
]

total_scores = []
total_len = 0
for i, sample in enumerate(samples):
    print("===== SAMPLE #%s =====" % i)

    # load test data
    truth, predicted = sample[0], sample[1]
    print("truth: %s" % truth)
    print("predict: %s" % predicted)
    print("\n")

    # normalize test data
    truth, predicted = normalize(truth), normalize(predicted)
    print("truth (normalize): %s" % truth)
    print("predict (normalize): %s" % predicted)
    print("\n")

    # score test data
    wer_score, ref_len = word_errors(truth, predicted)
    print("wer: %s" % (wer_score / float(ref_len)))

    # keep track of running average
    total_scores.append(wer_score)
    total_len += ref_len
    print("\n")

    # pause so user can inspect results
    raw_input("<Hit the ENTER key to continue>")
    print("\n\n")

# example for multiple samples
average_wer = float(sum(total_scores)) / float(total_len)
print("Average WER: %s" % average_wer)
