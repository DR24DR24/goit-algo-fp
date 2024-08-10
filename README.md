# goit-algo-fp

# Report on Monte Carlo Method Accuracy Analysis

## Experiment Description

To analyze the accuracy of the Monte Carlo method, I chose a number of experiments equal to 10,000. With this number of experiments, the error can be estimated as one divided by the square root of 10,000, that is, 1/100.

## Results

When executing the program, it was observed that the difference between the results obtained by the Monte Carlo method and the theoretical results does not exceed 1% on one hand. On the other hand, the maximum error is about half a percent, which is in good agreement with the theoretical error estimate.

The following table shows the results:

| Value | Monte Carlo Result | Theoretical Error |
|-------|---------------------|--------------------|
| 2     | 2.68%               | -0.10%             |
| 3     | 5.18%               | -0.38%             |
| 4     | 8.60%               | 0.27%              |
| 5     | 11.19%              | 0.08%              |
| 6     | 14.05%              | 0.16%              |
| 7     | 16.20%              | -0.47%             |
| 8     | 13.92%              | 0.03%              |
| 9     | 11.31%              | 0.20%              |
| 10    | 8.28%               | -0.05%             |
| 11    | 5.71%               | 0.15%              |
| 12    | 2.88%               | 0.10%              |

## Conclusions

The assessed errors within 1% and half a percent confirm the accuracy of the Monte Carlo method when conducting 10,000 experiments and are consistent with theoretical expectations.
