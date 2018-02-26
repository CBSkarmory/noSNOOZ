#!/usr/bin/env python3
import analytics, sys, util

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    if argc == 2:
        preds = analytics.public_get_predictions(argv[1])
    else:
        preds = analytics.public_get_predictions(None)
    util.print_col(preds)
