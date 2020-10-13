# Install

   $ (cd lib && make)
   $ python example/paper.py
   {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}
   $ python example/gauss.py
   z G x correct?: [396, 405] [(387, 415)] 500 False
   z G x correct?: [396, 405, 500] [(301, 510)] 446 True
   z G x correct?: [396, 405, 500, 446] [(332, 505)] 562 False
   $ python example/plot.py

# References

- Shafer, G., and Vovk, V. "A tutorial on conformal prediction."
  Journal of Machine Learning Research 9.Mar (2008): 371-421.

- Vovk, V., Gammerman, A., & Shafer, G. (2005). Algorithmic learning
  in a random world. Springer Science & Business Media.
