x = 15
y = 20

print ("Addition:", x+y)
print ("Subtraction:", x - y)
print ("Multiplication:", x * y)
print ("Division:", x / y)


scores = [85, 90, 78, 92, 88]

scores.append(95)  
print("After appending:", scores)  

scores.insert(2, 80)  
print("After inserting:", scores)  

new_scores = [75, 89, 94]
scores.extend(new_scores)  
print("After extending:", scores)  

scores.remove(78)  
print("After removing 78:", scores)  

average_score = sum(scores) / len(scores)  
print("Average Score:", average_score)  
