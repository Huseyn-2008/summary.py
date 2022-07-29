def sum(*numbers):
     summary = 0
     for i in numbers:
          summary += i
          print(f'Result {summary}')
sum(1, 2, 3, 4)
