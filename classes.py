class HashTable:
    def __init__(self,class_size):
        self.class_size = class_size
        self.array = {"A":[],"B":[],"C":[],"D":[]}

    def hash(self,score):
        if score >= 90:
            return "A"
        elif score < 90 and score>= 80:
            return "B"
        elif score < 80 and score>= 70:
            return "C"
        elif score < 70 and score>= 60:
            return "D"
        else:
            return None

    def insert(self,list):
        for i in list:
            current_name = i["name"]
            current_score = i["score"]
            current_class = self.hash(current_score)
            if current_class != None:
                if len(self.array[current_class]) >= self.class_size:
                    print("class is full")
                else:
                    self.array[current_class].append({"name":current_name,"score":current_score})

    def print_table(self):
        for n in self.array:
            print("------in class %s------"%(n))
            for i in self.array[n]:
                print("Name: %s - Score: %s"%(i["name"],i["score"]))


num_students = int(input("insert max num of students: "))
classes = HashTable(num_students)
students = [
    {
        "name": "Jean-Luc Garza",
        "score": 24
    },
    {
        "name": "Teddy Munoz",
        "score": 79
    },
    {
        "name": "Georgia Ali",
        "score": 17
    },
    {
        "name": "Vicky Calhoun",
        "score": 8
    },
    {
        "name": "Awais Weaver",
        "score": 65
    },
    {
        "name": "Athena Kline",
        "score": 52
    },
    {
        "name": "Zacharia Whitaker",
        "score": 38
    },
        {
        "name": "Clarice Davenport",
        "score": 99
    },
    {
        "name": "Viktoria Flynn",
        "score": 84
    },
    {
        "name": "Ianis Crossley",
        "score": 20
    },
    {
        "name": "Johnnie Owens",
        "score": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "score": 33
    },
    {
        "name": "Adeel Nieves",
        "score": 100
    },
    {
        "name": "Dustin Villegas",
        "score": 98
    },
    {
        "name": "Maxine Hughes",
        "score": 65
    },
    {
        "name": "Bilaal Harding",
        "score": 79
    },
    {
        "name": "Maddie Ventura",
        "score": 71
    },
    {
        "name": "Leroy Rees",
        "score": 44
    },
    {
        "name": "Wanda Frank",
        "score": 73
    },
    {
        "name": "Margaux Herbert",
        "score": 80
    },
    {
        "name": "Ali Rios",
        "score": 70
    },
    {
        "name": "Nigel Santiago",
        "score": 25
    },
    {
        "name": "Markus Greene",
        "score": 78
    },
    {
        "name": "Harlan Parrish",
        "score": 97
    },
    {
        "name": "Baran Davidson",
        "score": 43
    },
    {
        "name": "Seth Rodriguezh",
        "score": 67
    },
    {
        "name": "Diego Mayer",
        "score": 100
    },
]
classes.insert(students)
print("-"*40)
classes.print_table()
