def  per(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/500)*100 
    return p
marks1 = [47,34,65,23,56]
persentage1 = per(marks1)



marks2 = [33,55.78,58.56]
persentage2 = per(marks2)

print(persentage1, persentage2)