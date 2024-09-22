#Q.32 write a python script to sort (ascending and descending) a dictionary by value.

dict={"riya":5,
      "nina":8,
      "sima":3,
      "piya":2,
      "diya":1
}
print(sorted(dict.values()))
print(sorted(dict.values(),reverse=True))
